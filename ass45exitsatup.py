length = int(input("enter size of tuple :"))
my_tuple = tuple()
for i in range(length):
    temp=int(input("enter a tuple items :"))
    my_tuple +=(temp,)
element = int(input("enter an element to check :"))
try:
    index = my_tuple.index(element)
except ValueError:
    print("exits")
else:
    print("not exits")

    
