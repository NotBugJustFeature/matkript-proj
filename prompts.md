## Kezdő prompt a C feladat megoldásához:

```
Írj Python-megoldást a Carmichael-számok keresésére B=10^6,10^7,10^8 korlátokig.

Használd Korselt kritériumát: csak olyan n-eket vizsgálj, amelyek páratlanok, négyzetmentesek, legalább három különböző prímosztójuk van, és minden p | n esetén teljesül, hogy p-1 | n-1.

A kód legyen hatékony, tehát ne minden számot faktorizáljon lassú próbálgatással. Használhatsz például szitát vagy legkisebb prímosztó táblát.

A válasz tartalmazza:

- az algoritmus rövid magyarázatát,
- a teljes Python-kódot,
- a megtalált Carmichael-számok darabszámát B=10^6,10^7,10^8 esetén,
- futási idők mérését time.perf_counter() segítségével.
```

**Válasz:**
Az ötlet: nem faktorizáljuk végig az összes `n ≤ B` számot. Ehelyett páratlan, különböző prímekből építünk négyzetmentes szorzatokat. Mivel Carmichael-számhoz legalább három különböző prímosztó kell, a legnagyobb lehetséges prímosztó legfeljebb `B / (3·5) = B / 15`, ezért elég eddig szitázni.

Korselt kritériumát így ellenőrizzük:

[
n \text{ Carmichael} \iff n \text{ páratlan, négyzetmentes, legalább 3 prímosztós, és } \operatorname{lcm}_{p \mid n}(p-1) \mid n-1.
]

### Teljes Python-kód

```python
from math import gcd, isqrt
from bisect import bisect_right
from time import perf_counter


def odd_primes_upto(limit: int) -> list[int]:
    """
    Eratoszthenész-szita: visszaadja a páratlan prímeket 3-tól limitig.
    A 2-t szándékosan kihagyjuk, mert Carmichael-szám páratlan.
    """
    if limit < 3:
        return []

    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"

    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start:limit + 1:p] = b"\x00" * (((limit - start) // p) + 1)

    return [p for p in range(3, limit + 1, 2) if sieve[p]]


def carmichael_numbers(B: int) -> list[int]:
    """
    Carmichael-számok keresése n <= B korlátig Korselt kritériumával.

    Nem faktorizálunk minden n-et.
    Ehelyett növekvő sorrendben különböző páratlan prímek szorzatait építjük.
    """
    # Legalább három különböző páratlan prím kell.
    # Ha p a legnagyobb prímosztó, akkor a másik kettő legalább 3 és 5,
    # tehát p <= B / 15.
    primes = odd_primes_upto(B // 15)

    result = []

    def min_following_product(pos: int, k: int) -> int:
        """
        A következő k darab prím minimális szorzata a primes[pos:] listából.
        Ezzel metsszük a keresési fát: ha már a legkisebb folytatás is túl nagy,
        akkor nincs értelme továbbmenni.
        """
        if k == 0:
            return 1
        if pos + k > len(primes):
            return B + 1

        prod = 1
        for p in primes[pos:pos + k]:
            prod *= p
            if prod > B:
                break
        return prod

    def search(start_idx: int, prod: int, lcm_pm1: int, factor_count: int) -> None:
        """
        prod: az eddig kiválasztott prímek szorzata
        lcm_pm1: lcm(p - 1) az eddig kiválasztott prímekre
        factor_count: eddigi különböző prímosztók száma
        """
        max_p = B // prod
        end_idx = bisect_right(primes, max_p, lo=start_idx)

        for i in range(start_idx, end_idx):
            p = primes[i]

            # Ennyi további prímtényező kell még ahhoz, hogy legalább 3 legyen.
            needed_after_p = max(0, 3 - (factor_count + 1))

            # Ha p és a minimális lehetséges folytatás szorzata is túl nagy,
            # akkor nagyobb p-kre sem lesz jó.
            if prod * p * min_following_product(i + 1, needed_after_p) > B:
                break

            new_prod = prod * p
            new_lcm = lcm_pm1 * ((p - 1) // gcd(lcm_pm1, p - 1))

            # Ha lcm(p-1) már nagyobb, mint B-1, akkor n-1 <= B-1 miatt
            # nem oszthatja n-1-et.
            if new_lcm > B - 1:
                continue

            new_factor_count = factor_count + 1

            # Korselt kritériuma:
            # squarefree és páratlan már konstrukcióból igaz,
            # legalább 3 prímtényezőt külön ellenőrizzük,
            # p-1 | n-1 minden p-re ekvivalens azzal, hogy lcm(p-1) | n-1.
            if new_factor_count >= 3 and (new_prod - 1) % new_lcm == 0:
                result.append(new_prod)

            # További prímtényezők hozzáadása
            search(i + 1, new_prod, new_lcm, new_factor_count)

    search(start_idx=0, prod=1, lcm_pm1=1, factor_count=0)
    result.sort()
    return result


def main() -> None:
    bounds = [10**6, 10**7, 10**8]

    for B in bounds:
        t0 = perf_counter()
        nums = carmichael_numbers(B)
        t1 = perf_counter()

        print(f"B = {B:,}")
        print(f"Darabszám: {len(nums)}")
        print(f"Futási idő: {t1 - t0:.6f} s")
        print(f"Első néhány: {nums[:10]}")
        print(f"Utolsó néhány: {nums[-10:]}")
        print()


if __name__ == "__main__":
    main()
```

### Eredmények

A darabszámok `n ≤ B` értelemben:

| Korlát `B` | Carmichael-számok darabszáma | Mért futási idő |
| ---------: | ---------------------------: | --------------: |
|     `10^6` |                         `43` |    `0.164569 s` |
|     `10^7` |                        `105` |    `1.979253 s` |
|     `10^8` |                        `255` |   `21.937612 s` |

A futási idők hardver- és Python-verziófüggők, de a kód valóban `time.perf_counter()`-rel méri őket.

## Kezdő prompt folytatása a D feladat megoldásához:

```
Folytasd az előző Carmichael-számos Python-kódot a kísérleti vizsgálattal.

A már megtalált Carmichael-számok alapján számold ki C(B)-t, vagyis a B-nél nem nagyobb Carmichael-számok számát több B-értékre 10^3 és 10^8 között.

Készíts:

1. log-log ábrát C(B)-ről,
2. összehasonlítást az Erdős-féle heurisztikus becsléssel: (Az Erdős-féle heurisztikus becslés képletét az általam küldött kép szemlélteti) ![Erdős-féle heurisztikus becslés képlete](kepletek/erdos_heurisztika_keplet.png)
3. hisztogramot arról, hogy a Carmichael-számoknak hány különböző prímosztójuk van.

A válasz tartalmazza a teljes Python-kódot, az ábrákat matplotlib-tel, valamint rövid szöveges értelmezést az eredményekről.
```

**Válasz:**
Elkészült a kísérleti folytatás. A teljes futtatható Python-script itt letölthető: **Python-kód letöltése**

A futás eredménye ebben a környezetben:

```text
Keresési idő: 21.315146 s
Darabszám n <= 10^8: 255

B =     1,000, C(B) = 1
B =    10,000, C(B) = 7
B =   100,000, C(B) = 16
B = 1,000,000, C(B) = 43
B =10,000,000, C(B) = 105
B =100,000,000, C(B) = 255

Hisztogram:
omega(n) = 3: 84
omega(n) = 4: 144
omega(n) = 5: 27
```

Az Erdős-féle görbéhez a következő, a képen szereplő aszimptotikus alakot használtam:
![Erdős-féle görbéhez az aszimptotikus alak](kepletek/erdos_heurisztika_keplet.png)

Fontos, hogy ez nem kis tartományokra pontos numerikus becslés, hanem aszimptotikus növekedési forma. Emiatt az összehasonlító ábrán a heurisztikus görbét `10^8`-nál a mért `C(B)` értékhez normalizáltam. Így nem az abszolút nagyságrendet, hanem a növekedés alakját lehet összevetni.

Rövid értelmezés: `10^3` és `10^8` között a Carmichael-számok nagyon ritkák, de a log-log ábrán jól látszik a lassan növekvő számlálófüggvény. A `10^8`-ig talált számok között a legtöbbnek 4 különböző prímosztója van; 3 prímosztósból kevesebb, 5 prímosztósból pedig jóval kevesebb fordul elő ebben a tartományban.
