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
"""



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

print(a1.autoar)
















        
