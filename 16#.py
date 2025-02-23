"""
i=0
while i<3:
    try:
        a=float(input("Kérem az a oldalat:"))
        b=float(input("Kéreb a b oldalat:"))
        if a>0:
            print("Terület:", a*b)
            print("Kerület:", 2*a+2*b)
            i=i+1
        else:
            print("Negatív számot kaptam")
            i=i+1
    except:
        print("Nem számot kaptam")
        i=i+1
"""

class Kutya():
    neve=""
    fajta=""

k1=Kutya()
k1.neve="Bodri"
k1.fajta="tacskó"

print(k1)
print(k1.neve)
print(k1.fajta)

print("--------------------------")

k2=Kutya()
k2.neve="Jerry"
k2.fajta="németjuhász"

print(k2)
print(k2.neve)
print(k2.fajta)

print("--------------------------")

class Negyzet():
    a=9

    def set_a(self,value):
        self.a=value
        
kicsi=Negyzet()
kicsi.a=5
kozepes=Negyzet()
kozepes.a=10
nagy=Negyzet()
nagy.a=50

print(4*kicsi.a)
print(4*kozepes.a)
print(4*nagy.a)

nagy.set_a(100)
print(nagy.a)

print("--------------------------")

class Allat():
    def __init__(self,faj,darab):
        self.faj =faj
        self.darab=darab

madar=Allat
madar.faj="madar"

macska=Allat("macska",2)

print(madar.faj)
print(macska.faj)

print("--------------------------")

class Konyv:
    def __init__(self,cím,szerzo,ar,ev):
        self.cím = cím
        self.szerzo = szerzo
        self.ar = ar
        self.ev = ev

    def kiír(self):
    #Kiírja a könyv adatait
        print(f"Cím: {self.cím}")
        print(f"Szerző: {self.szerzo}")
        print(f"Ár: {self.ar} Ft")
        print(f"Kiadási év: {self.ev}")

konyv1 = Konyv("A kis herceg", "Antonie de Saint-Exupéry", 2000, 1943)
konyv2 = Konyv("A ceg", "Thomas", 2500, 1993)
konyv3 = Konyv("The Dark One", "Nikki St. Crowe", 4700, 2022)
konyv4 = Konyv("Atomi szokások", "James Clear", 6800, 2020)
konyv5 = Konyv("Rachel Price visszatérése", "Holly Jackson", 5690, 2025)

konyv1.kiír()
print("----------")
konyv2.kiír()
print("----------")
konyv3.kiír()
print("----------")
konyv4.kiír()
print("----------")
konyv5.kiír()

print("--------------------------")

a=konyv2
a.kiír()

print("--------------------------")

lst=[konyv1,konyv2,konyv3,konyv4,konyv5]
print(lst[4].ev)



















