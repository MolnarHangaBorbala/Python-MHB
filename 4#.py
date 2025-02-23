"""
lista=[3,5,1,12,5,8,1]

#Van-e és hol?
hely=0
for i in lista:
    hely=hely+1
    if i==5:
        print(hely)

#Téglalap és négyzet területe és kerülete (def)
a=5
b=6
def feladat(a,b):
    print("A négyzet kerülete és területe",4*a)
    print("A téglalap kerülete és területe",2*a+2*b)

feladat(a,b)


a=float(input())
b=float(input())
def feladat(a,b):
    ker=2*a+2*b
    ter=a*b
    return(ker,ter)

print("A téglalap kerülete:",feladat(a,b)[0])
print("A téglalap területe:",feladat(a,b)[1])

if feladat(a,b)[0]>feladat(a,b)[1]:
    print("A kerület a nagyobb.")
elif feladat(a,b)[0]==feladat(a,b)[1]:
    print("A kerület és a terület egyenlő.")
else:
    print("A terület a nagyobb.")

#2024.11.14.
r=float(input("Kérem a kör sugarát"))
def kor(r):
    print("A kör kerülete:",2*r*3.14)
kor(r)

#2
r=float(input("Kérem a kör sugarát:"))
def sugár(r):
    ker=2*r*3.14
    ter=r*r*3.14
    return(ker,ter)

print("A kör kerülete:",sugár(r)[0])
print("A kör területe:",sugár(r)[1])

if sugár(r)[0]>sugár(r)[1]:
    print("A kerület a nagyobb.")
elif sugár(r)[0]==sugár(r)[1]:
    print("A kerület és a terület egyenlő.")
else:
    print("A terület a nagyobb.")
"""
#mind, de külön sorban függvénnyel
lista=[2,62,81,23,6,19]

def feladat():
    for i in lista:
        print(i)
feladat()











