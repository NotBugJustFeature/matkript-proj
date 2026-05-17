```
Van egy ilyen feladatom. Neked az a feladatod h megmond h jo-e a gondolat menetem vagy nem. (a) Bizonyítsák be Korselt kritériumát. Ehhez használják a kínai maradéktételt: ha n = p1 · · · pk négyzetmentes, akkor an ≡ a (mod n) minden a-ra pontosan akkor, ha an ≡ a (mod pi) minden i-re, ami Fermat kis tétele alapján ekvivalens pi − 1 | n − 1-gyel. a gondolat menetem: Szoval van nekunk a n negyzetmentes, es minden p | n prımre p - 1 | n - 1. n = p1 _ p2 _ ... \* pk a ^ n == a (mod n) a ^ n == a (mod pi) Fermat kis tétele szerint ha a ^ (Pi - 1) == 1 mod pi akkor (ha 0 akkor nincs teendonk) a ^ pi == a (mod pi) a ^ pi-1 == 1 (mod pi) Jol gondolom h ezek alapjan at kellene vezetni a p - 1 | n - 1-re?
```

Igen, jó irányban gondolod, csak egy pontosítást kell tenni: nem a
p<sub>i</sub> ≡ a ( mod p<sub>i</sub> )-ből vezeted le, hanem a n≡a( mod p<sub>i</sub> )-t kötöd össze azzal, hogy p<sub>i</sub>−1 | n−1.
