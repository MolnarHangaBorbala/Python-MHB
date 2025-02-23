file = open("city.txt")
city=[]
for i in file:
    i=i.strip().split()
    i[2]=float(i[2])
    i[3]=float(i[3])
    city.append(i)
file.close()
print(city)
print("-------------------------------")
#hány város
print(len(city), "város van a listában.")
print("-------------------------------")

#legnagyobb város
max=0
cit="aa"

for i in city:
    if i[2]>max:
        max=i[2]
        cit=i[0]
print(cit, "a legnagyobb város.")
print("-------------------------------")
    
#legkevesebb lakosságú város
min=1000
lak="aa"

for i in city:
    if i[3]<min:
        min=i[3]
        lak=i[0]
print(lak,"a legkevesebb lakosságú város.")
print("-------------------------------")

#városok össz lakossága
össz=0

for i in range(len(city)):
    össz=össz+city[i][3]
print("Összesen", össz, "a lakosok száma.")
print("-------------------------------")

#zalai városok össz lakossága
összv=0

for i in range(len(city)):
    if city[i][1]=="Zala":
        összv=összv+city[i][3]
print("A zalai városok össz lakossága:",összv)
