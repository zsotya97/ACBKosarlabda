import datetime as dt
#Adatok beolvasása
class Adatok:
    def __init__(self,sor):
        split = sor.split(';')
        self.Hazai=split[0]
        self.Idegen=split[1]
        self.HazaiPont=int(split[2])
        self.IdegenPont=int(split[3])
        self.Helyszin = split[4]
        self.Idopont =dt.datetime.strptime(split[5], "%Y-%m-%d") 

#Beolvasás
with open("eredmenyek.csv","r") as Beolvas:
    fejlec = Beolvas.readline().strip()
    lista = [Adatok(x.strip()) for x in Beolvas]
    hazai = {}
    idegen = {}

#3. feladat:
for x in lista:
    if x.Hazai=="Real Madrid":
        hazai[x.Hazai]=hazai.get(x.Hazai,0)+1
    elif x.Idegen=="Real Madrid":
        idegen[x.Idegen]=idegen.get(x.Idegen,0)+1
print(f"3. feladat: Real Madrid: Hazai: {hazai['Real Madrid']}, Idegen: {idegen['Real Madrid']}")

#4. feladat:
volt = False
for x in lista:
    if x.HazaiPont == x.IdegenPont:
        volt=True
        break
print("4. feladat: Volt döntetlen?",end=" ")
dontetlen ="igen" if volt==True else "nem"
print(dontetlen)

#5. feladat:
print(f"5. feladat: Barcelonai csapat pontos neve: {[x.Hazai for x in lista if x.Hazai.__contains__('Barcelona')][0]}")

#6. feladat:
eredmenyek = {}
print("6. feladat")
for x in lista:
    if x.Idopont ==dt.datetime(2004,11,21):
        eredmenyek[x.Hazai]=eredmenyek.get(x.Hazai, [0+x.HazaiPont,0+x.IdegenPont])

for x, y in eredmenyek.items():
    print(f"\t{x}: ({y[0]}:{y[1]})")

#7. feladat:
print("7. feldatat:")
stadionok = {}
for x in lista:
    stadionok[x.Helyszin]=stadionok.get(x.Helyszin,0)+1
[print(f"\t{x}: {y}") for x,y in stadionok.items() if y>20]