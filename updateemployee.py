import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
# from tkinter import ttk
root=Tk()
root.geometry("1366x768+60+10")
root.title("Login")
root.resizable(0, 0)
myimage=ImageTk.PhotoImage(Image.open('./images/update.png'))
Label(image=myimage).pack()
fullname_lbl=Label(root,text="Full Name",font=('Consolas',15),bg="white")
fullname_lbl.place(x=180,y=200)
department_lbl=Label(root,text="Department",font=('Consolas',15),bg="white")
department_lbl.place(x=720,y=200)
age_lbl=Label(root,text="Age",font=('Consolas',15),bg="white")
age_lbl.place(x=180,y=290)
gender_lbl=Label(root,text="Gender",font=('Consolas',15),bg="white")
gender_lbl.place(x=720,y=290)
contact_lbl=Label(root,text="Contact",font=('Consolas',15),bg="white")
contact_lbl.place(x=180,y=380)
address_lbl=Label(root,text="Address",font=('Consolas',15),bg="white")
address_lbl.place(x=720,y=380)

fullname_entry=Entry(root,width=25,border=0,font=('Consolas',15))
fullname_entry.place(x=180,y=230)
department_entry=Entry(root,width=25,border=0,font=('Consolas',15))
department_entry.place(x=720,y=230)
age_entry=Entry(root,width=25,border=0,font=('Consolas',15))
age_entry.place(x=180,y=320)
gender_entry=Entry(root,width=25,border=0,font=('Consolas',15))
gender_entry.place(x=720,y=320)
contact_entry=Entry(root,width=25,border=0,font=('Consolas',15))
contact_entry.place(x=180,y=410)
email_entry=Entry(root,width=25,border=0,font=('Consolas',15))
email_entry.place(x=720,y=410)
add_btn=Button(root,text="ADD",font=('Consolas',15),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=25,pady=10)
add_btn.place(x=560,y=630)
clear_btn=Button(root,text="CLEAR",font=('Consolas',15),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=25,pady=10)
clear_btn.place(x=715,y=630)
root.mainloop()