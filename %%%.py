from tkinter import *
from tkinter import messagebox

import pymysql

top=Tk()
top.title("dhanasekaran")
top.geometry('500x400')
to=pymysql.connect(host="localhost", user="root", password="", database="sns")
def data():
    name=e1.get()
    cursor = to.cursor()
    sql = "delete from user_details where name='"+name+"'"
    # print(sql)
    cursor.execute(sql)
    to.commit()
    messagebox.showinfo('delete', 'Successfully deleted')
l1=Label(top,text="Delete")
l1.place(x=150,y=50)
l2=Label(top,text="Name")
l2.place(x=100,y=100)
e1=Entry(top)
e1.place(x=200,y=100)
b1=Button(top,text="Delete",command=data)
b1.place(x=200,y=150)
top.mainloop()