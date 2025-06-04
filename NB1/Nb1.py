"""
focilst=[]
class Foci:
    def __init__(self,vnev,csnev,rszam,ehely,mhely,hhely,bajn):
        self.vnev=vnev
        self.csnev=csnev
        self.rszam=int(rszam)
        self.ehely=int(ehely)
        self.mhely=int(mhely)
        self.hhely=int(hhely)
        self.bajn=bajn=="True"

    def bajnok(self):
        return "Igen" if self.bajn else "Nem"

    def __repr__(self):
        return f"A versenyző neve:({self.vnev}), csapata:({self.csnev}), rajtszáma:({self.rszam}), helyezései: első:({self.ehely}), második:({self.mhely}), harmadik:({self.hhely}), volt-e bajnok:({self.bajnok()})."

file=open("NB1.txt", encoding="utf-8")
for sor in file:
    adat=sor.strip().split()
    f1=Foci(*adat)
    focilst.append(f1)

for i in focilst:
    print(i)
print("----------------------------")

#1. Határozza meg és írja ki a képernyőre, hogy hány versenyző van!
print("Hány versenyző van?")
print(len(focilst),"versenyző van.")
print("----------------------------")

#2. Határozza meg és írja ki a képernyőre, hogy van-e olyan versenyző akinek a neve VargaBarni! Írja ki azt is, ha nincs ilyen!
print("Van olyan versenyző akinek a neve VargaBarni?")
van=False
for i in focilst:
    if i.vnev=="VargaBarni":
        van=True
if van:
    print("Van.")
else:
    print("Nincs.")
print("----------------------------")

#3. Határozza meg, hogy hány bajnok van!
print("Hány bajnok van?")
bajnokok=0
nbajnokok=[]
for i in focilst:
    if i.bajn:
        bajnokok+=1
        nbajnokok.append(i.vnev)
print(f"{bajnokok} versenyző van: {', '.join(nbajnokok)}")
print("----------------------------")

#4. Kérjen be a felhasználótól egy számot! Írja ki a rajtszámnak megfelelő versenyző nevét és csapatának nevét!
print("Rajtszámnak megfelelő versenyző neve és csapatának neve.")
a=int(input("Versenyző rajtszáma: "))
for i in focilst:
    if a==i.rszam:
        print(f"A versenyző neve: {i.vnev}, csapata: {i.csnev}.")
"""


#1. Határozza meg és írja ki a képernyőre, hogy hány versenyző van!
print("Hány versenyző van?")

print("----------------------------")

#2. Határozza meg és írja ki a képernyőre, hogy van-e olyan versenyző akinek a neve VargaBarni! Írja ki azt is, ha nincs ilyen!
print("Van olyan versenyző akinek a neve VargaBarni?")

print("----------------------------")

#3. Határozza meg, hogy hány bajnok van!
print("Hány bajnok van?")

print("----------------------------")

#4. Kérjen be a felhasználótól egy számot! Írja ki a rajtszámnak megfelelő versenyző nevét és csapatának nevét!
print("Rajtszámnak megfelelő versenyző neve és csapatának neve.")










