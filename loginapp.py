import tkinter
import sqlite3
from tkinter import messagebox

def login():
    db=sqlite3.connect('login.sqlite')
    db.execute('CREATE TABLE IF NOT EXISTS LOGIN(username TEXT,password TEST)')
    #db.execute("INSERT INTO login(username, password) VALUES('admin', 'admin')")
    db.execute("INSERT INTO login(username, password) VALUES('Neelu', 'admin')")
    cursor=db.cursor()
    cursor.execute("SELECT * FROM login where username=? AND password=?", (userinput.get(), pass_input.get()))
    row=cursor.fetchone()
    if row:
        messagebox.showinfo('info', 'login success')
    else:
        messagebox.showinfo('info', 'login failed')
    cursor.connection.commit()
    db.close()

main_window=tkinter.Tk()
main_window.title('login app')
main_window.geometry('400x300')
user_input=tkinter.StringVar()
pass_input=tkinter.StringVar()

padd=20
main_window['padx']=padd
info_label=tkinter.Label(main_window, text='Login application')
info_label.grid(row=0,column=0)

info_user=tkinter.Label(main_window, text='username')
info_user.grid(row=1, column=0)
userinput=tkinter.Entry(main_window, textvariable=user_input)
userinput.grid(row=1, column=1)

info_pass=tkinter.Label(main_window, text='password')
info_pass.grid(row=2, column=0)
passinput=tkinter.Entry(main_window, textvariable=pass_input, show='*')
passinput.grid(row=2, column=1)

login_btn=tkinter.Button(main_window,text='Login', command=login)
login_btn.grid(row=3, column=1)
main_window.mainloop()

