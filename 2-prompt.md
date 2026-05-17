```
Van egy ilyen feladatom. Neked az a feladatod h megmond h jo-e a gondolat menetem vagy nem. Bizonyítsák be, hogy minden Carmichael-szám páratlan, és legalább három külön- böz˝o prímtényez˝oje van. gondolat menet: egyelore csak a paratlannal foglalkozunk szoval a prim osztok csak egyszer fordulhatnak elo vagyis négyzetmentes. vegyuk pl a 2,3,5,7,11-et peldanak. Amenyiben az oszto primjei kozott szerepel a 2 az csorbirja a p | n p - 1 | n - 1 feltetelt mert a p - 1 | n - 1 esettben paratlan szamot kellene parossal osztani ami z-ben nem lehetseges
```

```
A gondolatmeneted jó irányba megy, de van benne egy kis pontatlanság.

A Carmichael-számokra használható a Korselt-kritérium:

Ha n Carmichael-szám, akkor n összetett, négyzetmentes, és minden p∣n prímosztóra:

p−1∣n−1

A páratlanság bizonyítása így jó:

Tegyük fel indirekten, hogy n páros Carmichael-szám. Mivel n négyzetmentes, ezért 2∣n, de 4∤n.

Viszont ha n páros, akkor n−1 páratlan.

Mivel n összetett és négyzetmentes, van egy páratlan prímosztója is, legyen ez p. Ekkor p∣n, tehát Korselt szerint:

p−1∣n−1

De p páratlan prím, ezért p−1 páros. Tehát egy páros számnak kellene osztania egy páratlan számot, ami lehetetlen.

Ezért n nem lehet páros, tehát minden Carmichael-szám páratlan.

A hibád csak annyi, hogy nem a p=2 prímmel van gond, mert ott p−1=1, és 1∣n−1 mindig igaz. Hanem egy másik, páratlan prímosztóval kell érvelni.
```

```
minimum 3 darab: En ugy kezdenek neki h mivel p | n es p - 1 | n - 1 az alap osszefuggesunk. igy az n legyegyen egyenlo n = pr // 2 oszto n = pqr // 3 oszto azzal a kikotessel h p < q < r r | n 2: r | pr r - 1 | pr - 1 De a kongruenciareláció miatt: pr - 1 == p*1-1 (mod r - 1) igy p - 1 == 0 (mod r - 1) azaz r - 1 | p - 1 mikozben p < r mig 3. as esettben ugyan ennek a levezetesnek az eredmenye r - 1 | pq - 1
```

```
Igen, ez a 2 prímtényezős esethez jó gondolatmenet.

Ha n=pq, ahol p<q, akkor q∣n, ezért Korselt szerint:

q−1∣n−1=pq−1

Mivel q≡1(modq−1), ezért:

pq−1≡p⋅1−1=p−1(modq−1)

Tehát:

q−1∣p−1

De p<q, ezért:

p−1<q−1

Ez lehetetlen, mert egy nagyobb pozitív szám nem oszthat egy nála kisebb pozitív számot. Tehát Carmichael-számnak nem lehet pontosan két különböző prímtényezője.

A 3 prímtényezős esetet nem kell cáfolni, mert a feladat azt állítja, hogy legalább három különböző prímtényezője van. Tehát azt kell kizárni, hogy 1 vagy 2 legyen.

Az 1 prímtényezős eset: ha n=p lenne, az prím, de Carmichael-szám definíció szerint összetett.

Szóval a teljes lezárás:

n

=p,n

=pq

ezért n-nek legalább három különböző prímtényezője van.
```
