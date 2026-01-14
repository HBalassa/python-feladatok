# GYAKORLÁS 01
# 2025.01.14.

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

pulzus_adatok = [138, 50, 158, 165, 160, 152, 145]

print('#1')

# Összeadjuk a pulzus_adatok pulzusait, majd elosztjuk annyival amennyi adat van.
ossz_pulzus = sum(pulzus_adatok)        # sum() -> összeadja a lista elemeit
pulzusok_szama = len(pulzus_adatok)     # len() -> megadja a lista hosszát (mennyi elem van benne)

atlag_pulzus = ossz_pulzus / pulzusok_szama
print(f'Az átlag pulzus: {atlag_pulzus} bpm')   # f'' -> ilyenkor {} lehet változókat írni

# range(a, b, c)    -> a: honnan (beletartozik) [opcioinális, alap: 0]; b: hová (nem tartozik bele) [kötelező]; c: milyen lépéssel [opcinális, alap: 1]
# range(0, 10, 2)   -> [0,10[ 2-esével: 0, 2, 4, 6, 8
# range(20)         -> [0, 20[ 1-esével: 0,1,2...18,19
# range(5, 10)      -> [5, 10[ 1-esével: 5,6,7,8,9

# lista 1. eleme az 0. indexű elemet jelöl!!! (PYTHON 0-s indexelésű)

# for i in range(7):
#     # ilyenkor az i változó végigmegy 0...6 között
#     print(i)

db = 0
for pulzus_adat in pulzus_adatok:
    # ilyenkor a pulzus_adat változóba belekerül a pulzus_adatok lista egyes elemei
    # végigmegy a listán egyesével az egyes elemeken

    if pulzus_adat > 150:
        db += 1

print(f'{db}x haladta meg a pulzusszám a 150 bpm értéket.')

legnagyobb_pulzus = max(pulzus_adatok)      # max() -> megadja a legnagyobb elemét a listának
print(f'{legnagyobb_pulzus} a legmagasabb pulzusszám.')

# volt_60_alatt = False
# for pulzus_adat in pulzus_adatok:
#     if pulzus_adat < 60:
#         volt_60_alatt = True
#         break
#
# if volt_60_alatt:
#     print('A pulzus számod esett 60 bpm alá.')
# else:
#     print('A pulzus számod nem esett 60 bpm alá.')

# Másik féle megoldás
legkisebb_adat = min(pulzus_adatok)

if legkisebb_adat > 60:
    print('A pulzus számod nem esett 60 bpm alá.')
else:
    print('A pulzus számod esett 60 bpm alá.')




###########################
# 2
###########################
# Egy pilóta vagy, aki egy kisrepülőgépet vezet, és 30 percenként rögzíti az előző 30 percben megtett távolságot.
# A félóránként megtett távolságokat a 'tavolsagok' változó tartalmazza.

# Kérdések
# 1. Mekkora az összes megtett távolságod?
# 2. Mekkora volt az átlagsebességed? (v_átlag [km/h] = s_össz [km] / t_össz [h])
# 3. Volt-e olyan 30 perces szakasz amelyben több mint 250 km-t tettél meg?
# 4. Mikor haladtál először kevesebb mint 300 km-t egy félórában?

tavolsagok = [320, 315, 310, 305, 298, 290, 285, 295, 305, 315, 330, 340, 355, 360, 345, 330, 310, 295, 280, 270]




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