# GYAKORLÁS 03
# 2025.01.12.

###########################
# 1
# Google Classroom, Dig. Kult. 11.A/MAT, 2024.10.17. órai munka
###########################
# Egy hőmérsékletösszesítő szoftver fejlesztője vagy.

# A program a következő feladatokat oldja meg.
# 1. Kérj be a felhasználótól 5 hőmérsékletet (celsiusban) és tárold el egy listában.
# 2. Mekkora  volt a hőingadozás? (maximális és minimális hőmérsékletek különbsége)
# 3. Hány adat volt az átlaghőmérséklet alatt?
# 4. Írd ki az összes értéket fahreinheitben!  F = (C × 9/5) + 32
# 5. Fagyott-e?
# 6. Melyik volt az első 10 C feletti a hőmérséklet?

print('#1')
homersekletek = []
for i in range(5):
    homersekletek.append(int(input(f'Kérem a/az {i+1}. hőmérsékletet Celsiusban! ')))

max_homerseklet = max(homersekletek)
min_homerseklet = min(homersekletek)

hoingas = max_homerseklet - min_homerseklet

atlag_homerseklet = sum(homersekletek) / len(homersekletek)
atlag_alatt = 0
homerseklet_F = []
fagyott_e = False
elso_10_felett = -1

for i, homerseklet in enumerate(homersekletek):
    if homerseklet < atlag_homerseklet:
        atlag_alatt += 1

    homerseklet_F.append((homerseklet * 9/5) + 32)

    if homerseklet <= 0:
        fagyott_e = True

    if homerseklet > 10 and elso_10_felett == -1:
        elso_10_felett = i + 1

print(f'A hőingás nagysága: {hoingas} C')
print(f'Átlagghőmérséklet alatti adatok száma: {atlag_alatt} db')
print(f'A hőmérsékletek fahrenheitben: {homerseklet_F}')
if fagyott_e:
    print('Fagyott.')
else:
    print('Nem fagyott.')
print(f'Az első 10 C feletti hőmérséklet: {elso_10_felett}. adat.')



print()
###########################
# 2
# Google Classroom, Dig. Kult. 11.A/MAT, 2024.10.22. órai munka
###########################
# Egy nap jegyzed az ételfogyasztásod, és írsz erre egy programot.

# 1. A program addig kérje be a kalóriamennyiségeket, amíg az összmennyiség el nem éri a 2000 kalóriát.
# 2. Mennyi volt az átlagos kalóriafogyasztásod?
# 3. Ma ettél egy Big Mac-et, a nap legmagasabb kalóriatartalmú tételét.  Hány kalóriát tartalmazott?
# 4. Mikor fogyasztottál először 500 kalóriánál többet egyetlen étkezés során? Mekkora volt az elfogyasztott mennyiség?
# 5. Hány étkezés után érted el az 1000 összkalóriát?

print('#2')
ossz_kaloria = 0
kaloriak = []

while ossz_kaloria < 2000:
    bekert_kaloria = int(input('Kérek egy kalóriamennyiséget! '))
    ossz_kaloria += bekert_kaloria
    kaloriak.append(bekert_kaloria)

atlag_kaloria = sum(kaloriak) / len(kaloriak)
max_kaloria = max(kaloriak)
elso_tobb_500_idx = -1
eddigi_kaloria = 0
eler_1000 = -1

for i, kaloria in enumerate(kaloriak):
    if kaloria > 500 and elso_tobb_500_idx == -1:
        elso_tobb_500_idx = i + 1
        elso_tobb_500_kaloria = kaloria

    eddigi_kaloria += kaloria
    if eddigi_kaloria >= 1000 and eler_1000 == -1:
        eler_1000 = i + 1

print(f'Átlagos kalória: {atlag_kaloria}')
print(f'A Big Mac kalóriája: {max_kaloria}')
print(f'Először a/az {elso_tobb_500_idx}. étkezésnél evett 500 kalóránál többet, pontosan {elso_tobb_500_kaloria} kalóriát.')
print(f'Az 1000 összkalóriát {eler_1000} étkezés alatt érte el.')



print()
###########################
# 3
# Google Classroom, Dig. Kult. 11.A/MAT, 2024.10.24. órai munka
###########################
# Egy Föld körüli pályán keringő űrállomásnak te vagy a kapitánya.
# Keringésed alatt három erőforrással kell számolnod: üzemanyag, oxigén és energia.
# Az állomáson 3 feladat elvégzésére van lehetőséged:
#   1. Űrséta: Ennek végrehajtása 5 üzemanyagot, 50 oxigént és 40 energiát fogyaszt.
#   2. Karbantartás: Ennek végrehajtása 0 üzemanyagot, 20 oxigént és 20 energiát fogyaszt.
#   3. Turbó: Ennek végrehajtása 50 üzemanyagot, 10 oxigént és 5 energiát fogyaszt.
# Kezdetben 200 egység üzemanyaggal, 250 egység oxigénnel és 225 egység energiával indulsz.

# Az állomás számítógépe minden órában megkérdezi, hogy milyen feladatot szeretnél végrehajtani.
# Ha valamelyik erőforrás nulla alá csökken, a program hagyja abba a kérdések feltevését és közölje velünk:
# „Figyelmeztetés! Az [erőforrás neve] fogyóban! Újratöltés szükséges!”.

# Majd oldjuk meg a következő feladatokat is:
# 1. Hány feladatot hajtottunk végre összesen?
# 2. Melyik feladatot választottad a leggyakrabban?
# 3. Mennyi volt az átlagos üzemanyag-fogyasztásod?

print('#3')
uzemanyag = 200
oxigen = 250
energia = 225
feladatok = []

while uzemanyag > 0 and oxigen > 0 and energia > 0:
    bekert_feladat = int(input('Milyen feladatot szeretnél végrehajtani? [űrséta: 1 / karbantartás: 2 / turbó: 3] '))
    feladatok.append(bekert_feladat)

    if bekert_feladat == 1:
        uzemanyag -= 5
        oxigen -= 50
        energia -= 40
    elif bekert_feladat == 2:
        oxigen -= 20
        energia -= 20
    elif bekert_feladat == 3:
        uzemanyag -= 50
        oxigen -= 10
        energia -= 5

    elfogyott = []
    if uzemanyag <= 0:
        elfogyott.append('üzemanyag')

    if oxigen <= 0:
        elfogyott.append('oxigén')

    if energia <= 0:
        elfogyott.append('energia')

    if len(elfogyott) != 0:
        print(f'Figyelmeztetés! Az {elfogyott} fogyóban! Újratöltés szükséges!')

ossz_feladat = len(feladatok)
max_feladat_idx = max(feladatok)
if max_feladat_idx == 1:
    max_feladat = 'űrséta'
elif max_feladat_idx == 2:
    max_feladat = 'karbantartás'
elif max_feladat_idx == 3:
    max_feladat = 'turbó'

ossz_uzemanyag_fogyasztas = 0

for feladat in feladatok:
    if feladat == 1:
        ossz_uzemanyag_fogyasztas += 5
    elif feladat == 2:
        ossz_uzemanyag_fogyasztas += 0
    elif feladat == 3:
        ossz_uzemanyag_fogyasztas += 50

atlag_uzemanyag_fogyasztas = ossz_uzemanyag_fogyasztas / len(feladatok)

print(f'Összes feladat: {ossz_feladat} db')
print(f'Legyakrabb feladat: {max_feladat}')
print(f'Átlagos üzemanyag fogyasztás: {atlag_uzemanyag_fogyasztas}')