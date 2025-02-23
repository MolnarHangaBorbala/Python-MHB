lista=[5,2,2,4,3,2,4,10,5,5,3,5,4,3,3]
'''
print("Kérem hogy Mari néni hány liter lekvárt főzött be:")
L=int(input())
print("2. feladat")
print("Mari néni lekvárja:",L)

print("3. feladat")
i=0
hely=0
for i in lista:
    while i>hely:
        hely=i+1
print("A legnagyobb üveg",max(lista),"dl és",hely,"-dik a sorban.")
'''
print("4. feladat")
össz=sum(lista)

