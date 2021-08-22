# from tkinter import *
# from PIL import Image,ImageTk
# import os
# import addemployee
#
#
# root=Tk()
# root.geometry("1366x768+60+10")
# root.title("Login")
# root.resizable(0, 0)
#
#
# myimage=ImageTk.PhotoImage(Image.open('empmanagement.png'))
# Label(image=myimage).pack()
# id_lbl=Label(root,text="Employee ID",font=('Consolas',13),bg="white")
# id_lbl.place(x=120,y=200)
# option_lbl=Label(root,text="Employee Option",font=('Consolas',13),bg="white")
# option_lbl.place(x=155,y=290)
# id_entry=Entry(root,width=25,border=0,font=('Consolas',13))
# id_entry.place(x=60,y=220)
# logout_btn=Button(root,text="LOG OUT",font=('Consolas',13),cursor='hand2',
#                   bg="#00bff3",border=0,activebackground="#00bff3")
# logout_btn.place(x=50,y=75)
# search_btn=Button(root,text="Search",font=('Consolas',13),cursor='hand2',
#                   bg="#00bff3",border=0,activebackground="#00bff3")
# search_btn.place(x=316,y=218)
# add_btn=Button(root,text="ADD EMPLOYEE",font=('Consolas',13),cursor='hand2',
#                   bg="#00bff3",border=0,activebackground="#00bff3",padx=90)
# add_btn.place(x=75,y=330)
# update_btn=Button(root,text="UPDATE EMPLOYEE",font=('Consolas',13),cursor='hand2',
#                   bg="#00bff3",border=0,activebackground="#00bff3",padx=85)
# update_btn.place(x=65,y=380)
# # delete_btn=Button(root,text="DELETE EMPLOYEE",font=('Consolas',13),cursor='hand2',
# #                   bg="#00bff3",border=0,activebackground="#00bff3",padx=85)
# # delete_btn.place(x=65,y=435)
# exit_btn=Button(root,text="EXIT",font=('Consolas',13),cursor='hand2',
#                   bg="#00bff3",border=0,activebackground="#00bff3",padx=16)
# exit_btn.place(x=185,y=675)
#
#
# root.mainloop()

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
con = sqlite3.connect("EmployeeInfo.db")
cur = con.cursor()

# cur.execute("""CREATE TABLE employees(
#
#         UserName text,
#
#         FirstName text,
#
#         LastName text,
#
#         Address text,
#
#        Age integer
#
#
#
#  )""")

# function
# ------------------------------------------


def search():
    # my_tree.delete(0, END)
    my_tree.delete(*my_tree.get_children())
    con = sqlite3.connect("EmployeeInfo.db")
    cur = con.cursor()
    record_id = employeeID.get()
    cur.execute("SELECT  rowid, * FROM employees WHERE UserName = ?", (record_id,))
    rows = cur.fetchall()
    # for data in rows.get_children():

    for data in rows:
        my_tree.insert('', 'end', values=(data))


    con.commit()
    con.close()
    # pass

def logout():
    root.withdraw()
    os.system("front_page.py")

def adding():
    addemployee.add()

def update():
    root.withdraw()
    os.system("updateemployee.py")



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
my_tree = ttk.Treeview(root)
my_tree['columns'] = ("UserName", "First Name", "Last Name", "Address", "Age")

# my_tree.column("#0", width = 120, minwidth = 25)
my_tree.column("#0", stretch=NO, minwidth=0, width=0)
my_tree.column("#1", stretch=NO, minwidth=0, width=80)
my_tree.column("#2", stretch=NO, minwidth=0, width=260)
my_tree.column("#3", stretch=NO, minwidth=0, width=100)
my_tree.column("#4", stretch=NO, minwidth=0, width=198)
my_tree.column("#5", stretch=NO, minwidth=0, width=80)

# my_tree.heading("#0", text = "", anchor = W)
my_tree.heading("UserName", text = "Username", anchor = W)
my_tree.heading("First Name", text = "First name", anchor = W)
my_tree.heading("Last Name", text = "Last name", anchor = W)
my_tree.heading("Address", text = "Address", anchor = W)
my_tree.heading("Age", text = "Age", anchor = W)

my_tree.place(relx=0.307, rely=0.203, width=880, height=550)
my_tree.configure(yscrollcommand= scrollbary.set, xscrollcommand = scrollbarx.set)

# Scrollbar
scrollbarx.configure(command=my_tree.xview)
scrollbary.configure(command=my_tree.yview)

scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)
cur.execute("SELECT * FROM employees")
fetch = cur.fetchall()
for data in fetch:
    my_tree.insert("", "end", values=(data))

root.mainloop()