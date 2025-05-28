"""
kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def elet(self):
        korr=self.kor*7
        return korr

    def __repr__(self):
        return f"A kutya fajtája: {self.fajta}, neve: {self.nev}, kora: {self.kor}"

with open("kutya.txt", encoding="utf-8") as file:
    for sor in file:
        adat= sor.strip().split()
        k1=Kutya(*adat)
        kutyalst.append(k1)

print(kutyalst)
print("---------------------------------------------------------")


kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def elet(self):
        korr=self.kor*7
        return korr

    def __repr__(self):
        return f"A kutya fajtája: {self.fajta}, neve: {self.nev}, kora: {self.kor}"

file = open("kutya.txt", encoding="utf-8")
for i in file:
    i=i.strip().split()
    k1=Kutya(*i)
    kutyalst.append(k1)

print(kutyalst)
print("---------------------------------------------------------")


kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def elet(self):
        korr=self*7
        return korr

    def __repr__(self):
        return f"A kutya fajtája {self.fajta}, neve: {self.nev}, kora: {self.kor}"

file = open("kutya.txt", encoding="utf-8")
for i in file:
    i=i.strip().split()
    k1=Kutya(*i)
    kutyalst.append(k1)

print(kutyalst)
print("---------------------------------------------------------")


kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def elet(self):
        korr=kor*7
        return korr

    def __repr__(self):
        return f"A kutya fajtája: {self.fajta}, neve: {self.nev}, kora: {self.kor}"

file = open("kutya.txt", encoding="utf-8")
for i in file:
    i=i.strip().split()
    k1=Kutya(*i)
    kutyalst.append(k1)

print(kutyalst)
print("---------------------------------------------------------")


kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def elet(self):
        korr=kor*7
        return korr

    def __repr__(self):
        return f"A kutya fajtája: {self.fajta}, neve: {self.nev}, kora: {self.kor}"

file = open("kutya.txt", encoding="utf-8")
for sor in file:
    adat= sor.strip().split()
    k1=Kutya(*adat)
    kutyalst.append(k1)

print(kutyalst)
print("---------------------------------------------------------")


kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def elet(self):
        korr=kor*7
        return korr

    def __repr__(self):
        return f"A kutya fajtája: [self.fajta], neve: {self.nev}, kora: {self.kor}"

file = open("kutya.txt", encoding="utf-8")
for sor in file:
    adat=sor.strip().split()
    k1=Kutya(*adat)
    kutyalst.append(k1)
print(kutyalst)
print("---------------------------------------------------------")


kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def elet(self):
        korr=kor*7
        return korr

    def __repr__(self):
        return f"A kutya fajtája: {self.fajta}, neve: {self.nev}, kora: {self.kor}"

file = open("kutya.txt", encoding="utf-8")
for sor in file:
    adat=sor.strip().split()
    k1=Kutya(*adat)
    kutyalst.append(k1)
print(kutyalst)
print("---------------------------------------------------------")


kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def elet(self):
        korr=kor*7
        return korr

    def __repr__(self):
        return f"A kutya fajtája: {self.fajta}, neve: {self.nev}, kor: {self.kor}"

file = open("kutya2.txt", encoding="utf-8")
for sor in file:
    adat=sor.strip().split()
    k1=Kutya(*adat)
    kutyalst.append(k1)
print(kutyalst)
print("---------------------------------------------------------")


file = open("kutya2.txt", encoding="utf-8")
kutyalst1=[]
for i in file:
    i=i.split()
    i[2]=int(i[2])
    kutyalst1.append(i)
print(kutyalst1)
print("-------------------")

#Hány Dalmatian és Labrador?
print("Hány Dalmatian és Labrador?")
dalmatian=0
labrador=0

for i in kutyalst1:
    if i[0]=="Dalmatian":
        dalmatian+=1
    elif i[0]=="Labrador":
        labrador+=1

print(dalmatian,"Dalmatian és",labrador,"Labrador")
print("--------------------")

#Kutyanevek kiírása:
print("Kutyanevek kiírása:")
kutyanevek=[]
e_knevek={"Labrador","Németjuhász","Beagle","Bulldog","GoldenRetriever","Tacskó","BorderCollie","ShihTzu","Spániel","Dalmatian",}

for i in kutyalst1:
    if i[0] in e_knevek and i[0] not in kutyanevek:
        kutyanevek.append(i[0])
        
print(",".join(kutyanevek))
print("---------------------------------------------------------")


kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def elet(self):
        korr=kor*7
        return korr

    def __repr__(self):
        return f"A kutya fajtája: {self.fajta}, neve: {self.nev}, kor: {self.kor}"

file = open("kutya.txt", encoding="utf-8")
for sor in file:
    adat=sor.strip().split()
    k1=Kutya(*adat)
    kutyalst.append(k1)
print(kutyalst)
print("---------------------------------------------------------")


kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.kor=kor
        self.nev=nev

    def elet(self):
        return int(self.kor)*7

    def __repr__(self):
        return f"A kutya fajtája: {self.fajta}, neve: {self.nev}, kora kutya években: {self.kor}, emberi években: {self.elet()}"

file = open("kutya.txt", encoding="utf-8")
for sor in file:
    adat=sor.strip().split()
    k1=Kutya(*adat)
    kutyalst.append(k1)
print(kutyalst)
print("---------------------------------------------------------")


kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def elet(self):
        return int(self.kor)*7

    def __repr__(self):
        return f"A kutya fajtája: {self.fajta}, neve: {self.nev}, kora kutya években {self.kor}, emberi években {self.elet()}"

file = open("kutya.txt", encoding="utf-8")
for sor in file:
    adat=sor.strip().split()
    k1=Kutya(*adat)
    kutyalst.append(k1)

for kutya in kutyalst:
    print(kutya)
print("---------------------------------------------------------")


kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def elet(self):
        return int(self.kor)*7

    def __repr__(self):
        return f"A Kutya fajtája: ({self.fajta}), neve: ({self.nev}), kora emberi években ({self.kor}), kutya években ({self.elet()})"

file = open("kutya.txt", encoding="utf-8")
for sor in file:
    adat=sor.strip().split()
    k1=Kutya(*adat)
    kutyalst.append(k1)

for kutya in kutyalst:
    print(kutya)
print("---------------------------------------------------------")


kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def elet(self):
        return int(self.kor)*7

    def __repr__(self):
        return f"A kutya fajtája: ({self.fajta}), neve: ({self.nev}), kora kutya években ({self.kor}), emberi években ({self.elet()})"

file=open("kutya.txt", encoding="utf-8")
for sor in file:
    adat=sor.strip().split()
    k1=Kutya(*adat)
    kutyalst.append(k1)

for kutya in kutyalst:
    print(kutya)
print("---------------------------------------------------------")


kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def elet(self):
        return int(self.kor)*7

    def __repr__(self):
        return f"A kutya fajtája: ({self.fajta}), neve: ({self.nev}), kora kutya években ({self.kor}), emberi években ({self.elet()})"

file = open("kutya.txt", encoding="utf-8")
for sor in file:
    adat=sor.strip().split()
    k1=Kutya(*adat)
    kutyalst.append(k1)

for kutya in kutyalst:
    print(kutya)
print("---------------------------------------------------------")
"""

kutyalst=[]

class Kutya:
    def __init__(self,fajta,nev,kor):
        self.fajta=fajta
        self.nev=nev
        self.kor=kor

    def elet(self):
        return int(self.kor)*7

    def __repr__(self):
        return f"A kutya fajtája: ({self.fajta}), neve: ({self.nev}), kora kutya években ({self.kor}), emberi években ({self.elet()})"

file=open("kutya.txt", encoding="utf-8")
for sor in file:
    adat=sor.strip().split()
    k1=Kutya(*adat)
    kutyalst.append(k1)

for kutya in kutyalst:
    print(kutya)
print("---------------------------------------------------------")
