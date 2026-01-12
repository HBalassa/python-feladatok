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
# „Figyelmeztetés! A/Az [erőforrás neve] fogyóban! Újratöltés szükséges!”.

# Majd oldjuk meg a következő feladatokat is:
# 1. Hány feladatot hajtottunk végre összesen?
# 2. Melyik feladatot választottad a leggyakrabban?
# 3. Mennyi volt az átlagos üzemanyag-fogyasztásod?