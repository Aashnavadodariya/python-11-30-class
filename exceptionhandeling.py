print("start code")

try:
    a=int(input("enter a: "))
    b=int(input("enter b: "))

    c=a/b

    print("Divition :",c)

    l=[1,2,3,4,5]
    index=int(input("enter index number :"))
    print("value :",l[index])
except ZeroDivisionError as e:
    print("exception caught :",e)
except ValueError as e:
    print("exception caught :",e)
except IndexError as e:
    print("exception caught :",e)
except Exception as e:
    print("Exception Caught :",e)
finally:
    print("finally block")
print("end code")
