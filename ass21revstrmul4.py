def string_check(data):
    if len(data)%4 == 0:
        return data[::-1]
    return data
text=input("enter string :")
result=string_check(text)
print("final string is :",result)
