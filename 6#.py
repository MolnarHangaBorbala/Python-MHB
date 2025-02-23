"""
szoveg="Python programozás"
elso_karakter=szoveg[0] 
utolso_karakter=szoveg[-1]
hossz=len(szoveg) 

#Kis- és nagybetűk átalakítása
kisbetus=szoveg.lower()
nagybetus=szoveg.upper()

#Karakterek cseréje
modositott=szoveg.replace("P","J")

#Szöveg darabolása szavakra
mondat="Tanuljuk a python programozást"
szavak=mondat.split() #["Tanuljuk" "a" "python" "programozást"]

mondat="Tanuljuk*a*python*programozást"
szavak=mondat.split("*")

#Feladat
csapat="Zte 10 hely 13 pont 5 győzelem"
nev=csapat[0].upper()
hely=int(csapat[5])+7
pont=int(csapat[13])+12
gyozelem=int(csapat[21])+2
print(nev,hely,pont,gyozelem)

csapat1="Ute 6 hely 20 pont 7 győzelem"
nev1=csapat1[1].upper()
hely1=int(csapat1[4])+3
pont1=int(csapat1[11])+8
gyozelem1=int(csapat1[19])-5
print(nev1,hely1,pont1,gyozelem1)
"""

file1 = open("Zte.txt", "r")
for i in file1:
    print(i)
file1.close()
