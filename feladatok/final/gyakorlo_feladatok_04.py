# GYAKORLÁS 04
# 2025.01.14.

###########################
# 1
# Google Classroom, Dig. Kult. 11.A/MAT, 2024.11.07. órai munka
###########################
# Partit rendezel az osztálytársaidnak. A feladatod az, hogy összállítsd a költségvetést,
# és hogy megtervezd, hogy mire költöd a pénzt. Ahhoz, hogy ezt könnyebben megcsináld, írsz egy programot!
# A program először is bekéri a felhasználótól a buli költségvetését!

# Az így meghatározott pénzt 4 féle dologra költheted:
#   1) Party sapkák (5 font),
#   2) Italok (természetesen alkoholmentes, 10 font),
#   3) dekoráció (5 font),
#   4) rágcsálnivalók (4 font).
# A program kérdezze meg a felhasználót, hogy mire szeretné költeni a pénzét, egészen addig, amíg el nem fogy a pénze.

# Majd oldd meg a következő feladatokat!
# 1. Túlköltekeztél? Ha igen, mennyivel?
# 2. Mutasd meg a vásárolt összeget minden kategóriában!
# 3. A teljes költség hány százalékát költötted a partysapkákra?
# 4. Az összes kategóriából vásároltál termékeket?

print('#1')
koltsegvetes = int(input('Kérem a buli költségvetését: '))

valasztasok = []

while koltsegvetes > 0:
    valasztas = int(input('Mire szeretnéd költeni a pénzed? \nVálassz az alábbiak közül! [Party sapka: 1 / Ital: 2 / Dekoráció: 3 / Rágcsálnivaló: 4]: '))

    if valasztas == 1 or valasztas == 3:
        koltsegvetes -= 5
    elif valasztas == 2:
        koltsegvetes -= 10
    elif valasztas == 4:
        koltsegvetes -= 4

    valasztasok.append(valasztas)

if valasztas < 0:
    print(f'Túlköltekeztél {koltsegvetes} fonttal.')

dbok = [0, 0, 0, 0]

for valasztas in valasztasok:
    if valasztas == 1:
        dbok[0] += 1
    elif valasztas == 2:
        dbok[1] += 1
    elif valasztas == 3:
        dbok[2] += 1
    elif valasztas == 4:
        dbok[3] += 1

osszegek = [
    dbok[0] * 5,
    dbok[1] * 10,
    dbok[2] * 5,
    dbok[3] * 4
]

for i, osszeg in enumerate(osszegek):
    print(f'A vásárolt összeg a/az {i+1}. termékből: {osszeg} font.')

partysapka_szazalek = osszegek[0] / sum(osszegek) * 100
print(f'A teljes költség {partysapka_szazalek}%-a ment party sapkára.')

if min(dbok) != 0:
    print('Az összes kategóriából vásároltál!')
else:
    print('Nem az összes kategóriából vásároltál!')



print()
###########################
# 2
# Google Classroom, Dig. Kult. 11.A/MAT, 2024.11.12. dolgozat "A"
###########################
# Egy könyvtárat vezetsz, és nyomon kell követned a könyvkölcsönzéseket. Minden könyvnek a kategóriája alapján kölcsönzési díja van.
# Állítsd be a költségvetést: Kérdezd meg a felhasználót, hogy mekkora költségvetéssel rendelkezik.

# A könyveknek négy kategóriája van, mindegyikhez kölcsönzési díj tartozik, ezek a következőek:
#   1) Szépirodalom: 3 dollár könyvenként
#   2) Nem szépirodalom: 5 dollár könyvenként
#   3) Gyermekkönyvek: 2 dollár könyvenként
#   4) Képregény: 1 dollár könyvenként
# A program kérdezze meg a felhasználót hogy milyen kategóriát szeretne kölcsözöni, egészen addig,
# amíg el nem fogy a keret, vagy el nem éri a 10 könyvet.
# Minden egyes alkalommal, amikor kiválaszt egy kategóriát, vond le a megfelelő összeget a költségvetéséből.

# Ezután oldd meg az alábbi feladatokat!
# 1. A felhasználó megpróbált a költségvetésén felül kölcsönözni? Ha igen, mennyivel?
# 2. Mutasd meg, hogy az egyes kategóriákból hány könyvet kölcsönöztek ki.
# 3. Számítsd ki, hogy a teljes költségvetés hány százalékát költötték szépirodalmi könyvekre.
# 4. Az összes kategóriából kölcsönzött a felhasználó?

print('#2')
koltsegvetes = int(input('Add meg a költségvetésed: '))
konyvek_db = 0
konyvek = []

print('Milyen kategóriájú könyvet szeretnél kölcsönözni?')
while koltsegvetes > 0 and konyvek_db < 10:
    valasztas = int(input('Kérem válassz az alábbiak közül! [Szépirodalom: 1 / Nem szépirodalom: 2 / Gyermekkönyvek: 3 / Képregény: 4] '))
    konyvek_db += 1
    konyvek.append(valasztas)

    if valasztas == 1:
        koltsegvetes -= 3
    elif valasztas == 2:
        koltsegvetes -= 5
    elif valasztas == 3:
        koltsegvetes -= 2
    elif valasztas == 4:
        koltsegvetes -= 1

if koltsegvetes < 0:
    print(f'Túlöltekeztél {koltsegvetes} dollárral!')

dbok = [0,0,0,0]

for konyv in konyvek:
    if konyv == 1:
        dbok[0] += 1
    elif konyv == 2:
        dbok[1] += 1
    elif konyv == 3:
        dbok[2] += 1
    elif konyv == 4:
        dbok[3] += 1

kategoriak = ['szépirodalom', 'nem szépirodalom', 'gyermekkönyv', 'képregény']

for i, db in enumerate(dbok):
    print(f'A kölcsönzések száma a "{kategoriak[i]}" kategóriából: {db}')

osszegek = [
    dbok[0] * 3,
    dbok[1] * 5,
    dbok[2] * 2,
    dbok[3] * 1,
]

szepirodalmi_szazalek = osszegek[0] / sum(osszegek) * 100

print(f'A teljes költségvetés {szepirodalmi_szazalek}%-a ment szépirodalmi könyvekre.')

if min(dbok) == 0:
    print('Nem kölcsönzött minden kategóriából!')
else:
    print('Kölcsönzött minden kategóriából!')



print()
###########################
# 3
# Google Classroom, Dig. Kult. 11.A/MAT, 2024.11.12. dolgozat "B"
###########################
# Egy programot készítesz a kockadobások nyomon követésére.
# A programnak először meg kell kérdeznie a felhasználót, hogy hányszor akar kockával dobni.
# Ezután kérje a felhasználót, hogy adja meg az egyes dobások értékét.
# A program csak 1 és 6 közötti értékeket fogadjon el; minden ezen a tartományon kívüli dobást 0-nak kell számolni.

# Feladatok:
# 1. Több páros vagy páratlan számot dobott a felhasználó (a 0-kat nem számítva)?
# 2. Mennyi volt a dobások átlagértéke?
# 3. Az összes dobás hány százalékát tették ki az egyes számok (1-től 6-ig)?
# 4. Hány dobás után dobott a felhasználó először 3-ast?
# 5. Hány gurítás után érte el az összeg a 10-et?

print('#3')
dobasok_db = int(input('Mennyiszer akarsz dobni? '))
dobasok = []

for i in range(dobasok_db):
    dobas = int(input(f'Kérlek add meg a/az {i+1}. dobás értékét: '))
    if dobas > 6 or dobas < 1:
        dobas = 0
    dobasok.append(dobas)

paros_db = 0
paratlan_db = 0
ossz_jo_dobasok = 0
len_jo_dobasok = 0
dbok = [0,0,0,0,0,0]

for dobas in dobasok:
    if dobas != 0:
        # páros-páratlan
        if dobas % 2 == 0:
            paros_db += 1
        else:
            paratlan_db += 1

        # átlag
        ossz_jo_dobasok += dobas
        len_jo_dobasok += 1

        # dobások számai
        if dobas == 1:
            dbok[0] += 1
        elif dobas == 2:
            dbok[1] += 1
        elif dobas == 3:
            dbok[2] += 1
        elif dobas == 4:
            dbok[3] += 1
        elif dobas == 5:
            dbok[4] += 1
        elif dobas == 6:
            dbok[5] += 1


if paros_db > paratlan_db:
    print('Több páros dobás volt.')
elif paratlan_db > paros_db:
    print('Több páratlan dobás volt.')
else:
    print('Ugyanannyi páros és páratlan dobás volt.')

atlag_dobas = ossz_jo_dobasok / len_jo_dobasok;
print(f'Az átlagos dobásszám: {atlag_dobas}')

szazalekok = [
    dbok[0] / len_jo_dobasok * 100,
    dbok[1] / len_jo_dobasok * 100,
    dbok[2] / len_jo_dobasok * 100,
    dbok[3] / len_jo_dobasok * 100,
    dbok[4] / len_jo_dobasok * 100,
    dbok[5] / len_jo_dobasok * 100,
]

for i, szazalek in enumerate(szazalekok):
    print(f'Az összes dobás {szazalek}%-a volt {i+1}.')

for i, dobas in enumerate(dobasok):
    if dobas == 3:
        print(f'{i+1} dobás után dobott először 3-ast.')
        break

osszeg = 0
for i, dobas in enumerate(dobasok):
    osszeg += dobas
    if osszeg >= 10:
        print(f'{i+1} dobás után érte el a dobások összege a 10-et.')
        break



print()
###########################
# 4
# Google Classroom, Dig. Kult. 11.A/MAT, 2024.11.12. dolgozat "C"
###########################
# A nap folyamán nyomon követed a vízfogyasztásod.
# A programnak minden alkalommal meg kell adnia az általad megivott vízmennyiséget ml-ben,
# amíg a teljes vízmennyiség el nem éri a legalább 3000 ml-t.

# Feladatok:
# 1. Számítsd ki a bevitelenként átlagosan elfogyasztott vízmennyiséget.
# 2. Tegyük fel, hogy valamikor megittál egy nagy palack vizet, ami a legmagasabb vízbevitel a nap folyamán.
#    Hány millilitert tartalmazott ez a palack?
# 3. Mikor fogyasztottál először 700 ml-nél többet egy alkalommal? Mekkora volt az elfogyasztott mennyiség?
# 4. Hány bejegyzés után érte el a teljes vízfogyasztásod az 1500 ml-t?
# 5. Kis italnak számít minden 250 ml alatti, nagy italnak minden 500 ml feletti ital.
#    Milyen típusú italból ivott a felhasználó a több alkalommal?

print('#4')
megivott_viz = 0
vizmennyisegek = []

while megivott_viz < 3000:
    vizmennyiseg = int(input('Adj meg egy vízmennyiséget ml-ben: '))
    megivott_viz += vizmennyiseg
    vizmennyisegek.append(vizmennyiseg)

atlag_viz = sum(vizmennyisegek) / len(vizmennyisegek)
print(f'Az átlagosan bevitt víz: {atlag_viz} ml')

max_viz = max(vizmennyisegek)
print(f'A maximálisan bevitt víz: {max_viz} ml')

for i, vizmennyiseg in enumerate(vizmennyisegek):
    if vizmennyiseg >= 700:
        print(f'Először {i+1}. alkalommal volt nagyobb a bevitt víz mint 700 ml. Pontosan: {vizmennyiseg} ml.')
        break

osszeg = 0
for i, vizmennyiseg in enumerate(vizmennyisegek):
    osszeg += vizmennyiseg
    if osszeg >= 1500:
        print(f'{i+1} bejegyzés után érte el az 1500 ml-t.')
        break

kis_ital_db = 0
nagy_ital_db = 0
for vizmennyiseg in vizmennyisegek:
    if vizmennyiseg < 250:
        kis_ital_db += 1
    elif vizmennyiseg > 500:
        nagy_ital_db += 1

if kis_ital_db > nagy_ital_db:
    print('Kis italból többet ivott.')
elif kis_ital_db < nagy_ital_db:
    print('Nagy italból többet ivott.')
else:
    print('Ugyanannyit ivott kis és nagy italból is.')