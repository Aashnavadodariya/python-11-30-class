import udf
while True:
    print("*"*50)
    print("1.max of two")
    print("2.max of three")
    print("3.odd/even")
    print("4.prime")
    print("5.fibonacci")
    print("6.exit")
    print("*"*50)
    choice=int(input("enter your choice :"))

    if choice==1:
       a=int(input("enter number :"))
       b=int(input("enter number :"))
       udf.maxoftwo(a,b)
       print("*"*50)
    
    elif choice==2:
       a=int(input("enter number :"))
       b=int(input("enter number :"))
       c=int(input("enter number :"))
       udf.maxofthree(a,b,c)
       print("*"*50)
   
    elif choice==3:
        a=int(input("enter number :"))
        udf.oddeven(a)
        print("*"*50)

    elif choice==4:
        a=int(input("enter number :"))
        udf.prime(a)
        print("*"*50)

    elif choice==5:
        a=int(input("enter number :"))
        udf.fibonacci(a)
        print("*"*50)
    else:
        break
        
