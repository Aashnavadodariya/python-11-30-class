n=int(input("enter the number of element in the list :"))
list1=[]
for i in range(n):
    a=int(input("enter the elements of list 1:"))
    list1.insert(i,a)
print(list1)

m=int(input("enter the number of element in the list :"))
list2=[]
for j in range(m):
    b=int(input("enter the elements of list :"))
    list2.insert(i,b)
print(list2)

for a in list1:
    for b in list2:
        if a==b:
            print("true")
