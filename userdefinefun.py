#function with no argument no return value
def printline():
    print("*" *40)
printline()
print("welcome to user define function in python")
printline()


#function with argument but no return value
def add(a,b):
    print("addition :",a+b)
printline()
add(10,20)
printline()

#function with argument but no return value
def add(a,b):
    print("addition :",a+b)
x=int(input("enter value:"))
y=int(input("enter value:"))
add(x,y)
printline()

#function with arguuent with return value
def sub(a,b):
    return a-b
printline()
ans=sub(x,y)
print("substraction :",ans)
print("substraction :",sub(x,y))
printline()
