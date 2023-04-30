s=input("enter string :")
space=0
digit=0
alpha=0

for i in s:
    if i.isspace():
        space=space+1
    elif i.isdigit():
        digit+=1
    elif i.isalpha():
        alpha+=1
    else:
            special+=1
print("total alphabets :",alpha)
print("total digit :",digit)
print("total space :",space)
print("tota special charcter :",special)
