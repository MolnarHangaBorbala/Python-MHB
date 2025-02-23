lista=[21,4,16,44,28]
'''
a=0
i = int(input())
if i in lista:
    print("Van ilyen szám a listában.")
else:
    print("Nincs ilyen szám a listában.")
'''
def len3():
    len3=0
    a=0
    while a<len(lista):
        len3+=1
        a+=1
    print(len3)
len3()

