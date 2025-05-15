class Téglalap:
    def __init__(self,a_oldal,b_oldal):
        self.a_oldal=a_oldal
        self.b_oldal=b_oldal
        
    def kerület(self):
        ker=2*self.a_oldal+2*self.b_oldal
        return ker

    def terület(self):
        ter=self.a_oldal*self.b_oldal
        return ter


teglalap01=Téglalap(2,3)
teglalap02=Téglalap(4,8)

print(teglalap01.a_oldal,teglalap01.b_oldal)
print(teglalap01.kerület())
print(teglalap01.terület())
print(teglalap01)





class Teglalap:
    joteglalap=0
    rosszteglalap=0

    def __init__(self,a_oldal,b_oldal):
        self.a_oldal=a_oldal
        self.b_oldal=b_oldal
        if a_oldal>=1:
            type(self).joteglalap+=1
        else:
            type(self).rosszteglalap+=1

    def kerület(self):
        ker=2*self.a_oldal+2*self.b_oldal
        return ker

    def terület(self):
        ter=self.a_oldal*self.b_oldal
        return ter

    def __repr__(self):
        return f"A téglalap adatai ({self.a_oldal} cm,{self.b_oldal}cm)"

    @classmethod
    def db(cls):
        return cls.joteglalap+cls.rosszteglalap

    @staticmethod
    def alap():
        return"Python The Best/nand The Math!!"

teglalap01=Teglalap(2,3)
teglalap02=Teglalap(4,8)
teglalap03=Teglalap(1,7)
teglalap04=Teglalap(0,7)

print(teglalap01.a_oldal,teglalap01.b_oldal)
print(teglalap01.kerület())
print(teglalap01.terület())
print(teglalap01)
print(Teglalap.joteglalap)
print(Teglalap.rosszteglalap)
print(Teglalap.db())
print(Teglalap.alap())






import random

class Teglalap:
    joteglalap=0
    rosszteglalap=0

    def __init__(self,a_oldal,b_oldal):
        self.a_oldal=a_oldal
        self.b_oldal=b_oldal
        if a_oldal>=1:
            type(self).joteglalap+=1
        else:
            type(self).rosszteglalap+=1 

    def kerület(self):
        ker=2*self.a_oldal+2*self.b_oldal
        return ker

    def terület(self):
        ter=self.a_oldal*self.b_oldal
        return ter

    def __repr__(self):
        return f"A téglalap adatai ({self.a_oldal} cm,{self.b_oldal}cm)"

    @classmethod
    def db(cls):
        return cls.joteglalap+cls.rosszteglalap

    @staticmethod
    def alap():
        return"Python The Best/nand The Math!!"

teglalapok=[]

for i in range(10):
    teglalap1=Teglalap(random.randint(0,6),random.randint(1,6))
    teglalapok.append(teglalap1)


print(teglalapok)
print(Teglalap.joteglalap)
print(Teglalap.rosszteglalap)
print(Teglalap.db())
print(teglalapok[0].a_oldal)

for i in teglalapok:
    if i.a_oldal==6:
        print("Van 6-os 'a' oldalú téglalap.")
        break






class Csoki:
    feherje_gazdag=0
    feherje_szegeny=0
    def __init__(self,nev,suly,energia,feherje,szenhidrat,zsír,cukor):
        self.nev=nev
        self.suly=float(suly)
        self.energia=float(energia)
        self.feherje=float(feherje)
        self.szenhidrat=float(szenhidrat)
        self.zsír=float(zsír)
        self.cukor=float(cukor)
        if self.feherje >2:
            type(self).feherje_gazdag+=1
        else:
            type(self).feherje_szegeny+=1

def __repr__(self):
    return f"Csoki({self.nev}, {self.súly} g, {self.energia} kcal, {self.feherje}g feherje, {self.szenhidrat}g szényhidrát, {self.zsír}g zsír, {self.cukor}g cukor)"

    @classmethod
    def db(cls):
        return cls.feherje_gazdag+cls.feherje_szegeny

    @staticmethod
    def alap():
        return "A csoki finom!!"




csoki_lista=[]

with open("csoki.txt", encoding="utf-8") as file:
    #next(file) Fejléc átugrása
    for sor in file:
        adat=sor.strip().split()
        csoki_obj=Csoki(*adat)
        csoki_lista.append(csoki_obj)

#Lista kiírása
for csoki in csoki_lista:
    print(csoki)
print(csoki_lista)
print('------------222---------------')
print(csoki_lista[1].nev)
print(len(csoki_lista))

for i in csoki_lista:
    print(i.nev)



max1=0
id1=0
id2=0
for i in csoki_lista:
    if i.suly>max1:
        max1=i.suly
        id2=id1
    id1=id1+1


print(csoki_lista[id2].nev,csoki_lista[id2].suly)
print(csoki_lista[id2])
print(Csoki.feherje_gazdag)
print(Csoki.db())
print(Csoki.alap())
