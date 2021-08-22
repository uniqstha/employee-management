import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
# from tkinter import ttk


def insert():
    # database
    con = sqlite3.connect("EmployeeInfo.db")
    cur = con.cursor()
    cur.execute("INSERT INTO employees VALUES(:UserName,:FirstName, :LastName, :Address, :Age, :Password)",{
        'UserName': usernameEnt.get(),
        'FirstName': firstnameEnt.get(),
        'LastName': lastnameEnt.get(),
        'Address': addressEnt.get(),
        'Age': ageEnt.get(),
        'Password': passwordEnt.get()
    })
    messagebox.showinfo("Employee", "Inserted Sucessfully")

    con.commit()
    con.close()
    root1.destroy()

def clear():
    usernameEnt.delete(0,END)
    firstnameEnt.delete(0,END)
    lastnameEnt.delete(0,END)
    addressEnt.delete(0,END)
    ageEnt.delete(0,END)

def add():
    global root1
    root1 = Toplevel()
    root1.geometry("1366x768")
    root1.title("Add Employee")
    myimage1 = ImageTk.PhotoImage(Image.open('./images/add.png'))
    # bg = PhotoImage(file = "add_employee.png")
    label1 = Label(root1, image=myimage1)
    label1.pack()

    global usernameEnt
    global firstnameEnt
    global lastnameEnt
    global addressEnt
    global ageEnt
    global passwordEnt

    # desgin
    usernameEnt = Entry(root1)
    usernameEnt.place(relx=0.132, rely=0.296, width=374, height=30)
    usernameEnt.configure(relief="flat")

    # lastnameEnt
    lastnameEnt = Entry(root1)
    lastnameEnt.place(relx=0.132, rely=0.413, width=374, height=30)
    lastnameEnt.configure(relief="flat")

    # relx = 0.132, rely = 0.529, width = 374, height = 30

    # ageEnt
    ageEnt = Entry(root1)
    ageEnt.place(relx=0.132, rely=0.529, width=374, height=30)
    ageEnt.configure(relief="flat")

    # passwordEnt
    passwordEnt = Entry(root1)
    passwordEnt.place(relx=0.527, rely=0.529, width=374, height=30)
    passwordEnt.configure(relief="flat")

    # firstnameEnt
    firstnameEnt = Entry(root1)
    firstnameEnt.place(relx=0.527, rely=0.296, width=374, height=30)
    firstnameEnt.configure(relief="flat")

    # relx = 0.527, rely = 0.296, width = 374, height = 30

    # addressEnt
    addressEnt = Entry(root1)
    addressEnt.place(relx=0.527, rely=0.413, width=374, height=30)
    addressEnt.configure(relief="flat")


    addBTN = Button(root1, text="Add", relief="flat", command=insert, fg="#ffffff", bg="#CF1E14")
    addBTN.place(relx=0.408, rely=0.836, width=96, height=34)
    addBTN.configure()

    clearBTN = Button(root1, text="Clear", relief="flat", command=clear, fg="#ffffff", bg="#CF1E14")
    clearBTN.place(relx=0.526, rely=0.836, width=86, height=34)
    clearBTN.configure()



    root1.mainloop()