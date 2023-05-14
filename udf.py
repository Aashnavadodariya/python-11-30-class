def maxoftwo(a,b):
    if a>b:
        print(a,"is greter")
    else:
        print(b,"is greter")

def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print(a,"is greter")
        else:
            print(c,"is greter")
    elif b>c:
        print(b,"is greter")
    else:
        print(c,"is greter")

def oddeven(a):
    if a%2==0:
        print(a,"is even")
    else:
        print(a,"is odd")
def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print(n,"is not prime")
                break
            else:
                print(n,"is prime")
        else:
            print(n,"is not prime")
def fibonacci(n):
     a,b=0,1
     while b<n:
         print(b,end=" ")
         a,b=b,a+b
     print()
         
     
           

