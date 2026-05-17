1.

```paratlan:
A Korsel kritérium szerint
n négyzetmentes,
minden p ∣ n prímre teljesül:

mivel négyzetmentes ezért 2 | n
2 - 1 | n - 1
1 | n - 1

minimum 3 prim
2 minimum az osszetett szam definiciojabol kiindulva
tegyuk fel h
n = pq
q - 1 | n - 1
q - 1 | pq - 1

kongruenciareláció miatt:
pq−1 == p*1-1 (mod q-1)

De pq - 1 == 0 (mod q-1)
de ebben a fellalasban
p - 1 == 0 (mod q-1)
ami ellentmondas mert
q - 1 | p - 1
0 < p - 1 < q - 1

mig 3 prim eseten

n = pqr, p < q < r
r - 1 | pqr - 1
r == 1 (mod r - 1)
pqr - 1 == pq - 1 (mod r - 1)
r - 1 | pq - 1
pq - 1 >= r - 1
```

2.

```
paratlan:
Szoval ha van paros prim az osztok kozott akkor Korsel masodik feltele alapjan nem lesz oszthato mivel paratlant nem lehet parossal osztani Z-ben
Mivel 3 prim osztoja van es az egyik paros akkor
p | p-1
2 | 1
3 | 2
5 | 4

minimum 3 prim
2 minimum az osszetett szam definiciojabol kiindulva
tegyuk fel h
n = pq
q - 1 | n - 1
q - 1 | pq - 1

kongruenciareláció miatt:
pq−1 == p*1-1 (mod q-1)

De pq - 1 == 0 (mod q-1)
de ebben a fellalasban
p - 1 == 0 (mod q-1)
ami ellentmondas mert
q - 1 | p - 1
0 < p - 1 < q - 1

mig 3 prim eseten

n = pqr, p < q < r
r - 1 | pqr - 1
r == 1 (mod r - 1)
pqr - 1 == pq - 1 (mod r - 1)
r - 1 | pq - 1
pq - 1 >= r - 1
```

3.  Először is egy Carmichael egy olyan szám amelyre ha bármely pozitív egész számot hatványozzuk, majd az eredményt maradékosan osszuk ezzel a Carmichael számunkal, akkor vissza kapjuk az eredeti számot abban az esetben ha az a szám nagyobb mint 1 és kisebb mint a Carmichael számunk.

Ezentúl a Carmichael számokra teljesül a Fermat tétel is, miszerint ha veszünk hozzájuk egy relatív prímet majd azt a relatív prímet a Carmichael számunk -1 edik hatványra emeljük, akkor az eredményt maradékosan osztva ezzel a Carmichael számmal 1-et kapunk eredményül.

Ezentúl a Carmichael számokra igaz még az is, hogy legalább 3 prím szorzatából állnak valamint négyzetmentesek, ami azt jelenti, nincs olyan prím mely több mint egyszer szerepelne a szorzatban. Ezentúl a szorzatban szereplő egyes prímek -1 osszák magát a kijött Carmichael szám -1-et.

4.  A Korselt kritériuma azt mondja ki, hogy egy n szám pontosan akkor Carmichael, ha ugye négyzetmentes, szóval a prímtényezős szorzatában nem szerepel egy prím többször. Valamint minden egyes prím amely adja a prímtényezős szorzatot ha kivonunk belőlük 1-et akkor osztaniuk kell magát az n-1 et.

5.  A kínai maradéktétel azt mondja ki, hogy van egy számunk amelynek prímtényezős felbontása ha négyzetmentes, tehát az egyes prímek csak egyszer fordulnak elő: n = p1p2...pk, akkor egy 'a' szám maradéka az egyes prímekre nézve egyértelműen meghatározza a 'n'-re vett maradékot is.

6.

```Tegyük fel, hogy egy Carmichael-számnak csak két különböző prímtényezője van, tehát n=pq, ahol p<q prímek. Korselt kritériuma szerint minden prímosztóra teljesülnie kell annak, hogy p−1∣n−1. Különösen:

q−1∣pq−1.

Mivel q≡1(modq−1), ezért pq−1 maradéka q−1-gyel osztva ugyanaz, mint p−1 maradéka. Így következik, hogy

q−1∣p−1.

Ez azonban lehetetlen, mert p<q, tehát p−1<q−1, és egy nagyobb pozitív szám nem oszthat egy nála kisebb pozitív számot. Ez ellentmondás, tehát egy Carmichael-számnak nem lehet csak két prímtényezője, vagyis legalább három különböző prímtényezője van.
```

```
Tegyük fel, hogy létezik páros Carmichael-szám n. Ekkor 2∣n, és mivel a Carmichael-számok Korselt kritériuma szerint négyzetmentesek, n-nek van legalább egy páratlan prímosztója is, jelöljük ezt p-vel. Korselt kritériuma szerint ekkor

p−1∣n−1.

Mivel p páratlan prím, ezért p−1 páros szám. Viszont ha n páros, akkor n−1 páratlan. Ez lehetetlen, mert páros szám nem oszthat páratlan számot. Ellentmondásra jutottunk, tehát minden Carmichael-szám páratlan.
```

7.

A Korselt kritérium-ot kicsit átírva, ha a Carmichael-számunk páros lenne akkor már nem lenne igaz az, hogy a számunk prímtényezős felbontásában szereplő minden prímekből ha levonunk -1-et osszák az eredeti számunk -1-et, mert ha az eredeti számunk páros lenne, akkor ha levonunk -1-et páratlan számot kapunk, viszont amikor a prím-ből vonunk le -1-et ott meg páros számot kívétel ez alól a 2, viszont mivel még lennie-kell másik prímnek is és az már tuti nem lesz páros szám, így mikor vissza ellenőrizzük, hogy minden prím -1 ossza-e a n-1-et olyat esetekbe botlunk amikor páros számnak kellene osztania páratlan számot, ami Z ben nem lehetséges
