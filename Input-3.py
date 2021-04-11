from tkinter import *

root =Tk()

root.title("Information Form")

name = Label(root,text="Name :")
name.pack()
name1= Entry(root,borderwidth=2)
name1.pack()

def myName():
    n1=Label(root,text="My name is "+ name1.get())
    n1.pack()

age = Label(root,text="Age :")
age.pack()
age1= Entry(root,borderwidth=2)
age1.pack()

def myAge():
    a1=Label(root,text="My age is "+ age1.get())
    a1.pack()

add = Label(root,text="Address :")
add.pack()
add1= Entry(root,borderwidth=2)
add1.pack()

def myAdd():
    a2=Label(root,text="My address is " + add1.get())
    a2.pack()

mobile = Label(root,text="Mobile no. :")
mobile.pack()
mobile1= Entry(root,borderwidth=2)
mobile1.pack()

def mymobile():
    m1=Label(root,text="My mobile no is " + mobile1.get())
    m1.pack()

submit =Button(root,text="Submit information ",command=lambda:[myName(),myAge(),myAdd(),mymobile()])
submit.pack()

root.mainloop()
