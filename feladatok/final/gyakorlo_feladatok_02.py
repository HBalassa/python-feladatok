# GYAKORLÁS 02
# 2025.01.12.

###########################
# 1
# Google Classroom, Dig. Kult. 11.A/MAT, 2024.10.08. órai munka
###########################
# Pityu zöldségeshez megy. Egy programba jegyzi bevásárlásának adatait.

# A progmram:
# 1. Kérje be hogy hány zöldséget/gyümölcsöt szeretne venni Pityu.
# 2. Kérjen be és tároljon el annyi zöldséget/gyümölcsöt, amennyit Pityu megadott.
# 3. Mondja meg hány alma van a listában?
# 4. Kérjen be a felhasználótól egy zöldséget/gyümölcsöt és mondja meg, hogy szerepel-e a listában!

print('#1')
bekert_szam = int(input('Mennyi zöldséget/gyümölcsöt szeretnél venni? '))
etelek = []

for i in range(bekert_szam):
    etelek.append(input('Kérek egy zöldséget/gyümölcsöt! '))

bekert_etel = input('Melyik zöldségre/gyümölcsere vagy kiváncsi? ')
benne_van = False

almak_szama = 0
for etel in etelek:
    if etel == 'alma':
        almak_szama += 1

    if bekert_etel == etel:
        benne_van = True

if benne_van:
    print(f'A listában szerepel a/az {bekert_etel}.')
else:
    print(f'A listában nem szerepel a/az {bekert_etel}.')

print(f'A listában {almak_szama} db alma van.')



print()
###########################
# 2
# Google Classroom, Dig. Kult. 11.A/MAT, 2024.10.10. órai munka
###########################
# Egy programot készítünk, ami bekéri 8 db városnak a távolságát Budapesttől (km-ben).
# A bekért adatokat egy változóban (lista) tároljuk el, majd oldjuk meg a feladatokat:

# 1. Mennyi km-t kellene megtennünk, ha Budapestből indulva minden városba el szeretnénk menni,
#    majd Budapestre akarunk visszatérni? (Minden városba csak Bp-ből vezet egy út oda-vissza; a városok között nincsenek utak)
# 2. Átlagosan mennyire messze van tőlünk egy város?
# 3. Mennyire messze van tőlünk a legközelebbi illetve a legtávolabbi város?
# 4. Hány város van távolabb tőlünk 20 km-nél?

print('#2')

bekert_tavolsagok = []
for i in range(8):
    bekert_tavolsagok.append(int(input(f'Adja meg a/az {i+1}. város távolságát Budapesttől! ')))

megtett_tavolsag = 0
ossz_tavolsag = 0
max_tavolsag = -1
min_tavolsag = 9999
tavolabb_20km = 0

for tavolsag in bekert_tavolsagok:
    megtett_tavolsag += tavolsag * 2

    ossz_tavolsag += tavolsag

    if tavolsag > max_tavolsag:
        max_tavolsag = tavolsag
    if tavolsag < min_tavolsag:
        min_tavolsag = tavolsag

    if tavolsag > 20:
        tavolabb_20km += 1

atlag_tavolsag = ossz_tavolsag / len(bekert_tavolsagok)

print(f'Az összes megtett km: {megtett_tavolsag}')
print(f'Átlagos távolság: {atlag_tavolsag} km')
print(f'Legközelebbi város: {min_tavolsag} km; legtávolabbi város: {max_tavolsag} km')
print(f'20 km-nél távolabbi városok: {tavolabb_20km} db')



print()
###########################
# 3
# Google Classroom, Dig. Kult. 11.A/MAT, 2024.10.15. órai munka
###########################
# Játékfejlesztő vagy, aki egy RPG-n (szerepjátékon) dolgozik.  Feladatod a tapasztalati pontok (XP) és szintek (LVL) nyomonkövetése.

# Ehhez mindenekelőtt szükséged van egy programra, amely eltárolja a küldetések során megszerzett tapasztalati pontokat (XP).
# A program először bekéri a felhasználótól, hogy mennyi küldetést teljesített. Majd ennek ismeretében, bekéri hogy az egyes küldetések
# alatt mennyi XP-t sikerült elérnie a játékosnak.
# A megszerzett XP pontokat egy listában tároldd el!

# Ezután oldd meg az alábbi feladatokat:
# 1. Mennyi XP-t szerzett összesen a játékos?
# 2. Hány szintet ért el a játékos? (A szintlépés 100 XP-ként történik meg.)
# 3. Mennyi XP hiányzik a következő szint eléréséhez?
# 4. Hány küldetésnél szerzett több mint 50 XP-t?
# 5. Elérte-e a max szintet? (A maximum szint az 50-es)
# 6. Mennyi volt az egy küldetésből szerzett legmagasabb és legalacsonyabb XP?
# 7. Melyik volt az első küldetés ahol 80 XP-nél többet szerzett?

print('#3')
kuldetesek_szama = int(input('Mennyi küldetést teljesítettél? '))
tapasztalatok = []

for i in range(kuldetesek_szama):
    tapasztalatok.append(int(input(f'A/Az {i+1}. küldetés során szerzett tapasztalat: ')))

ossz_tapasztalat = sum(tapasztalatok)
elert_szint = int(ossz_tapasztalat / 100)
hianyzo_tapasztalat = 100 - (ossz_tapasztalat - elert_szint * 100)

tobb_50 = 0
max_tapasztalat = -1
min_tapasztalat = 9999
elso_tobb_80 = -1

for i, tapasztalat in enumerate(tapasztalatok):
    if tapasztalat > 50:
        tobb_50 += 1

    max_tapasztalat = max(tapasztalat, max_tapasztalat)
    min_tapasztalat = min(tapasztalat, min_tapasztalat)

    if tapasztalat > 80 and elso_tobb_80 == -1:
        elso_tobb_80 = i + 1

print(f'Összes XP: {ossz_tapasztalat}')
print(f'Elért szint: {elert_szint}')
print(f'Hiányzó XP a következő szintig: {hianyzo_tapasztalat}')
print(f'Több mint 50 XP {tobb_50} alkalommal volt.')
if elert_szint >= 50:
    print('Elérte a maximális szintet!')
else:
    print('Nem érte el a maximális szintet...')
print(f'Legtöbb XP: {max_tapasztalat}; legkevesebb XP: {min_tapasztalat}')
print(f'A/Az {elso_tobb_80}. küldetés volt, ahol először több mint 80 XP-t szerzett.')
