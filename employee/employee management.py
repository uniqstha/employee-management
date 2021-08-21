from tkinter import *
from PIL import Image,ImageTk


root=Tk()
root.geometry("1366x768")
root.title("Login")
myimage=ImageTk.PhotoImage(Image.open('empmanagement.png'))
Label(image=myimage).pack()
id_lbl=Label(root,text="Employee ID",font=('Consolas',13),bg="white")
id_lbl.place(x=120,y=200)
option_lbl=Label(root,text="Employee Option",font=('Consolas',13),bg="white")
option_lbl.place(x=155,y=290)
id_entry=Entry(root,width=25,border=0,font=('Consolas',13))
id_entry.place(x=250,y=260)
logout_btn=Button(root,text="LOG OUT",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3")
logout_btn.place(x=50,y=75)
search_btn=Button(root,text="Search",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3")
search_btn.place(x=316,y=218)
add_btn=Button(root,text="ADD EMPLOYEE",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=90)
add_btn.place(x=75,y=330)
update_btn=Button(root,text="UPDATE EMPLOYEE",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=85)
update_btn.place(x=65,y=380)
delete_btn=Button(root,text="DELETE EMPLOYEE",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=85)
delete_btn.place(x=65,y=435)
exit_btn=Button(root,text="EXIT",font=('Consolas',13),cursor='hand2',
                  bg="#00bff3",border=0,activebackground="#00bff3",padx=16)
exit_btn.place(x=185,y=675)


root.mainloop()