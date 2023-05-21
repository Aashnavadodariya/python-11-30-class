class A:
    def getA(self,a):
        self.a=a
       
    def putA(self):
        print("A :",self.a)
class B(A):
    def getB(self,b):
        self.b=b
        
    def putB(self):
        print("B :",self.b)
        
class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C :",self.c)
class D(B,C):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D :",self.d)
    
    def sum(self):
        print("sum :",self.a+self.b+self.c+self.d)

d1=D()
d1.getA(int(input("enter value :")))
d1.getB(int(input("enter value :")))
d1.getC(int(input("enter value :")))
d1.getD(int(input("enter value :")))
d1.putA()
d1.putB()
d1.putC()
d1.putD()
d1.sum()
