"""
a=int(input("Kérek egy számot: "))
ker=4*a
ter=a*a
print(ker)
print(ter)
if ker>ter:
    print("A kerület a nyagyobb.")
elif ter>ker:
    print("A kerület a nyagyobb.")
else:
    print("A két szám egyenlő.")


import random

ossz=0
for i in range(3):
    a=random.randint(1,6)
    ossz=ossz+a
print("Az első játékos dobásai:", ossz)

ossz2=0
for i in range(3):
    b=random.randint(1,6)
    ossz2=ossz2+b
print("Az első játékos dobásai:", ossz2)
print("------------------------------------------")

if ossz>ossz2:
    print("Az első játékos dobott többet.")
elif ossz2>ossz:
    print("A második játékos dobott többet.")
else:
    print("A két játékos dobásai egyenlőek.")



lst=[1,3,4,6,8,9,4,32]
print(lst)


print("---print(len(lst))---")
print(len(lst))


print("---print(sum(lst))---")
print(sum(lst))


print("---for i in lst:---")
ossz=0
for i in lst:
    ossz=ossz+i
print(ossz)


print("---print(min(lst))---")
print(min(lst))


print("---for i in range(len(lst)):---")
min=1000
for i in range(len(lst)):
    if min > lst[i]:
        min = lst[i]
print(min)


print("---print(max(lst))---")
print(max(lst))


print("---for i in range(len(lst)):---")
max1=0
i=0
while i != len(lst):
    if max1 < lst[i]:
        max1 = lst[i]
    i=i+1
print(max1)


print("------------------------------")
db=0
a=int(input("Kérek egy számot: "))
for i in lst:
    if i == a:
        db=db+1
if db > 0:
    print("Van benne,", db)
else:
    print("Nincs benne")

print("---def1---")
def negyzet1():
    a=int(input("Kérek egy számot:"))
    print("Kerület:", 4*a)
    print("Terület:", a*a)
negyzet1()


print("---def2---")
def negyzet2(a):
    print("Kerület:", 4*a)
    print("Terület:", a*a)
a=int(input("Kérek egy számot:"))
negyzet2(a)


print("---def3 return---")
a=int(input("Kérek egy számot: "))
def negyzet3():
    ker=4*a
    ter=a*a
    return ker,ter

print(negyzet3(a)[0])
print(negyzet3(a)[1])
"""


str1="Korte"
print("---print(len(str1))---")
print(len(str1))

print("---print(str1[0])---")
print(str1[0])

print("---'Mississippi'---")
lst=[]
str2="Mississippi"
for i in str2:
    if i not in lst:
        lst.append(i)
print(lst)







