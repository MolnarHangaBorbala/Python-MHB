#1. Olvassa be a játékosok adatait a fájlból, és tárolja őket egy Jatekos osztály segítségével!
jateklst=[]
class Jatekos:
    def __init__(self,nev,csapat,mezsz,golsz,golpa,sarga,piros,valo):
        self.nev=nev
        self.csapat=csapat
        self.mezsz=int(mezsz)
        self.golsz=int(golsz)
        self.golpa=int(golpa)
        self.sarga=int(sarga)
        self.piros=int(piros)
        self.valo=valo=="True"

    def valogatott(self):
        return "Igen" if self.valo else "Nem"

    def __repr__(self):
        return f"A játékos neve: ({self.nev}),csapata: ({self.csapat}),mezszáma: ({self.mezsz}),gólszáma: ({self.golsz}),gólpassza: ({self.golpa}),sárga: ({self.sarga}),piros: ({self.piros}),válogatott: ({self.valogatott()})"

file=open("jatekosok.txt", encoding="utf-8")
for sor in file:
    adat=sor.strip().split()
    j1=Jatekos(*adat)
    jateklst.append(j1)

#2. Írja ki, hogy hány játékos szerepel az állományban!
print("Hány játékos szerepel az állományban?")
print(len(jateklst),"játékos szerepel az állomáyban")
print("--------------------------------------------")

#3. Vizsgálja meg, hogy van-e olyan játékos, akit Messinek hívnak!
print("Van olyan játékos, akit Messinek hívnak?")
for i in jateklst:
    if i.nev=="Messi":
        print("Van Messi nevű játékos.")
print("--------------------------------------------")

#4. Számolja meg, hányan voltak válogatott játékosok!
print("Hányan voltak válogatott játékosok?")
valogatottj=0
for i in jateklst:
    if i.valo:
        valogatottj+=1
print(f"{valogatottj} játékos volt válogatott.")
print("--------------------------------------------")

#5. Kérjen be a felhasználótól egy mezszámot, és írja ki annak a játékosnak a nevét és csapatát, akinek ilyen a mezszáma!
a=int(input("Kérek egy mezszámot: "))
for i in jateklst:
    if a==i.mezsz:
        print(f"Játékos neve: ({i.nev}), csapata: ({i.csapat})")
