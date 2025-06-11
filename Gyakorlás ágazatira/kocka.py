import random
ejatekos=0
mjatekos=0

for i in range(1):
    ejatekos+=random.randint(1,6)
    mjatekos+=random.randint(1,6)


if ejatekos>mjatekos:
    print("Az első játékos nyert: ",ejatekos)
elif mjatekos>ejatekos:
    print("A második játékos nyert: ",mjatekos)
else:
    print("Döntetlen.")
