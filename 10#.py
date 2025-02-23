nb1=[]
file = open("Zte.txt")

for i in file:
    i=i.split()
    i[1]=int(i[1])
    i[3]=int(i[3])
    i[5]=int(i[5])
    nb1.append(i)
print(nb1)

print("-----------------------")
print("Az nb1-ben ", len(nb1), "csapat van.")
print("-----------------------")

pont=0
for i in nb1:
    pont=pont+i[3]

print("Összesen", pont,"pontszámot értek el.")
print("-----------------------")

max=0
csap="aa"

for i in nb1:
    if i[3]>max:
        max=i[3]
        csap=i[0]

print("Az első csapat:", csap)
print("-----------------------")

min=100
csap0="bb"

for i in nb1:
    if i[3]<min:
        min=i[3]
        csap0=i[0]

print("Az utolsó csapat:", csap0)
print("-----------------------")

negy=0
csap1="aa"

for i in nb1:
    if i[3]>negy:
        negy=i[3]
        csap1=i[0]

print("A negyedik helyen a", csap1,"áll.")
