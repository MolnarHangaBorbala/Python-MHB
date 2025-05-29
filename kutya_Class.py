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

print("Lista kiírása:")
file=open("kutya.txt", encoding="utf-8")
kutyalst1=[]
for i in file:
    i=i.split()
    i[2]=int(i[2])
    kutyalst1.append(i)    
file.close()
print(kutyalst1)
print("------------------------------")

#Hány kutya van a listában?
print("Hány kutya van a listában?")
print(len(kutyalst1), "kutya van a listában.")
print("------------------------------")

#Van Rex nevű kutya?
print("Van Rex nevű kutya?")
for i in kutyalst1:
    if i[1]=="Rex":
        print("Igen")
print("------------------------------")

#Van-e 'input' nevű kutya?
print("Kérem a keresendő kutya nevét:")
a=input()
for i in kutyalst1:
    if i[1]==a:
        print("Van",a,"nevű kutya.")
        break
    else:
        print("Nincs",a,"nevű kutya.")
        break
print("------------------------------")

#Hány tacskó van?
print("Hány kutya van a listában?")
tacskó=0
for i in kutyalst1:
    if i[0]=="Tacskó":
        tacskó+=1
print(tacskó,"tacskó van a listában.")
print("------------------------------")

#Van-e 'input' korú kutya?
print("Kérem a keresendő kutya korát:")
a=int(input())
for i in kutyalst1:
    if i[2]==a:
        print("Van",a,"éves kutya.")
        break
    else:
        print("Nincs",a,"éves kutya.")
        break
print("------------------------------")

