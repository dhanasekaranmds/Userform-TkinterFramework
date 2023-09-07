import sys
from tkinter import *
from tkinter import messagebox
from tokenize import Name

# import contact as contact
import pymysql

top=Tk()
top.title("dhanasekaran")
top.geometry('500x400')
to=pymysql.connect(host="localhost", user="root", password="", database="sns")
def data():
    email=e1.get()
    password=e2.get()
    if(email==""):
        messagebox.showinfo("Alert","Enter the username")
    elif(password==""):
        messagebox.showinfo("Alert", "Enter the password")
    else:
        sql="select * from user_details where email='"+email+"' and password='"+password+"'"
        cursor = to.cursor()
        cursor.execute(sql)
        myresult = cursor.fetchall()
        if (myresult):
            messagebox.showinfo('Alert', 'SUCCESS')
        else:
            msg=messagebox.showinfo('Failed,"Log In Failed')



l1=Label(top,text="Login page")
l1.place(x=130,y=50)
l2=Label(top,text="email")
l2.place(x=100,y=80)
e1=Entry(top)
e1.place(x=170,y=80)
l3=Label(top,text="password")
l3.place(x=100,y=110)
e2=Entry(top)
e2.place(x=170,y=110)
b1=Button(top,text="Login",command=data)
b1.place(x=170,y=150)
top.mainloop()