file = open("csoki.txt")
cslst=[]
for i in file:
    i=i.strip().split()
    i[1]=float(i[1])
    i[2]=float(i[2])
    i[3]=float(i[3])
    i[4]=float(i[4])
    i[5]=float(i[5])
    i[6]=float(i[6])
    cslst.append(i)
file.close()
print(cslst)

print("---------------------------------")
print(len(cslst), "darab csoki van.")

print("---------------------------------")
for i in range(len(cslst)):
    print(cslst[i][0],cslst[i][1],"g")
    
print("---------------------------------")
for i in range(len(cslst)):
    print(cslst[i][1],"g")
    
print("---------------------------------")
össz=0
for i in range(len(cslst)):
    össz=össz+cslst[i][1]
print("Összesen", össz, "g nehezek")

print("---------------------------------")
max=0
csok="aa"

for i in cslst:
    if i[1]>max:
        max=i[1]
        csok=i[0]
print(csok, "a legnehezebb csoki")

print("---------------------------------")
max=0

for i in cslst:
    if i[1]>max:
        max=i[1]
print("A legenehezebb csoki", max, "g nehéz")

print("---------------------------------")
mix=0
csoki="aa"

for i in cslst:
    if i[3]>mix:
        mix=i[3]
        csoki=i[0]
print("A", csoki, "csokiban van a legtöbb fehérje.")






















