# Emelt szintű Python gyakorló feladatsor -- Adatszerkezetek

## 1. feladat -- Egyszerű adatszerkezetek (int, float, string, bool)

Írj programot, amely:

1.  Bekér egy egész számot (életkor).
2.  Bekér egy lebegőpontos számot (testmagasság méterben).
3.  Bekér egy nevet (string).
4.  Állapítsa meg logikai változó segítségével, hogy a felhasználó
    nagykorú-e (\>= 18).
5.  Írja ki az adatokat formázott szövegként.
6.  Számítsa ki, hogy hány év múlva lesz 65 éves.
7.  Alakítsa át az életkort stringgé és fűzze hozzá egy mondathoz.

------------------------------------------------------------------------

## 2. feladat -- Listák

Adott egy lista, amely diákok pontszámait tartalmazza:

``` python
pontszamok = [56, 78, 45, 90, 62, 78, 100, 34]
```

Feladat:

1.  Írd ki a lista hosszát.
2.  Írd ki a legnagyobb és legkisebb pontszámot.
3.  Számítsd ki az átlagot.
4.  Számold meg, hány tanuló ért el legalább 60 pontot.
5.  Rendezd növekvő sorrendbe a listát.
6.  Távolítsd el a legkisebb elemet.
7.  Fűzz hozzá egy új pontszámot (88).

------------------------------------------------------------------------

## 3. feladat -- Kétdimenziós lista

Egy osztály három dolgozatának pontszámai:

``` python
eredmenyek = [
    [56, 78, 90],
    [45, 60, 75],
    [88, 92, 85],
    [70, 68, 72]
]
```

Feladat:

1.  Írd ki az első tanuló harmadik dolgozatának pontszámát.
2.  Számítsd ki minden tanuló összpontszámát.
3.  Számítsd ki az egyes dolgozatok átlagát.
4.  Keresd meg, melyik tanuló érte el a legnagyobb összpontszámot.
5.  Írd ki az összes pontszámot soronként.

------------------------------------------------------------------------

## 4. feladat -- Szótárak

Egy bolt termékeinek raktárkészlete:

``` python
raktar = {
    "alma": 120,
    "banan": 85,
    "narancs": 60,
    "korte": 45
}
```

Feladat:

1.  Írd ki az összes termék nevét.
2.  Írd ki az összes készletértéket.
3.  Add hozzá az "eper" terméket 30 darabbal.
4.  Növeld meg az alma készletét 20 darabbal.
5.  Számítsd ki az összes termék darabszámát.
6.  Töröld a "korte" terméket.
7.  Írd ki kulcs-érték páronként a teljes szótárt.

------------------------------------------------------------------------

## 5. feladat -- Halmazok

Adott két osztály tanulóinak névsora:

``` python
osztaly_a = ["Anna", "Béla", "Csaba", "Dóra", "Emma"]
osztaly_b = ["Csaba", "Emma", "Ferenc", "Gábor"]
```

Feladat:

1.  Alakítsd át a listákat halmazzá.
2.  Határozd meg, kik vannak mindkét osztályban (metszet).
3.  Határozd meg az összes egyedi tanulót (unió).
4.  Kik vannak csak az A osztályban?
5.  Hány különböző tanuló van összesen?
6.  Alakítsd vissza az uniót listává.
