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
    def getc(self,c):
        self.c=c
    def putC(self):
        print("C :",self.c)
class D(A):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D :",self.d)
    
    def sum(self):
        print("sum :",self.a+self.b+self.c+self.d)

b1=B()
c1=C()
d1=D()
b1.getA(int(input("enter value :")))
b1.getB(int(input("enter value :")))
c1.getC(int(input("enter value :")))
d1.getD(int(input("enter value :")))
b1.putA()
b1.putB()
c1.putC()
d1.putD()

