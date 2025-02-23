"""
#Ismétlés - négyzet kerület, terület
print('Adja meg a négyzet a oldalát!')
a=int(input())
ker=4*a
ter=a*a
print(f'A négyzet kerülete', {ker})
print(f'A négyzet területe', {ter})

if ker>ter:
    print('A kerület nagyobb!')
elif ker<ter:
    print('A terület nagyobb!')
else:
    print('Egyenlőek!')

#Try és except parancs:

for i in range(5):
    try:
        a=int(input('Kérem az a oldalt:'))
        print('A négyzte kerülete', 4*a)
    except:
        print('Nem számot kaptam!')

i=0
while i<len(range(7)):
    try:
        a=int(input('Kérem az a oldalt:'))
        print('A négyzet kerülete', 4*a)
    except:
        print('Nem számot kaptam!')
    i+=1

#Darabszám ismétlése
lista1=[2, 6, 5, 6, 7]

print(len(lista1))

db=0
for i in lista1:
    db=db+1
print(i)

db=0
for i in range(len(lista1)):
    db=db+1
print(i)

i=0
db=0
while i<len(lista1):
    db=db+1
    i+=0
print(i)

#Maximum, minimum:

max=0
for i in lista1:
    if i<max:
        max=i
print(max)

min=100
for i in lista1:
    if i>min:
        min=i
print(min)

#Random szám
import random
szám=random.randint(1,6)
print('A szám a következő:',szám)

import math 
print("Kérem a háromszög a oldalát")
a=int(input())
print("Kérem a háromszög b oldalát")
b=int(input())
c=math.sqrt(math.pow(a,2)+math.pow(b,2))
print("A háromszög c oldala", c)

i=False
while i!=True:
    try:
        a=int(input("Kérem a háromszög a oldalát"))
        i=True
    except:
        print("Nem számot kaptam.")

i=False
while i!=True:
    try:
        b=int(input("Kérem a háromszög b oldalát"))
        i=True
    except:
        print("Nem számot kaptam.")

i=False
while i!=True:
    try:
        a=int(input("Kérem a háromszög a oldalát"))
        b=int(input("Kérem a háromszög b oldalát"))
        i=True
    except:
        print("Nem számot kaptam.")


import math 
print("Kérem a háromszög p oldalát")
p=int(input())
print("Kérem a háromszög q oldalát")
q=int(input())
m=math.sqrt(p*q)
print("A háromszög m oldala", m)
"""
import math 
print("Kérem a háromszög c oldalát")
c=int(input())
print("Kérem a háromszög p oldalát")
p=int(input())
b=math.sqrt(c*p)
print("A háromszög m oldala", b)


























    
    
