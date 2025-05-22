"""
import random

tanar=0
diak=0
i=0

for i in range(1):
    tanar=random.randint(1,6)
    diak=random.randint(1,6)

print("Tanár:",tanar)
print("Diák:",diak)
if tanar>diak:
    print("A tanár nyert!")
elif tanar<diak:
    print("A diák nyert!")
elif tanar==diak:
    print("Döntetlen!")





import random

nap=[]
áll=[]

for i in range(random.randint(15,30)):
    nap.append(random.randint(15,30))

for i in range(random.randint(10,22)):
    áll.append(random.randint(10,22))


def függ():
    i=0
    minn=1000
    maxn=0

    miná=1000
    maxá=0

    
    for i in nap:
        while i<minn:
            minn=i
        while i>maxn:
            maxn=i
        átlagn=minn+maxn
    for i in áll:
        while i<miná:
            miná=i
        while i>maxá:
            maxá=i
        átlagá=miná+maxá

    
    print("Állat:",miná,maxá,"Nap:",minn,maxn)
    print("Állat átlag:",átlagá,"Nap átlag:",átlagn)
függ()



class Szulo():
    def __init__(self,vnev,knev,gydb):
        self.vnev=vnev
        self.knev=knev
        self.gydb=gydb

    def gyar(self):
        ar=self.gydb*50000
        return ar

    def __repr__(self):
        return f"A szülő neve ({self.vnev} {self.knev} és {self.gydb} db gyereke van)"

sz1=Szulo("Kovács","Péter",2)
sz2=Szulo("Horváth","Kálmán",3)
    
print(sz1)
print(sz1.gyar())
print(sz1.knev)
print(sz2)
print(sz2.gyar())
print(sz2.knev)
print(sz2.gydb)



class Auto():
    def __init__(self,marka,tipus,ar):
        self.marka=marka
        self.tipus=tipus
        self.ar=ar

    def autoar(self):
        autoar=self.ar*1,27
        return autoar

    def __repr__(self):
        return f"Az auto márkája: ({self.marka} tipusa: {self.tipus} ára: {self.ar})"

a1=Auto("Nissan","Almera",3000000)

print(a1.autoar())









class Kutya():
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def kora(self):
        ko=self.kor*7
        return ko

    def __repr__(self):
        return f"A kutya fajtája: {self.fajta}, neve {self.nev}, kora: {self.kor}"

k1=Kutya("Amerikai staffordshire terrier","Rokkó",12)
k2=Kutya("Tacskó","Mucsi",4)

print(k1)
print("----------------------------")
print(k2)
print("----------------------------")
print("1. Példa:")
print(k1.nev)
print(k1.fajta)
print(k1.kora())
print("----------------------------")
print("2. Példa:")
print(k2.nev)
print(k2.fajta)
print(k2.kora())
"""



import random
korlst=[]

class Kor():        
    def __init__(self,sugar):
        self.sugar=sugar

    def kerulet(self):
        ker=self.sugar*2*3.14
        return ker

    def __repr__(self):
        return f"A kor sugara {self.sugar}"

for i in range(12):
    k1=Kor(random.randint(2,7))
    korlst.append(k1)


print(korlst)
print(k1)
print(k1.kerulet())

























        
