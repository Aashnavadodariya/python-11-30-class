class A:
    def getA(self,a):
        self.a=a        return self.a
    def putA(self):
        print("A :",self.a)
class B(A):
    def getB(self,b):
        self.b=b
        return self.b
    def putB(self):
        print("B :",self.b)

    def sum(self):
        print("sum :",self.a+self.b)
b1=B()
b1.getA(int(input("enter value :")))
b1.getB(int(input("enter value :")))
b1.putA()
b1.putB()
