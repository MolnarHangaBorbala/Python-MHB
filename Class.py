class Téglalap:
    def __init__(self,a_oldal,b_oldal):
        self.a_oldal=a_oldal
        self.b_oldal=b_oldal
        
    def kerület(self):
        ker=2*self.a_oldal+2*self.b_oldal
        return ker

    def terület(self):
        ter=self.a_oldal*self.b_oldal
        return ter


teglalap01=Téglalap(2,3)
teglalap02=Téglalap(4,8)

print(teglalap01.a_oldal,teglalap01.b_oldal)
print(teglalap01.kerület())
print(teglalap01.terület())
print(teglalap01)





class Teglalap:
    joteglalap=0
    rosszteglalap=0

    def __init__(self,a_oldal,b_oldal):
        self.a_oldal=a_oldal
        self.b_oldal=b_oldal
        if a_oldal>=1:
            type(self).joteglalap+=1
        else:
            type(self).rosszteglalap+=1

    def kerület(self):
        ker=2*self.a_oldal+2*self.b_oldal
        return ker

    def terület(self):
        ter=self.a_oldal*self.b_oldal
        return ter

    def __repr__(self):
        return f"A téglalap adatai ({self.a_oldal} cm,{self.b_oldal}cm)"

    @classmethod
    def db(cls):
        return cls.joteglalap+cls.rosszteglalap

    @staticmethod
    def alap():
        return"Python The Best/nand The Math!!"

teglalap01=Teglalap(2,3)
teglalap02=Teglalap(4,8)
teglalap03=Teglalap(1,7)
teglalap04=Teglalap(0,7)

print(teglalap01.a_oldal,teglalap01.b_oldal)
print(teglalap01.kerület())
print(teglalap01.terület())
print(teglalap01)
print(Téglalap.joteglalap)
print(Téglalap.rosszteglalap)
print(Téglalap.db())
print(Téglalap.alap())






import random

class Téglalap:
    joteglalap=0
    rosszteglalap=0

    def __init__(self,a_oldal,b_oldal):
        self.a_oldal=a_oldal
        self.b_oldal=b_oldal
        if a_oldal>=1:
            type(self).joteglalap+=1
        else:
            type(self).rosszteglalap+=1 














