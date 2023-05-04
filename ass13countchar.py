string=input("enter string :")
print("operation to perform 1.total length 2.count of charcter")
choice=input()
if choice=='1':
    print(len(string))
elif choice=='2':
    char=input("enter charcter :")
    if char in string:
        print(string.count(char))
    else:
        print("charcter not availble")
else:
    print("invalid choice")
