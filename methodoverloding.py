class Point:
    
    def __init__(self,x,y):
        print("init called")
        self.x=x
        self.y=y
    def __str__(self):
        print("str called")
        return "[{0},{1}]".format(self.x,self.y)
    def __add__(self,obj):
        print("add called")
        x=self.x+obj.x
        y=self.y+obj.y
        return Point(x,y)
    
P1=Point(10,20)
print(P1)
P2=Point(30,40)
print(P2)
print("Addition of 2 Objects :" ,P1+P2)
