class A:
    def getA(self,a):
        self.a=a
       
    def putA(self):
        print("A :",self.a)
class B:
    def getB(self,b):
        self.b=b
        
    def putB(self):
        print("B :",self.b)
class c(A,B):
    def getc(self,c):
        self.c=c
    def putc(self):
        print("c :",self.c)
    
    def sum(self):
        print("sum :",self.a+self.b+self.c)
b1=c()
b1.getA(int(input("enter value :")))
b1.getB(int(input("enter value :")))
b1.getc(int(input("enter value :")))
b1.putA()
b1.putB()
b1.putc()
