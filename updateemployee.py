import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
# from tkinter import ttk
# import employee

# global function for save
global usernameEnt
global firstnameEnt
global lastnameEnt
global addressEnt
global ageEnt
global passwordEnt
global root2

def clear():
    usernameEnt.delete(0,END)
    firstnameEnt.delete(0,END)
    lastnameEnt.delete(0,END)
    addressEnt.delete(0,END)
    ageEnt.delete(0,END)
    passwordEnt.delete(0,END)

def save():
    con = sqlite3.connect("EmployeeInfo.db")
    cur = con.cursor()
    record_id = employee.employeeID.get()
    cur.execute("""UPDATE employees SET
        UserName=:UserName,
        FirstName=:FirstName ,
        LastName=:LastName,
        Address=:Address ,
        Age=:Age ,
        Password=:Password

        WHERE oid = :oid""",
                {
                    'UserName': usernameEnt.get(),
                    'FirstName': firstnameEnt.get(),
                    'LastName': lastnameEnt.get(),
                    'Address': addressEnt.get(),
                    'Age': ageEnt.get(),
                    'Password': passwordEnt.get(),

                    'oid': record_id
                })
    con.commit()
    con.close()
    root2.destroy()
    pass

def updated():
    global root2
    root2 = Toplevel()
    root2.geometry("1366x768+60+10")
    root2.title("Update Employee")
    root2.resizable(0, 0)
    myimage2 = ImageTk.PhotoImage(Image.open('./images/update.png'))
    label1 = Label(root2, image=myimage2)
    label1.pack()

    # database
    con = sqlite3.connect("EmployeeInfo.db")
    cur = con.cursor()
    record_id = empmanagement.employeeID.get()
    cur.execute("SELECT  rowid, * FROM employees WHERE UserName = ?", (record_id,))
    rows = cur.fetchall()




    # desgin
    usernameEnt = Entry(root2)
    usernameEnt.place(relx=0.132, rely=0.296, width=374, height=30)
    usernameEnt.configure(relief="flat")

    # lastnameEnt
    lastnameEnt = Entry(root2)
    lastnameEnt.place(relx=0.132, rely=0.413, width=374, height=30)
    lastnameEnt.configure(relief="flat")

    # relx = 0.132, rely = 0.529, width = 374, height = 30

    # ageEnt
    ageEnt = Entry(root2)
    ageEnt.place(relx=0.132, rely=0.529, width=374, height=30)
    ageEnt.configure(relief="flat")

    # passwordEnt
    passwordEnt = Entry(root2)
    passwordEnt.place(relx=0.527, rely=0.529, width=374, height=30)
    passwordEnt.configure(relief="flat")

    # firstnameEnt
    firstnameEnt = Entry(root2)
    firstnameEnt.place(relx=0.527, rely=0.296, width=374, height=30)
    firstnameEnt.configure(relief="flat")

    # relx = 0.527, rely = 0.296, width = 374, height = 30

    # addressEnt
    addressEnt = Entry(root2)
    addressEnt.place(relx=0.527, rely=0.413, width=374, height=30)
    addressEnt.configure(relief="flat")


    SaveBTN = Button(root2, text="Save", relief="flat", command=empmanagement.save, fg="#ffffff", bg="#CF1E14")
    SaveBTN.place(relx=0.408, rely=0.836, width=96, height=34)
    SaveBTN.configure()

    clearBTN = Button(root2, text="Clear", relief="flat", command=clear, fg="#ffffff", bg="#CF1E14")
    clearBTN.place(relx=0.526, rely=0.836, width=86, height=34)
    clearBTN.configure()

    for row in rows:
        usernameEnt.insert(0, row[0])
        firstnameEnt.insert(0, row[1])
        lastnameEnt.insert(0, row[2])
        addressEnt.insert(0, row[3])
        ageEnt.insert(0, row[4])
        passwordEnt.insert(0, row[5])

    con.commit()
    con.close()

    root2.mainloop()