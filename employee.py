from tkinter import *
from PIL import Image,ImageTk
import os
import sqlite3
from tkinter import messagebox
import addemployee
from tkinter import ttk



root=Tk()
root.geometry("1366x768+60+10")
root.title("Login")
root.resizable(0, 0)



# # creating database
conn = sqlite3.connect("EmployeeInfo.db")
c = conn.cursor()
'''
c.execute("""CREATE TABLE employees(
        FullName text,
        Department text,
        Age integer,
        Gender text,
       Contact integer,
         Address text
 )""")
'''

# function
# ------------------------------------------
def save():
    global main

    conn = sqlite3.connect('EmployeeInfo.db')
    c = conn.cursor()
    record_id=employeeID.get()
    c.execute("""UPDATE employees SET
         FullName=:fullname,
         Department=:department,
         Age=:age,
         Gender=:gender,
         Contact=:contact,
         Address=:address
         WHERE oid =:oid""",
         {
         'fullname':fullname.get(),
         'department':department.get(),
         'age': age.get(),
         'gender': gender.get(),
         'contact':contact.get(),
         'address': address.get(),
         'oid': record_id
         })
    conn.commit()
    conn.close()
    employeeID.delete(0,END)
    main.destroy()
    os.system("employee.py")



def clear():
    fullname.delete(0,END)
    department.delete(0,END)
    age.delete(0,END)
    gender.delete(0,END)
    contact.delete(0,END)
    address.delete(0, END)

def update():
    root.withdraw()
    global my_img
    global main
    main = Toplevel()
    main.geometry("1366x768+60+10")
    main.title("Login")
    main.resizable(0, 0)

    conn = sqlite3.connect('EmployeeInfo.db')
    c = conn.cursor()
    record_id = employeeID.get()
    c.execute("SELECT*from employees WHERE oid = " + record_id)
    records = c.fetchall()
    global fullname
    global department
    global age
    global gender
    global contact
    global address

    my_img = ImageTk.PhotoImage(Image.open('images/update.png'))
    my_label=Label(main,image=my_img).pack()
    fullname_lbl = Label(main, text="Full Name", font=('Consolas', 15), bg="white")
    fullname_lbl.place(x=180, y=200)
    department_lbl = Label(main, text="Department", font=('Consolas', 15), bg="white")
    department_lbl.place(x=720, y=200)
    age_lbl = Label(main, text="Age", font=('Consolas', 15), bg="white")
    age_lbl.place(x=180, y=290)
    gender_lbl = Label(main, text="Gender", font=('Consolas', 15), bg="white")
    gender_lbl.place(x=720, y=290)
    contact_lbl = Label(main, text="Contact", font=('Consolas', 15), bg="white")
    contact_lbl.place(x=180, y=380)
    address_lbl = Label(main, text="Address", font=('Consolas', 15), bg="white")
    address_lbl.place(x=720, y=380)

    fullname = Entry(main, width=25, border=0, font=('Consolas', 15))
    fullname.place(x=180, y=230)
    department = Entry(main, width=25, border=0, font=('Consolas', 15))
    department.place(x=720, y=230)
    age = Entry(main, width=25, border=0, font=('Consolas', 15))
    age.place(x=180, y=320)
    gender = Entry(main, width=25, border=0, font=('Consolas', 15))
    gender.place(x=720, y=320)
    contact = Entry(main, width=25, border=0, font=('Consolas', 15))
    contact.place(x=180, y=410)
    address = Entry(main, width=25, border=0, font=('Consolas', 15))
    address.place(x=720, y=410)
    for record in records:
        fullname.insert(0, record[0])
        department.insert(0, record[1])
        age.insert(0, record[2])
        gender.insert(0, record[3])
        contact.insert(0, record[4])
        address.insert(0, record[5])
    update_btn = Button(main, text="UPDATE", font=('Consolas', 15), cursor='hand2',
                     bg="#00bff3", border=0, activebackground="#00bff3", padx=20, pady=10,command=save)
    update_btn.place(x=550, y=630)
    clear_btn = Button(main, text="CLEAR", font=('Consolas', 15), cursor='hand2',
                       bg="#00bff3", border=0, activebackground="#00bff3", padx=25, pady=10,command=clear)
    clear_btn.place(x=715, y=630)




def search():
    # my_tree.delete(0, END)
    my_tree.delete(*my_tree.get_children())
    conn = sqlite3.connect("EmployeeInfo.db")
    c = conn.cursor()
    record_id = employeeID.get()
    c.execute("SELECT *,oid FROM employees WHERE FullName = ?", (record_id,))
    records= c.fetchall()
    # for data in rows.get_children():
    print(records)

    for record in records:
        my_tree.insert('', 'end', values=(record))


    conn.commit()
    conn.close()
    # pass

def logout():
    root.withdraw()
    os.system("main.py")

def adding():
    root.withdraw()

    addemployee.add()







def Exit():
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=root)
    if sure == True:
        root.destroy()




# desgin
# -------------------------------------

# image
myimage=ImageTk.PhotoImage(Image.open('./images/empmanagement.png'))
Label(image=myimage).pack()

# label
id_lbl=Label(root,text="Employee ID",font=('Consolas',13),bg="white")
id_lbl.place(x=120,y=190)
option_lbl=Label(root,text="Employee Option",font=('Consolas',13),bg="white")
option_lbl.place(x=155,y=290)

# entry
employeeID=Entry(root,width=25,border=0,font=('Consolas',13))
employeeID.place(x=60,y=220)
# entryID = employeeID.get()



# buttons
logoutBTN=Button(root,text="LOG OUT",font=('Consolas',13),cursor='hand2',
                  bg="#687afd",border=0,activebackground="#687afd",padx=16,command = logout)
logoutBTN.place(x=1218,y=49)

searchBTN=Button(root,text="Search",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",command = search)
searchBTN.place(x=316,y=218)

addEmpBTN=Button(root,text="ADD EMPLOYEE",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=90,command=adding)
addEmpBTN.place(x=75,y=330)

updateBTN=Button(root,text="UPDATE EMPLOYEE",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=85, command = update)
updateBTN.place(x=65,y=380)



# delete_btn=Button(root,text="DELETE EMPLOYEE",font=('Consolas',13),cursor='hand2',
#                   bg="#00bff3",border=0,activebackground="#00bff3",padx=85)
# delete_btn.place(x=65,y=435)

exitBTN =Button(root,text="EXIT",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=16,command = exit)
exitBTN .place(x=185,y=675)

# Scrollbar
scrollbarx = Scrollbar(root, orient=HORIZONTAL)
scrollbary = Scrollbar(root, orient=VERTICAL)

# tree

c.execute('SELECT * ,oid from employees')
records = c.fetchall()
my_tree = ttk.Treeview(root)
my_tree['columns'] = ("FullName", "Department", "Age","Gender", "Contact","Address")

my_tree.column("#0", width =0, stretch=NO)
my_tree.column("FullName", anchor=W,width=150)
my_tree.column("Department", anchor=W,width=120)
my_tree.column("Age", anchor=W,width=40)
my_tree.column("Gender", anchor=W,width=90)
my_tree.column("Contact", anchor=W,width=100)
my_tree.column("Address", anchor=W,width=100)

my_tree.heading("#0", text = "", anchor = W)
my_tree.heading("FullName", text = "FullName", anchor = W)
my_tree.heading("Department", text = "Department", anchor = W)
my_tree.heading("Age", text = "Age", anchor = W)
my_tree.heading("Gender", text = "Gender", anchor = W)
my_tree.heading("Contact", text = "Contact", anchor = W)
my_tree.heading("Address",text = "Address", anchor = W)

my_tree.place(relx=0.307, rely=0.203, width=880, height=550)
my_tree.configure(yscrollcommand= scrollbary.set, xscrollcommand = scrollbarx.set)
# Scrollbar
scrollbarx.configure(command=my_tree.xview)
scrollbary.configure(command=my_tree.yview)
scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

count=0
for record in records:
    my_tree.insert(parent='',index='end',iid=count,text="Parent",values=(record[0],record[1],record[2],record[3],record[4],record[5]))
    count+=1
conn.commit()
conn.close()
root.mainloop()