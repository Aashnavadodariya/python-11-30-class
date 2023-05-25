def uniqelst(dat1):
    x=[]
    for p in dat1:
        if p not in x:
            x.append(i)
    return x

datalist=[]
n=int(input("enter total element in a list "))
for k in range(n):
    dat=int(input("enter in data list :"))
    datalist.append(dat)

print("original list",datalist)
print(uniquelist(datalist))
