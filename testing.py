from tkinter import*
from tkinter import messagebox
import ast
import os
import hashlib
import csv


root=Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.resizable(False,False)

def login():
    username=code.get()
    password=user.get()

    hash1 = hashlib.sha256(username.encode('utf_8')).hexdigest()
    hash2 = hashlib.sha256(password.encode('utf_8')).hexdigest()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)

    file.close()
    print(hash1,hash2)




    # print(r.keys())
    # print(r.values())

    if username in r.keys()and password==r[username]:
        messagebox.showinfo('Log In', 'Sucessfully logged into the system')
        screen=Toplevel(root)
        screen.title("Main Page")
        screen.geometry("925x500+300+200")

        def letsee():

            Month = 'december'

            file = f"hsbc_{Month}.csv"
            transactions = []
            subs_name = {''}
            sum = 0

            # def hsbcFin(file,subs_name):
            with open(file, mode='r') as csv_file:

                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    date = row[0]
                    name = row[1]
                    category = 'other'
                    if name == 'H3G DD':
                        category = 'Phone Bill'
                    if name in subs_name:
                        category = 'Subscriptions'

                    transaction = ((date, name, category))

                    print(transaction)
                    transactions.append(transaction)

        def home_page():
            home_frame = Frame(main_frame)
            lbl = Label(home_frame, text='Home Page \n\nPage : 1 ', font=("Bold", 30))
            lbl.pack()
            home_frame.pack(pady=20)

        def about_page():
            about_frame = Frame(main_frame)
            lbl = Label(about_frame, text='About \n\nPage : 1 ', font=("Bold", 30))
            lbl.pack()
            about_frame.pack(pady=20)

        def acc_page():
            acc_frame = Frame(main_frame)
            lbl = Label(acc_frame, text='Account Information \n\nPage : 1 ', font=("Bold", 30))
            lbl.pack()
            sewy = Button(acc_frame, text='Click Here to see your Account Details')
            sewy.pack()
            acc_frame.pack(pady=20)

        def tran_page():
            tran_frame = Frame(main_frame)
            lbl = Label(tran_frame, text='Transactions \n\n ', font=("Bold", 30))

            def on_enter(e):
                user1.delete(0, 'end')

            def on_leave(e):
                if user1.get() == '':
                    user1.insert()

            user1 = Entry(tran_frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
            user1.place(x=30, y=160)
            user1.insert(0, 'Password')
            user1.bind("<FocusIn>", on_enter)
            user1.bind("<FocusOut>", on_leave)

            Frame(tran_frame, width=295, height=2, bg='black').place(x=25, y=187)
            trs = Button(tran_frame, text='Show Transactions', command=letsee)
            trs.pack()
            tran_frame.pack(pady=20)
            lbl.pack()
            tran_frame.pack(pady=20)

        def hide_indicators():
            home_indicate.config(bg='#c3c3c3')
            about_indicate.config(bg='#c3c3c3')
            acc_indicate.config(bg='#c3c3c3')
            tran_indicate.config(bg='#c3c3c3')

        def exite():
            messagebox.showinfo('Log Out', 'Sucessfully logged out of the system')
            screen.destroy()

        def delete_pages():
            for frame in main_frame.winfo_children():
                frame.destroy()



        def indicate(lb, page):
            hide_indicators()
            lb.config(bg='#158aff')

            delete_pages()
            page()

        options_frame = Frame(screen, bg='grey')

        home_btn = Button(options_frame, text='Home', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3',
                          command=lambda: indicate(home_indicate, home_page))
        home_btn.place(x=10, y=50)

        home_indicate = Label(options_frame, text='', bg='#c3c3c3')
        home_indicate.place(x=3, y=50, width=5, height=40)

        about_btn = Button(options_frame, text='About', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3',
                           command=lambda: indicate(about_indicate, about_page))
        about_btn.place(x=10, y=110)
        about_indicate = Label(options_frame, text='', bg='#c3c3c3')
        about_indicate.place(x=3, y=110, width=5, height=40)

        acc_btn = Button(options_frame, text='Account Info', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3',
                         command=lambda: indicate(acc_indicate, acc_page))
        acc_btn.place(x=10, y=170)
        acc_indicate = Label(options_frame, text='', bg='#c3c3c3')
        acc_indicate.place(x=3, y=170, width=5, height=40)

        tran_btn = Button(options_frame, text='Transactions', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3',
                          command=lambda: indicate(tran_indicate, tran_page))
        tran_btn.place(x=10, y=230)
        tran_indicate = Label(options_frame, text='', bg='#c3c3c3')
        tran_indicate.place(x=3, y=230, width=5, height=40)

        logout_btn = Button(options_frame, text='Log Out', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3',
                            command=lambda: indicate(logout_indicate,exite))
        logout_btn.place(x=10, y=290)
        logout_indicate = Label(options_frame, text='', bg='#c3c3c3')
        logout_indicate.place(x=3, y=290, width=5, height=40)

        options_frame.pack(side=LEFT)
        options_frame.pack_propagate(False)
        options_frame.configure(width=180, height=500)

        main_frame = Frame(screen, highlightbackground='black', highlightthickness=2)
        main_frame.pack(side=LEFT)
        main_frame.pack_propagate(False)
        main_frame.configure(height=900, width=500)





        



        screen.mainloop()

    else:
        messagebox.showerror('Invalid','Its either you have entered the wrong password or username')
#########################################################################################
def signup_command():
    window=Toplevel(root)
    window.title("Sign UP")
    window.wm_geometry("925x500+300+200")
    window.configure(bg='#fff')
    window.resizable(False, False)

    def signup():
        username = code.get()
        password = user.get()
        conf1rm = cnfirm.get()

        has = hashlib.sha256(username.encode('utf_8')).hexdigest()
        has2 = hashlib.sha256(password.encode('utf_8')).hexdigest()
        has3 = hashlib.sha256(conf1rm.encode('utf_8')).hexdigest()

        if has2 == has3:
            try:
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('datasheet.txt', 'w')
                w = file.write(str(r))

                messagebox.showinfo('Sign Up', 'Sucessfully sign up')
                window.destroy()

            except:
                file = open('datasheet.txt', 'w')
                pp = str({'Username': 'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid', 'Both Password should match')

    def sign():
        window.destroy()

    '''img =PhotoImage(file='dragon-ball-z-fashion-header.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=90)'''

    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft Yahei Ui', 23, 'bold'))
    heading.place(x=100, y=5)

    ####-------------------

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        if code.get() == '':
            code.insert()

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    code.place(x=30, y=80)
    code.insert(0, 'Username')
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert()

    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=160)
    user.insert(0, 'Password')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=187)

    def on_enter(e):
        cnfirm.delete(0, 'end')

    def on_leave(e):
        if cnfirm.get() == '':
            cnfirm.insert()

    cnfirm = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    cnfirm.place(x=30, y=240)
    cnfirm.insert(0, 'Confirm Password')
    cnfirm.bind("<FocusIn>", on_enter)
    cnfirm.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=267)

    ####------------

    Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35,
                                                                                                              y=297)
    label = Label(frame, text='Already have an Account?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=90, y=340)

    login = Button(frame, width=6, text='Sign Up', bg='white', fg='#57a1f8', cursor='hand2', border=0, command=sign)
    login.place(x=200, y=340)

    window.mainloop()
 ##################################################################################################
    '''img =PhotoImage(file='dragon-ball-z-fashion-header.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=90)'''


    heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft Yahei Ui', 23, 'bold'))
    heading.place(x=100, y=5)


frame=Frame(root,width=350,height=390,bg='#fff')
frame.place(x=480,y=50)

heading=Label(frame,text='Sign Up',fg='#57a1f8',bg='white',font=('Microsoft Yahei Ui',23,'bold'))
heading.place(x=100,y=5)


####-------------------

def on_ent(e):
    code.delete(0,'end')

def on_lea(e) :
    if code.get()=='':
        code.insert()

code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=80)
code.insert(0,'Username')
code.bind("<FocusIn>",on_ent)
code.bind("<FocusOut>",on_lea)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    user.delete(0,'end')

def on_leave(e) :
    name=user.get()
    if name=='':
        user.insert()

user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=160)
user.insert(0,'Password')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=187)



Button(frame,width=30,pady=7,text='Sign In',bg='#57a1f8',fg='white',cursor='hand2',border=0,command= login).place(x=35,y=210)

label=Label(frame,text="Don't have an Account?",fg='black',bg='white',cursor='hand2',font=('Calibre',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)





root.mainloop()
