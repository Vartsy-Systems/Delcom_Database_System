import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
from PIL import Image, ImageTk


class UserLogin:
    def __init__(self,master):
        self.master = master
        self.master.geometry("950x700+200+0")
        self.master.resizable(0,0)
        self.master.title("Delcom Management System")

        #=========================================functions=====================================================
        self.user = StringVar()
        self.passwd = StringVar()

        def login():
            if self.user.get()=="Delcom" and self.passwd.get()=="Delcom123":
                master.destroy()
                os.system("python index.py")

            elif self.user.get()=="" and self.passwd.get()=="":
                messagebox.showerror("invalid credential","Please Enter Correct Credentials")

            else:
                messagebox.showerror("Login unsuccessful","Incorrect Password and Username")


        



        self.nav_frame = Frame(self.master,width = 950,height = 60,bg = "blue")
        self.nav_frame.pack()
        self.title = Label(self.nav_frame,text ="ADMIN LOGIN SYSTEM", fg = "white",bg = "blue",font = ("calibri",15,"bold"))
        self.title.place(relx = 0,rely = 0.3)
        



        def Time():
            hour = time.strftime("%H")
            minutes = time.strftime("%M")
            seconds = time.strftime("%S")
            day = time.strftime("%A")
            am_pm = time.strftime("%p")

            self.timelabel.config(text = day + " "+ hour + " : "+minutes + " : "+seconds + " "+am_pm)
            self.timelabel.after(1000,Time)


        self.timelabel =Label(self.nav_frame,text = "",font= ("calibri",14,"bold"),bg = "blue",fg = "white")
        self.timelabel.place(relx = 0.77,rely = 0.3)
        Time()
        

        self.main_frame = Frame(self.master,width = 950,height= 700,bg = "white" )
        self.main_frame.pack()
        self.login_f = Frame(self.main_frame,width = 300,height = 450,bd = 2,relief = RAISED,bg = "white")
        self.footer = Frame(self.main_frame,width =950,height = 30,bg ="blue")
        self.footer.place(relx = 0,rely = 0.96)
        self.login_f.place(relx = 0.34,rely = 0.05)

        self.avatar = Label(self.login_f,bg = "white")
        self.logo = Image.open("img/avatar.png")
        resized_image = self.logo.resize((100, 100))
        self.limg = ImageTk.PhotoImage(resized_image)
        #self.avatar = Label(self.login_f,bg ="white")
        #self.ava = PhotoImage(file = "img/avatar.png")
        #self.ava = self.ava.resize((80, 80))
        self.avatar.config(image =self.limg)
        self.avatar.place(relx= 0.3,rely =0.05)
       
    #============================================username and password ===============================================
        self.username = Label(self.login_f,text = "Username",font = ("calibri",14,"bold"),bg = "white",fg = "blue")
        self.username.place(relx = 0.35,rely = 0.37)
        self.username_entry = Entry(self.login_f,width =23,font = ("calibri",14),bd = 2,textvariable = self.user)
        self.username_entry.place(relx = 0.1,rely =0.46)

        self.password = Label(self.login_f, text="Password", font=("calibri", 14, "bold"), bg="white", fg="blue")
        self.password.place(relx=0.35, rely=0.55)
        self.password_entry = Entry(self.login_f, width=23, font=("calibri", 14), bd=2,show = "*",textvariable =self.passwd)
        self.password_entry.place(relx=0.1, rely=0.62)
        
        self.login_btn = Button(self.login_f,text = "Login",font = ("calibri",15,"bold"),bg ="purple",fg = "white")
        self.login_btn.place(relx = 0.1,rely = 0.75)
        self.login_btn.config(width = 23,command = login)

        

master = Tk()
obj = UserLogin(master)
master.mainloop()