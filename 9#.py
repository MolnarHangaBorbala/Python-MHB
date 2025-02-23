lista=[3,5,9,76,23]

print("---------------")

#össz
print("Össz")
print("1# sum")

print(sum(lista))

print("-------")
print("2# for")

össz=0
for i in lista:
    össz=össz+i
print(össz)

print("-------")
print("3# def")

def össz1():
    i=0
    szum1=0
    while i<len(lista):
        szum1=szum1+lista[i]
        i=i+1
    print(szum1)
össz1()

print("-------")
print("4# while")

i=0
szum1w=0
while i<len(lista):
    szum1w=szum1w+lista[i]
    i=i+1
print(szum1w)

print("---------------")

#elemek
print("Elemek")
print("1# print")

print(lista)
print("-------")

print("2# for")

for i in lista:
    print(i)

print("-------")
print("3# def")

def elem():
    for i in lista:
        print(i)
elem()

print("-------")
print("4# while")

i=0
db=0
while i<len(lista):
    db=db+1
    i+=1
print(db)

print("---------------")

#min
print("Minimum")
print("1# min()")

print(min(lista))

print("-------")
print("2# for")

min=1000
for i in lista:
    if i<min:
        min=i
print(min)

print("-------")
print("3# def")

def min1():
    i=0
    min2=1000
    while i<len(lista):
        if lista[i]<min2:
            min2=lista[i]
        i=i+1
    print(min2)
min1()

print("-------")
print("4# while")

i=0
min2w=1000
while i<len(lista):
    if lista[i]<min2w:
        min2w=lista[i]
    i=i+1
print(min2w)

print("---------------")

#max
print("Maximum")
print("1# max()")

print(max(lista))

print("-------")
print("2# for")

max=0
for i in lista:
    if i>max:
        max=i
print(max)

print("-------")
print("3# def")

def max1():
    i=0
    max2=0
    while i<len(lista):
        if lista[i]>max2:
            max2=lista[i]
        i=i+1
    print(max2)
max1()

print("-------")
print("4# while")

i=0
max2w=0
while i<len(lista):
    if lista[i]>max2w:
        max2w=lista[i]
    i=i+1
print(max2w)

print("---------------")




