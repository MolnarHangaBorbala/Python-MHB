#Választás
import math

def negyzet():
    for i in range(3):
        try:
            a=float(input("Kérek egy számot: "))
            if a>0:
                print("A négyzet kerülete: ", 4*a)
                print("A négyzet területe: ", a*a)
                break
            else:
                print("Negatív szám nem lehetséges...")
        except:
            print("Ez nem szám.")

def teglalap():
    for i in range(3):
        try:
            a=float(input("Kérem a téglalap 'a' oldalát: "))
            b=float(input("Kérem a téglalap 'b' oldalát: "))
            if a>0 and b>0:
                print("A téglalap kerülete: ", 2*a+2*b)
                print("A téglalap területe: ", a*b)
                break
            else:
                print("Negatív szám nem lehetséges...")
        except:
            print("Ez nem szám.")

def haromszog():
    for i in range(3):
        try:
            a=float(input("Kérem a háromszög 'a' oldalát: "))
            b=float(input("Kérem a háromszög 'b' oldalát: "))
            c=float(input("Kérem a háromszög 'c' oldalát: "))
            s=(a*b*c)/2
            ter=math.sqrt(s*(s-a)*(b-a)*(c-a))
            if a>0 and b>0 and c>0:
                print("A háromszög kerülete: ", a+b+c)
                print("A háromszög területe: ", ter)
                break
            else:
                print("Negatív szám nem lehetséges...")
        except:
            print("Ez nem szám.")

def kor():
    for i in range(3):
        try:
            r=float(input("Kérek egy számot: "))
            if r>0:
                print("A kör kerülete: ", 2*r*math.pi)
                break
            else:
                print("Negatív szám nem lehetséges...")
        except:
            print("Ez nem szám.")



while True:
    try:
        mit_akar = int(input("\n Válasszon az opciók közül: \n 1. Négyzet kerülete és területe \n 2. Téglalap kerülete \n 3. Háromszög \n 4. Kör \n 5. Kilép \n"))
        if mit_akar == 1:
            print("---Négyzet---")
            negyzet()
        if mit_akar == 2:
            print("---Téglalap---")
            teglalap()
        if mit_akar == 3:
            print("---Háromszög---")
            haromszog()
        if mit_akar == 4:
            print("---Kör---")
            kor()
        if mit_akar == 5:
            print("---Kilép---")
            break
    except ValueError:
        print("Ez nem szám")
