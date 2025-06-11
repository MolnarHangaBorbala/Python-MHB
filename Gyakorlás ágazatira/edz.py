import random

nap=random.randint(12,30)
orak=[]
for i in range(nap):
    i=random.randint(1,5)
    orak.append(i)

def Szamolas():
    minidonap=0
    maxidonap=0
    for i in orak:
        if i==1:
            minidonap+=1
        elif i==5:
            maxidonap+=1

    átlag=sum(orak)/nap
    össz=minidonap+maxidonap

    print(f"A teljes edzésterv napjainak száma: ({nap})")
    print(f"A napi gyakorlási idők listája: ({orak})")
    print("A legkevesebb és legtöbb napi óraszám összege:",össz)
    print(f"Az átlagos napi gyakorlási idő: {átlag:.2f}")
Szamolas()
