rno=int(input("enter roll no of the student :"))
rname=int(input("enter name of the student :"))
s1=int(input("enter marks of subject 1 :"))
s2=int(input("enter marks of subject 2 :"))
s3=int(input("enter marks of subject 3 :"))

total=s1+s2+s3
per=total/3

print("student name :",sname)
print("student rollno :",sno)
print("student total :",total)
print("percentage :",per)

if per>=70:
    print("distriction")
elif per>=60:
    print("first class")
elif per>=50:
    print("second class")
elif per>=40:
    print("pass class")
else:
    print("fail")
    

