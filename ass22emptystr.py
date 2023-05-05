def get_string(text):
    if len(text) < 2:
        return ""
    return text[-2:]
my_string = input("enter a string :")
print("new modified string is :",get_string(my_string))
