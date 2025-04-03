auto=[]
file = open("auto.txt")

for i in file:
    i=i.split()
    i[3]=int(i[3])
    i[4]=int(i[4])
    i[5]=int(i[5])
    auto.append(i)
file.close
print(auto)
print("-----------------------------------------------")
#Mennyi autó van?
print("Összesen",len(auto),"autó van a listában.")
print("-----------------------------------------------")
#Mennyi Audi van?
audi=0
for i in auto:
    if i[0]=="Audi":
        audi=audi+1

print("Összesen",audi,"Audi van.")
print("-----------------------------------------------")
#Mennyi Opel és Nissan van?
opel=0
nissan=0
for i in auto:
    if i[0]=="Opel":
        opel=opel+1
    elif i[0]=="Nissan":
        nissan=nissan+1

print("Összesen",opel,"Opel és",nissan,"Nissan van.")
print("-----------------------------------------------")
#Leggyengébb autó?
min=1000
automin="aa"
automintip="aa"
for i in auto:
    if i[3]<min:
        min=i[3]
        automin=i[0]
        automintip=i[1]
print("A leggyengébb autó:",automin, automintip,",aminek teljesítménye:",min)    
print("-----------------------------------------------")
#Márka felsorolása
márka=""

for i in auto:
    márka=márka+i[0]+","
print(márka)
