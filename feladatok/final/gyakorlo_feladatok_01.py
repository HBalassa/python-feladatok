# GYAKORLÁS 01
# 2025.01.12.

# Google Classroom, Dig. Kult. 11.A/MAT, 2024.10.05. gyakoló feladatok

###########################
# 1
###########################
# Egy hosszútávfutó vagy , aki hosszú futás közben óránként rögzíti a pulzusszámát.
# Az óránkénti pulzus adatok bpm-ben a 'pulzus_adatok' változóban vannak elmentve.

# Kérdések:
# 1. Mennyi volt az átlagos pulzusszámod a futás során?
# 2. Hányszor haladta meg a pulzusszámod a 150 bpm értéket?
# 3. Mekkora volt a legmagasabb pulzusszámod?
# 4. Esett a pulzusszámod bármelyik pillanatban 60 bpm alá?

pulzus_adatok = [138, 150, 158, 165, 160, 152, 145]

print('# 1')
pulzus_osszeg = 0
nagyobb_150 = 0
max_pulzus = -1
esett_60_ala = False

for pulzus in pulzus_adatok:
    pulzus_osszeg += pulzus

    if pulzus > 150:
        nagyobb_150 += 1

    if pulzus > max_pulzus:
        max_pulzus = pulzus

    if pulzus < 60:
        esett_60_ala = True

atlag_pulzus = pulzus_osszeg / len(pulzus_adatok)
print(f'Átlag pulzus: {atlag_pulzus} bpm')
print(f'150 bpm feletti pulzusok száma: {nagyobb_150}')
print(f'Legmagasabb pulzus: {max_pulzus} bpm')
if esett_60_ala:
    print('60 bpm alá esett a pulzus.')
else:
    print('Nem esett 60 bpm alá a pulzus.')



print()
###########################
# 2
###########################
# Egy pilóta vagy, aki egy kisrepülőgépet vezet, és 30 percenként rögzíti az előző 30 percben megtett távolságot.
# A félóránként megtett távolságokat a 'tavolsagok' változó tartalmazza. A távolságok km-ben vannak megadva!

# Kérdések
# 1. Mekkora az összes megtett távolságod?
# 2. Mekkora volt az átlagsebességed? (v_átlag [km/h] = s_össz [km] / t_össz [h])
# 3. Volt-e olyan 30 perces szakasz amelyben több mint 250 km-t tettél meg?
# 4. Mikor haladtál először kevesebb mint 300 km-t egy félórában?

tavolsagok = [320, 315, 310, 305, 298, 290, 285, 295, 305, 315, 330, 340, 355, 360, 345, 330, 310, 295, 280, 270]

print('#2')
ossz_tavolsag = 0
ossz_ido = len(tavolsagok) * 30 / 60
nagyobb_250 = False
elso_kisebb_300 = -1

for idx, tavolsag in enumerate(tavolsagok):
    ossz_tavolsag += tavolsag

    if tavolsag > 250:
        nagyobb_250 = True

    if tavolsag < 300 and elso_kisebb_300 == -1:
        elso_kisebb_300 = idx + 1

atlag_sebesseg = ossz_tavolsag / ossz_ido

print(f'Összes megtett távolság: {ossz_tavolsag} km')
print(f'Átlagsebesség: {atlag_sebesseg} km/h')
if nagyobb_250:
    print('Volt olyan szakasz, amiben 250 km-nél többett tett meg.')
else:
    print('Nem volt olyan szakasz, amiben 250 km-nél többett tett meg.')
print(f'Először a/az {elso_kisebb_300}. szakaszon haladt kevesebb mint 300 km-t.')



print()
###########################
# 3
###########################
# Egy szafarin veszel észt. Megfigyeled a vadon élő állatokat, és feljegyzed, hány állatot látsz óránként.
# A szafari hossza 5 óra, és óránként feljegyzed, hogy hány állatot látsz. Az óránként látott állatok számát az 'allatok' változó tartalmazza

# Kérdések:
# 1. Mennyi volt az óránként látott állatok átlagos száma?
# 2. Hányszor láttál 10-nél több állatot egy óra alatt?
# 3. Volt olyan óra, amikor egyáltalán nem láttál állatokat?
# 4. A program kérjen be egy állatszámot és ha ennél a számnál volt magasabb állatszám, akkor a program írja ki, hogy: "Tetszett a szafari".
#    Ellenkező esetben az "Unalmas" szó jelenjen meg.

allatok = [12, 18, 25, 20, 14]

print('#3')

ossz_allatok = 0
nagyobb_10 = 0
nincs_allat = False

bekert_allatok = int(input('Legalább mennyi állatot szeretnél látni egy órában? '))
volt_tobb_allat = False

for allat in allatok:
    ossz_allatok += allat

    if allat > 10:
        nagyobb_10 += 1

    if allat == 0:
        nincs_allat = True

    if bekert_allatok < allat:
        volt_tobb_allat = True

atlag_allatok = ossz_allatok / len(allatok)

print(f'Állatok áltag száma: {atlag_allatok} db')
print(f'10-nél több állat egy órában: {nagyobb_10} alkalommal volt.')

if nincs_allat:
    print('Valamikor nem volt állat.')
else:
    print('Minden órában voltak állatok.')

if volt_tobb_allat:
    print('Tetszett a szafari!')
else:
    print('Unalmas...')
