from math import gcd, isqrt, log
from bisect import bisect_right
from collections import Counter
from time import perf_counter
import matplotlib.pyplot as plt


def odd_primes_upto(limit: int) -> list[int]:
    """
    Eratoszthenész-szita: páratlan prímek 3-tól limitig.
    A 2 kimarad, mert Carmichael-szám páratlan.
    """
    if limit < 3:
        return []

    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"

    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)

    return [p for p in range(3, limit + 1, 2) if sieve[p]]


def carmichael_numbers_with_factor_counts(B: int) -> list[tuple[int, int]]:
    """
    Carmichael-számok n <= B-ig Korselt kritériumával.

    Kimenet:
        [(n, omega(n)), ...],
    ahol omega(n) a különböző prímosztók száma.

    A keresés nem faktorizál minden n-et, hanem növekvő prímekből
    építi a squarefree páratlan szorzatokat.
    """
    primes = odd_primes_upto(B // 15)
    npr = len(primes)
    result: list[tuple[int, int]] = []

    def min_following_product(pos: int, k: int) -> int:
        """
        A következő k prím minimális szorzata a primes[pos:] listából.
        Metszéshez használjuk: ha a legkisebb folytatás is túl nagy,
        a nagyobb prímekkel sem lesz jó.
        """
        if k == 0:
            return 1
        if pos + k > npr:
            return B + 1

        prod = 1
        for j in range(k):
            prod *= primes[pos + j]
            if prod > B:
                break
        return prod

    def search(start_idx: int, prod: int, lcm_pm1: int, factor_count: int) -> None:
        """
        prod: eddigi prímek szorzata
        lcm_pm1: lcm(p - 1) az eddigi p prímekre
        factor_count: eddigi különböző prímosztók száma
        """
        end_idx = bisect_right(primes, B // prod, lo=start_idx)

        for i in range(start_idx, end_idx):
            p = primes[i]

            needed_after_p = max(0, 3 - (factor_count + 1))
            if prod * p * min_following_product(i + 1, needed_after_p) > B:
                break

            new_prod = prod * p
            new_lcm = lcm_pm1 * ((p - 1) // gcd(lcm_pm1, p - 1))

            if new_lcm > B - 1:
                continue

            new_factor_count = factor_count + 1

            # Korselt:
            # páratlan és négyzetmentes konstrukcióból,
            # legalább 3 prímosztó külön feltétel,
            # minden p | n esetén p - 1 | n - 1 ekvivalens:
            # lcm(p - 1 : p | n) | n - 1.
            if new_factor_count >= 3 and (new_prod - 1) % new_lcm == 0:
                result.append((new_prod, new_factor_count))

            search(i + 1, new_prod, new_lcm, new_factor_count)

    search(0, 1, 1, 0)
    result.sort()
    return result


def erdos_heuristic(B: float) -> float:
    """
    Az Erdős-féle alak konstans és o(1) nélkül:

        B^(1 - log(log(log(B))) / log(log(B)))

    Ez kis B-kre nem pontos becslés, inkább növekedési forma.
    """
    return B ** (1.0 - log(log(log(B))) / log(log(B)))


def main() -> None:
    Bmax = 10**8

    t0 = perf_counter()
    pairs = carmichael_numbers_with_factor_counts(Bmax)
    t1 = perf_counter()

    carmichaels = [n for n, k in pairs]
    factor_counts = [k for n, k in pairs]

    # Több B-érték 10^3 és 10^8 között:
    # egész hatványok + sűrűbb logaritmikus rács.
    B_grid = sorted(
        set(
            [10**e for e in range(3, 9)]
            + [round(10 ** (3 + 5 * i / 80)) for i in range(81)]
        )
    )

    C_values = [bisect_right(carmichaels, B) for B in B_grid]
    H_values = [erdos_heuristic(float(B)) for B in B_grid]

    # A képlet aszimptotikus, az o(1) tag és konstans nélkül.
    # Ezért a heurisztikus görbét 10^8-nál a mért C(B)-hez igazítjuk.
    scale = C_values[-1] / H_values[-1]
    H_scaled = [scale * h for h in H_values]

    print(f"Keresési korlát: Bmax = {Bmax:,}")
    print(f"Talált Carmichael-számok: {len(carmichaels)}")
    print(f"Keresési idő: {t1 - t0:.6f} s")
    print()

    print("C(B) néhány fontos B-re:")
    for B in [10**e for e in range(3, 9)]:
        print(f"B = {B:>9,}, C(B) = {bisect_right(carmichaels, B):>3}")

    print()
    print("Hisztogram omega(n), azaz a különböző prímosztók száma szerint:")
    hist = Counter(factor_counts)
    for k in sorted(hist):
        print(f"omega(n) = {k}: {hist[k]}")

    # 1. log-log ábra C(B)-ről
    plt.figure()
    plt.loglog(B_grid, C_values, marker="o", linewidth=1)
    plt.xlabel("B")
    plt.ylabel("C(B)")
    plt.title("Carmichael-számok számlálófüggvénye")
    plt.grid(True, which="both")
    plt.tight_layout()
    plt.savefig("charts/carmichael_loglog.png", dpi=160)
    plt.show()

    # 2. összehasonlítás az Erdős-féle alakkal
    plt.figure()
    plt.loglog(B_grid, C_values, marker="o", linewidth=1, label="mért C(B)")
    plt.loglog(
        B_grid,
        H_scaled,
        linestyle="--",
        linewidth=1,
        label="Erdős-alak, 10^8-nál normalizálva",
    )
    plt.xlabel("B")
    plt.ylabel("érték")
    plt.title("C(B) összehasonlítása az Erdős-féle heurisztikus alakkal")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.savefig("charts/erdos_comparison.png", dpi=160)
    plt.show()

    # 3. hisztogram a különböző prímosztók számáról
    xs = sorted(hist)
    ys = [hist[x] for x in xs]

    plt.figure()
    plt.bar(xs, ys)
    plt.xlabel("különböző prímosztók száma")
    plt.ylabel("Carmichael-számok száma")
    plt.title(f"Prímosztók számának eloszlása n ≤ {Bmax:,}")
    plt.xticks(xs)
    plt.tight_layout()
    plt.savefig("charts/factor_count_histogram.png", dpi=160)
    plt.show()


if __name__ == "__main__":
    main()
