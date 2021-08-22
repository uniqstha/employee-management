from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os
root=Tk()
root.geometry("1366x768+60+10")
root.resizable(0, 0)


global e1
global e2

def ok():
    uname=e1.get()
    password=e2.get()
    if(uname==""and password==""):
        messagebox.showinfo("","Blank Not Allowed")
    elif(uname=="employee"and password=="employee"):
        messagebox.showinfo("","Login Success")
        root.withdraw()
        os.system("empmanagement.py")
        root.deiconify()


    else:
        messagebox.showinfo("","Incorrect")




root.title("Login")
myimage=ImageTk.PhotoImage(Image.open('./images/login.png'))
Label(image=myimage).pack()
#e1 entry for username entry
e1=Entry(root,width=40,border=0,font=('Consolas',13))
e1.place(x=510,y=210)

#e2 entry for password entry
e2=Entry(root,width=40,border=0,show='*',font=('Consolas',13))
e2.place(x=510,y=300)

Button(root,text='LOGIN',font=('Consolas',20), padx=90,pady=10,cursor='hand2',
       border=0,bg="#6dcff6",activebackground="#6dcff6",command=ok).place(x=550,y=515)
root.mainloop()