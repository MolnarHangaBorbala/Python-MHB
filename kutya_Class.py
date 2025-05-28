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
"""

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































