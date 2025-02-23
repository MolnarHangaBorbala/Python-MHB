"""
i=0
while i<5:
    try:
        a=int(input("Kérek egy számot:"))
        print("A szám fele:", a/2)
        i=5
    except:
        print("Nem számot kaptam.")
        i=i+1
"""
list=[4,24,7,48,8,4]
print(list)
print("---Len---")
print(len(list))

print("---For---")
db=0
for i in list:
    db=db+1
print(db)

print("---While---")
i=0
db=0
while i<len(list):
    db=db+1
    i+=1
print(db)

print("---Sum---")
print(sum(list))

print("---For---")
i=0
össz=0
for i in list:
    össz=össz+i
print(össz)

print("---While---")
i=0
sum1w=0
while i<len(list):
    sum1w=sum1w+list[i]
    i=i+1
print(sum1w)

print("---Min---")
print(min(list))

print("---For---")
min=1000
for i in list:
    if i<min:
        min=i
print(min)

print("---While---")
i=0
min2w=1000
while i<len(list):
    if list[i]<min2w:
        min2w=list[i]
    i=i+1
print(min2w)

print("---Max---")
print(max(list))

print("---For---")
max=0
for i in list:
    if i>max:
        max=i
print(max)

print("---While---")
i=0
max2w=0
while i<len(list):
    if list[i]>max2w:
        max2w=list[i]
    i=i+1
print(max2w)















