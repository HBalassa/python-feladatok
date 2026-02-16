# Képzelj el egy erdőt, amely különböző fákat tartalmaz. Az alábbi fák szerepelnek az erdőben:
# "tölgy", "nyár", "fenyő", "hárs", "tölgy", "akác", "nyár", "fenyő", "hárs", "akác", "szilva", "tölgy", "nyár"

# 1. Tárold el a fákat egy megfelelő adatszerkezetben!
# 2. Írd ki a hány fa található az erdőben!
# 3. Kérd be a felhasználótól egy fának a nevét! Ez a fa szerepel a listában? Ha igen hanyadik helyen található az első ilyen fa?
# 4. Melyik fa szerepel a legtöbbször a listában?
# 5. Szeretnénk egy új fajta fát ültetni az erdőbe. Ehhez a program addig kérje be egy fának a nevét ameddig az nem szerepel az ültetett fák között.

fak = ["tölgy", "nyár", "fenyő", "hárs", "tölgy", "akác", "nyár", "fenyő", "hárs", "akác", "szilva", "tölgy", "nyár"]

osszes_fa = len(fak)
print(f'Ennyi fa található az erdőben: {osszes_fa}.')

fa_nev = input('Adj meg egy fának a nevét! ')

benne_van = False

for i, fa in enumerate(fak):
    if fa == fa_nev:
        benne_van = True
        break

if benne_van == True:
    print(f'{i+1}. helyen van az adott fa.')
else:
    print('Nincs ilyen adott fa.')

legtobb_ertek = 0
legtobb_fa_neve = ""

for fa in fak:
    szamolas = fak.count(fa)
    if szamolas > legtobb_ertek:
        legtobb_ertek = szamolas
        legtobb_fa_neve = fa

print(f"A {legtobb_fa_neve} szerepelt a legtöbbször.")


uj_fa = input("Adj meg egy fa nevet! ")

while (uj_fa in fak) == True:
    uj_fa = input("Adj meg egy fa nevet! ")

fak.append(uj_fa)
