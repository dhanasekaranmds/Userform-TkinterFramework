from tkinter import *
from tkinter import messagebox
from tokenize import Name

import of as of
import pymysql
from tkinter import messagebox

top=Tk()
top.title("dhanasekaran")
top.geometry('500x400')
to=pymysql.Connect(host="localhost",user="root",password="",database="mds")
def data():
    Name=e1.get()
    Department=e2.get()
    Percentage=e3.get()
    Year=e4.get()
    contact=e5.get()
    cursor=to.cursor()
    sql="insert into sekaran values('"+Name+"','"+Department+"','"+Percentage+"','"+Year+ "','" + contact + "')"
    cursor.execute(sql)
    to.commit()
    messagebox.showinfo('Success',"Registered Successfully")

l1=Label(top,text="Registration form",font=('times',20,'bold'))
l1.place(x=150,y=30)
l2=Label(top,text="Name")
l2.place(x=100,y=80)
e1=Entry(top)
e1.place(x=250,y=80)
l3=Label(top,text="Department")
l3.place(x=100,y=110)
e2=Entry(top)
e2.place(x=250,y=110)
l4=Label(top,text="Percentage")
l4.place(x=100,y=140)
e3=Entry(top)
e3.place(x=250,y=140)
l5=Label(top,text="Year")
l5.place(x=100,y=170)
e4=Entry(top)
e4.place(x=250,y=170)
l6=Label(top,text="contact")
l6.place(x=100,y=200)
e5=Entry(top)
e5.place(x=250,y=200)
b1=Button(top,text="Register",command=data)
b1.place(x=250,y=250)
top.mainloop()




