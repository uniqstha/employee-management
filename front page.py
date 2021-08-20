import os
from tkinter import *
from tkinter import messagebox

main = Tk()
main.geometry("1366x768")
main.title("LOGIN")
main.resizable(0, 0)


def Exit():
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()


main.protocol("WM_DELETE_WINDOW", Exit)


def emp():
    main.withdraw()
    os.system("login.py")
    main.deiconify()




label1 = Label(main)
label1.place(relx=0, rely=0, width=1366, height=768)
img = PhotoImage(file="./loginas.png")
label1.configure(image=img)

button1 = Button(main,command=emp)
button1.place(x=430,y=330, width=146, height=90)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="./employee_icon.png")
button1.configure(image=img2)
Label(main,text='EMPLOYEE',bg='white',font=('Consolas',15)).place(x=455,y=410)


button2 = Button(main)
button2.place(x=774,y=330, width=146, height=100)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="./admin_icon.png")
button2.configure(image=img3)
Label(main,text='ADMIN',bg='white',font=('Consolas',15)).place(x=815,y=410)


main.mainloop()
