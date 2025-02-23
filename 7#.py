nb1=[]
file = open("Zte.txt","r")

for i in file:
    i=i.split()
    nb1.append(i)
file.close()
print(nb1)

nb1[0][0]=nb1[0][0].upper()
nb1[0][1]=int(nb1[0][1])-2
nb1[0][3]=int(nb1[0][3])+2
nb1[0][5]=int(nb1[0][5])+2
nb1[0][6]=nb1[0][6].replace("o","oo")

nb1[1][0]=nb1[1][0].lower()
nb1[1][1]=int(nb1[1][1])+2
nb1[1][3]=int(nb1[1][3])-2
nb1[1][5]=int(nb1[1][5])-2
nb1[1][6]=nb1[1][6].replace("o","oo")

