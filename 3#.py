lista=[4,3,4,5,1,13,5,6]
"""
print(lista)
print(lista[2])

for i in lista:
    print(i)
    
print(len(lista))

db=0
for i in lista:
    db=db+1
print(db)

össz=0
for i in lista:
    össz=össz+i
print(össz)

print(sum(lista))

szum1=0
for i in range(len(lista)):
    szum1=szum1+lista[i]
print(szum1)

szum2=0
for i in lista:
    szum2=szum2+i
print(szum2)

def prt3():
    i=0
    szum3=0
    while i<len(lista):
        szum3=szum3+lista[i]
        i=i+1
    print(szum3)
prt3()

max1=0
for i in range(len(lista)):
    if lista[i]>max1:
        max1=lista[i]
print(max1)

max1=0
for i in lista:
    if i>max1:
        max1=i
print(max1)

def prt4():
    i=0
    max2=0
    while i<len(lista):
        if lista[i]>max2:
            max2=lista[i]
        i=i+1
    print(max2)
prt4()
"""
