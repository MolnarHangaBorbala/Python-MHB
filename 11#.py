"""
i=0
while i<5:
    try:
        a=int(input("Kérem a négyzet a oldalát:"))
        print("A négyzet kerülete:", 4*a)
        i=5
    except:
        print("Nem számot kaptam.")
        i=i+1
print("-----vége-----")
"""

nb1=[]
file=open("Zte.txt")

for i in file:
    i=i.split()
    i[1]=int(i[1])
    i[3]=int(i[3])
    i[5]=int(i[5])
    nb1.append(i)
file.close()
print(nb1)

#Hány csapat van?
print("--------------------------------------------")
print("Az nb1-ben összesen", len(nb1), "csapat van.")

#Hány pontja van as összes foci klubbnak?
print("--------------------------------------------")
össz=0
for i in nb1:
    össz=össz+i[3]
print("Összesen", össz, "pontot értek el a csapatok.")

#Melyik csapatnak van a legtöbb pontja?
print("--------------------------------------------")
max=0
csap="aa"

for i in nb1:
    if i[3]>max:
        max=i[3]
        csap=i[0]

print("A(z)", csap,"csapatnak van a legtöbb pontja.")

#Melyik csapatnak van a legkevesebb pontja?
print("--------------------------------------------")
min=100
csap2="aa"

for i in nb1:
    if i[3]<min:
        min=i[3]
        csap2=i[0]

print("A(z)", csap2,"csapatnak van a legkevesebb pontja.")

#Melyik csapat van a 4. helyen?
print("--------------------------------------------")
csap4="aa"

for i in nb1:
    if i[1]==4:
        csap4=i[0]

print("A 4. helyen a(z)", csap4,"csapat áll.")














