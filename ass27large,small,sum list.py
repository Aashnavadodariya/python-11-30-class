mylist=[20,30]
mylist.sort()
print(mylist)

print("smallest element is:",mylist[0])
print("largest element is:",mylist[-1])


mylist=[5,10,15,20]
total=0

for i in range(0,len(mylist)):
               total=total+mylist[i]

print("sum of all element in given list ",total)
