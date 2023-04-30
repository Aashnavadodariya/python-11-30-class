import random
#print(random.randint(1000,9999))
#print(random.choice([1,2,"tops","python",10,100,true]))

l=[]
lucky=[]
for i in range(1,101):
    l.append(i)
for i in range(10):
    num=random.choice(l)
    lucky.append(num)
print(l)
print(lucky)
