#Hány csapat van?
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

print(f"Az nb1-ben {len(nb1)} csapat van!")

#Hány pontot szereztek összesen a csapatok?
ossz=0
for i in nb1:
    ossz=ossz+i[3]

print(f"Az nb1 csapatoknak összesen {ossz} pontja lett!")

#Melyik csapatnak van a legöbb pontja?
max=0
csapat1="dd"
for i in nb1:
    if i[3]>max:
        max=i[3]
        csapat1=i[0]
        
print(f"A {csapat1} csapatnak lett a legtöbb pontja.")

#Melyik csapatnak lett a legkevesebb pontja?
min=100
csapat2="dd"
for i in nb1:
    if i[3]<min:
        min=i[3]
        csapat2=i[0]
        
print(f"A {csapat2} csapatnak lett a legkevesebb pontja.")

#Melyik csapat van a 4. helyen?
hely=4

for i in nb1:
    if i[1]==hely:
        csapat1=i[0]

print(f"A {csapat1} érte el a 4. helyet.")

#Melyik csapat van a(z) input helyen?
hely=input()
csapat0="dd"
for i in nb1:
    if i[1]==hely:
        csapat0=i[0]

print(f"A {csapat0} érte el a {hely}. helyet.")
