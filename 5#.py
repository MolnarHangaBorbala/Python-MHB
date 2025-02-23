"""
#Kockával dobjunk egyet
import random
num=random.randint(1,6)
print(num)

#Kockával pokerezzünk
import random
for i in range(5):
    num=random.randint(1,6)
    print(num)

#Két ember dob 3-at, összeadja, aki többet dobott, az nyer. T=Tamás P=Péter
import random
összT=0
for i in range(3):
    T=random.randint(1,6)
    print(T)
    összT=összT+T
print("Tamás össz dobása:",összT)
print("-----------------------")

összP=0
for i in range(3):
    P=random.randint(1,6)
    print(P)
    összP=összP+P
print("Péter össz dobása:",összP)
print("-----------------------")

if összT>összP:
    print("Tamás nyert!")
elif összT<összP:
    print("Péter nyert!")
elif összT==összP:
    print("Tamás és Péter ugyanannyit dobtak.")

#Ugyan az, mint az előbbi, csak fügvénnyel
import random
össz=0
def dobás(össz):
    for i in range(3):
        num=random.randint(1,6)
        össz=össz+num
    return(össz)

összT=dobás(össz)
összP=dobás(össz)

print("Tamás",(összT),"dobott")
print("Péter",(összP),"dobott")
"""
