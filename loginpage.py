from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.geometry('1366x768')
root.title("Login")
myimage=ImageTk.PhotoImage(Image.open('login.png'))
Label(image=myimage).pack()
#e1 entry for username entry
e1=Entry(root,width=40,border=0,font=('Consolas',13))
e1.place(x=510,y=210)

#e2 entry for password entry
e2=Entry(root,width=40,border=0,show='*',font=('Consolas',13))
e2.place(x=510,y=300)

Button(root,text='LOGIN',padx=20,pady=10,border=0,bg="#D2463E",activebackground="#D2463E").place(x=640,y=525)
root.mainloop()