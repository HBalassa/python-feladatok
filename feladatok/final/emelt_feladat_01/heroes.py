###############################################################################################
# EMELT FELADAT 01
# 2025.02.16.
# Google Classroom, Digitális Kultúra Fakultáció 2024-25,  2024.09.03. programozási feladat 1
###############################################################################################

# A heroes.txt egy videojátékhőseiről tartalmaz adatokat. Egy sora a fájlnak a következő felépítésű: név, szerep,
# szint, életerő(hp). Ezek az adatok a soron belül szóközökkel vannak elválasztva. A szöveges fájl beolvasásával oldd
# meg a következő feladatokat:

# 1. Mennyi hős adatait tartalmazza a fájl?
# 2. Kérd be egy hős nevét, majd jelenítsd meg a hozzátartozó adatokat!
# 3. Ki a legnagyobb szintű hős? (Megj.: ha több van, elég egyet megjeleníteni!)
# 4. Mennyi 11-es szintű hős szerepel a fájlban?
# 5. Szerepenként melyik hősnek van a legnagyobb életereje?
# 6. Melyik szerephez tarotozik a legtöbb hős?
# 7. Szintenként mennyi az áltag életerő? (Megj.: Ügyelj arra, hogy csak olyan szintek jelenjenek meg, amelyek
#    szerepelnek a fájlban!)
# 8. Írd ki a "warriors.txt" fájlba az összes Warrior szerepű hős nevét és szintjét szint szerint növekvő sorrendben!


# # File beolvasása
# heroes = []
# with open("heroes.txt", "r") as f:
#     for sor in f:
#         heroes.append(sor.strip().split(' '))
#
# # Hősök száma
# num_heroes = len(heroes)
# print(f'A file {num_heroes} db hős adatait tartalmazza.')
#
# #



# A megoldás OOP módszerrel

class Hero:
    def __init__(self, name: str = "", role: str = "", level: int = 0, life: int = 0):
        self.name = name
        self.role = role
        self.level = level
        self.life = life

    @staticmethod
    def file_beolvas() -> list["Hero"]:
        heroes = []
        with open("heroes.txt", "r") as f:
            for sor in f:
                sor_elemek = sor.strip().split(' ')
                hero = Hero()
                hero.name = sor_elemek[0]
                hero.role = sor_elemek[1]
                hero.level = sor_elemek[2]
                hero.life = sor_elemek[3]

                heroes.append(hero)

        return heroes

    @staticmethod
    def hosok_szama(heroes: list["Hero"]):
        print(f'A fájl ${len(heroes)} db hős adatait tartalmazza.')

    @staticmethod
    def hos_adatai(heroes: list["Hero"]):
        hos_neve = input('Kérem egy hősnek a nevét! ')

        for hero in heroes:
            if hos_neve == hero.name:
                print(f'A hős adatai: név: {hero.name}, szerep: {hero.role}, szint: {hero.level}, életerő: {hero.life}')
                break
        else:
            print('Nincs ilyen nevű hős a listában.')

    @staticmethod
    def legnagyobb_szintu_hos(heroes: list["Hero"]):
        max_szint = -1
        max_idx = -1
        for i, hero in enumerate(heroes):
            if hero.level > max_szint:
                max_szint = hero.level
                max_idx = i

        print(f'A legnagyobb szintű hős adatai: név: {heroes[max_idx].name}, szerep: {heroes[max_idx].role}, szint: {heroes[max_idx].level}, életerő: {heroes[max_idx].life}')

    @staticmethod
    def hosok_11_szinttel(heroes: list["Hero"]):
        num_11 = 0
        for hero in heroes:
            if hero.level == 11:
                num_11 += 1
        print(f'11-es szintű hősök száma: {num_11} db.')

    @staticmethod
    def szerepenkent_legnagyobb_elet(heroes: list["Hero"]):
        szerepek = {}

        for hero in heroes:
            if hero.role not in szerepek:
                szerepek[hero.role] = [hero.name, hero.life]
            else:
                if hero.life > szerepek[hero.role][1]:
                    szerepek[hero.role] = [hero.name, hero.level]

        print('A legnagyobb életű hősök nevei szerepenként:')
        for szerep, [nev, elet] in szerepek.items():
            print(f'{szerep}: {nev}, {elet} életerő.')

    @staticmethod
    def szerep_legtobb_hossel(heroes: list["Hero"]):
        szerepek = {}

        for hero in heroes:
            if hero.role not in szerepek:
                szerepek[hero.role] = 1
            else:
                szerepek[hero.role] += 1

        max_szam = max(szerepek.values())

        for szerep, szam in szerepek.items():
            if szam == max_szam:
                print(f'A legtöbb hőssel rendelkező szerep: {szerep}')
                break
