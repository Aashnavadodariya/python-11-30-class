from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="python_11_30",
        port="3306"
    )
#print(create_conn())
def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("insert status","all feilds are mendatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into student(fname,lname,email,mobile)values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("insert status","data inserted successfully")

def select_data():
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    if e_id.get()=="":
        msg.showinfo("serch status","id is mandatory for search")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_email.insert(0,i[3])
                e_mobile.insert(0,i[4])
        else:
             msg.showinfo("serch status","id not found")
        conn.close()
def update_data():
    if e_id.get()=="" or e_fname.get()=="" or e_email.get()=="" or e_mobile.get()=="" or e_lname.get()=="":
        msg.showinfo("update status","all feilds are mendatory")
    else:
        
        conn=conn.cursor()
        query="update student set fname=%s,lname=%s,email=%s,mobile=%s where id=%s"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("update status","data updated successfully")
    
   

        conn.close()
def delete_data():
    if e_id.get()=="":
        msg.showinfo("delete status","id is mendatory")
    else:
        
        conn=conn.cursor()
        query="delete from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("delete status","data deleted successfully")
        
root=Tk()
root.geometry("340x370")
root.title("Student Ragistration")
#root.resizable(width=False,height=False)

l_id=Label(root,text="ID",font=("ARIAL",10))
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME",font=("ARIAL",10))
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME",font=("ARIAL",10))
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL",font=("ARIAL",10))
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE",font=("ARIAL",10))
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("Arial",12),command=insert_data)
insert.place(x=80,y=320)

serch=Button(root,text="SERCH",bg="black",fg="white",font=("Arial",12),command=select_data)
serch.place(x=180,y=320)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("Arial",12),command=update_data)
update.place(x=80,y=390)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("Arial",12),command=delete_data)
delete.place(x=180,y=390)








