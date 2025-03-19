"""
print('Hello Premo')

# Ez a komment
print('Ezt kiírja!') #Ezt nem írja ki

szam1 = 10
szam2 = 20

str1 = "Anna"
str2 = 'Peti'
lista1= [3,'alma','Zoli']

print(szam1)
print(str1)
print(lista1)

szam1 = 2
szam2 = 3
szam3 = 8

print(szam1+szam2)
print(szam3/szam2)
print(szam3//szam2)
print(szam2%szam1)
print(szam1**szam2)

szam1 += 1 # szam1=szam1+1
print(szam1)

szam1 *= 2

print(szam1)

# Relációs operátorok (boolean)
# {>;<;>=;=<;!=;==}
print(szam3>szam1)
print(szam3==szam1)
print(szam3!=szam1)

# Logikai operátorok
# {and,or,not}
print(szam3==szam1 and szam3!=szam1)
print(szam3==szam1 or szam3!=szam1)

#List tömb
#Lista létrehozás
lista1 = []
print(lista1)

#Hozzáírás, append
lista1.append(2)
lista1.append('alma')
lista1.append(2)
print(lista1)

#Beszúrás, insert
lista1.insert(1,'körte')
print(lista1)

#Meg fordítja a sorrendet, reverse
lista1.reverse()
print(lista1)

#Lista hosszúságának meghatározása, length (len)
print('A lista',len(lista1),'elemű!')

#Törlés, remove
lista1.remove(2)
print(lista1)

#Törli az összes adatot
lista1.clear()
print(lista1)

#Sorrendbe rakja a listát, sort
lista2=[5,6,3,1]
print(lista2)
lista2.sort() 
print(lista2)

lista3=['Péter','Anna','Zoli','Dia']
print(lista3)
lista3.sort()
print(lista3)

#Lista közvetlen elérése, index kezelés
print(lista3[1]) #Bizonyos elem
print(lista3[0:1]) #Intervallum
print(lista3[0:2]) 
print(lista3[1:]) #Végéig
print(lista3[-1]) #Az utolsó elem
print(lista3[-2]) #Az utolsó elötti elem

#Multi lista
lista4=[[1,4,2],['alma','körte','szilva'],['Zoli','Anna','Peti']]
print(lista4)
print(lista4[2] [1])
print(lista4[2])

#Ciklusok
#For ciklus

for i in range(5):
    print(i,'Nem beszélek az órán')


lista1=['Péter','Anna','Zoli','Dia']

for i in range(len(lista1)):
    print(lista1[i])

for i in lista1:
    print(i)

#While ciklus

szam1=0

while szam1<10:
    print(szam1,'Hello')

    szam1+=1

#If ciklus

kor=25

if kor > 18 and kor<25:
    print('Ön egyetemista')
elif kor <= 18 and kor >14:
    print('Ön középiskolás')
elif kor <=13 and kor >7:
    print('Ön általánosiskolás')
else:
    print('Ön nem iskolás')



psw = 'mama'
print('Kérem a jelszót:')
bem = input()
while bem != psw:
    print('Rossz jelszó!')
    print('Kérem a jelszót:')
    bem = input()
print('ok vége')

#Négyzet kerülete és területe
print('Négyzet kerülete és területe')
print('Kérem a négyzet a oldalát')
a = input()
print('A négyzet területe:')
print(4*int(a))
print('A négyzet kerülete:')
print(int(a)*int(a))

#Téglalap kerülete és területe
print('Téglalap kerülete és területe')
print('Kérem a téglalap a oldalát')
a = input()
print('Kérem a téglalap b oldalát')
b = input()
print('A téglalap területe:')
print(2*int(a)+2*int(b))
print('A téglalap kerülete:')
print(int(a)*int(b))

print('Szia!')
print('Melyik hónapban születtél?')
ho = input()
if ho=='12' or ho=='1' or ho=='2':
    print('Téli hónapban születtél!')
elif ho=='3' or ho=='4' or ho=='5':
    print('Tavaszi hónapban születtél!')
elif ho=='6' or ho=='7' or ho=='8':
    print('Nyári hónapban születtél!')
elif ho=='9' or ho=='10' or ho=='11':
    print('Őszi hónapban születtél!')
else:
    print('Vicces vagy!')

#Páros nem páros
print('kérek egy számot:')
szam=input()
mar=int(szam)%2
print(mar)
if mar==0:
    print('A szám páros')
else:
    print('A szám páratlan')

#Pozitív, negatív vagy nulla
print('Kérek egy számot:')
a = input()
if int(a) > 0:
    print('A szám pozitív!')
elif int(a) < 0:
    print('A szám negatív!')
else:
    print('A szám nulla!')

#Az adott háromszög derékszög-e?
print('Az adott háromszög derékszög-e?')
print('Kérem az a oldalt:')
a = input()
print('Kérem a b oldalt:')
b = input()
print('Kérem a c oldalt:')
c = input()
if int(a)**2 + int(b)**2 == int(c)**2:
    print('A háromszög derékszögű!')
else:
    print('A háromszög nem derékszögű!')
print('Vége')

#Random szám
import random
szam1 = random.randint(3,12)
print('Találd ki melyik számra gondoltam:')
szam2 = input()
if int(szam1)>int(szam2):
    print('A szám nagyobb amire gondoltál')
elif int(szam1) == int(szam2):
    print('Eltaláltad')
else:
    print('A szám kisebb mint amire gondoltál')
print(szam1)

print("Kérem a pontjait")
pont = input()
pont = int(pont)
if pont > 79:
    print("Az ön osztályzata JELES")
elif pont>59:
    print("Az ön ösztáéyzata JÓ")
elif pont>39:
    print("Az ön ösztáéyzata KÖZEPES")
elif pont>19:
    print("Az ön ösztáéyzata ELÉGSÉGES")
else:
    print("Az ön ösztáéyzata ELÉGTELEN")

#print('Szia',padtárs)
padtárs=input();
szam= int(input("Kérek egy számot:"));
for i in range(szam):
    print("Jó napot",padtárs,i)
"""
#35,78,98,12,45,78,12,31,45
lista=[35,79,98,12,45,78,12,31,45]
#Mind
print(lista)
#1.
print(lista[0])
#Végét
print(lista[-1])
#Hány darab
print(len(lista))
#Legkissebb
lista.sort()
print(lista[-1])
#Legnagyobb
print(lista[0])
#Összeg
össz=0
for i in lista:
    össz=össz+i
print(össz)
#Átlag
print(össz/len(lista))
#Mind, de külön sorban
for i in lista:
    print(i)
#Hány db for ciklussal

#Összeg for ciklussal
össz=0
for i in lista:
    össz=össz+i
print(össz)
#Min for ciklussal
min=100
for i in lista:
    if i<min:
        min=i
print(min)
#Max for ciklussal
max=1
for i in lista:
    if i>max:
        max=i
print(max)
