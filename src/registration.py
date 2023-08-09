from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import student_db
from tkcalendar import DateEntry


class Register:
    def __init__(self,master):
        self.master = master
        self.master.geometry("600x500+400+100")
        self.master.title("Delcom Database")
        self.master.resizable(0,0)


        #==============================TEXT VARIABLES=============================
        self.name = StringVar()
        self.gender = StringVar()
        self.dob = StringVar()
        self.pob = StringVar()
        self.guard = StringVar()
        self.tel = StringVar()
        self.enroll = StringVar()
        self.health = StringVar()
        self.id = StringVar()
        self.id.set("COC/SC/23/001")


        def submit():
            if (len(self.guard.get())!=0):
                student_db.Insert(self.name.get(),self.gender.get(),self.dob.get(),self.pob.get(),self.guard.get(),self.tel.get(),self.enroll.get(),self.health.get(),self.id.get())
                reset()

            else:
                messagebox.showwarning("Entry error","Enter Credentials before submitting!!!")


        def reset():
            gen_id()
            self.gender.set("")
            self.dob.set("")
            self.id.set("")
            self.pob.set("")
            self.guard.set("")
            self.tel.set("")
            self.enroll.set("")
            self.health.set("")





        self.nav = Frame(self.master,width = 600,height = 50,bg = "blue",bd = 2)
        self.nav.pack()
        self.lbl_title = Label(self.nav,text = "Student Registration Form",font =("calibri",16,"bold"),bg = "blue",fg = "white")
        self.lbl_title.place(relx = 0.05,rely = 0.02)
        self.main = Frame(self.master,width = 600,height =450,bg = "white")
        self.main.pack()

        def gen_id():
            self.std_id_entry1.config(state='disabled', disabledbackground="blue", disabledforeground="white")
            self.rand_id = random.randint(100, 900)
            self.conv_id = ('DELCOM/GR/KKMA/' + str(self.rand_id))
            self.name.set(self.conv_id)
        self.std_id = Label(self.main,text = "Student ID",font = ("calibri",14),bg= "white")
        self.std_id.place(relx = 0.2,rely = 0.1)
        self.std_id_entry1= Entry(self.main,font = ("calibri",14),bd = 2,textvariable = self.name)
        self.std_id_entry1.place(relx = 0.1,rely = 0.16)
        gen_id()

        self.std_regno = Label(self.main, text="Student Name", font=("calibri", 14),bg = "white")
        self.std_regno.place(relx=0.2, rely=0.24)
        self.std_regno_entry = Entry(self.main, font=("calibri", 14),bd = 2,textvariable =self.gender)
        self.std_regno_entry.place(relx=0.1, rely=0.3)

        self.std_id = Label(self.main, text="Date of Birth", font=("calibri", 14), bg="white")
        self.std_id.place(relx=0.2, rely=0.37)
        self.std_id_entry = DateEntry(self.main, font=("calibri", 14),textvariable = self.dob,date_pattern = "dd-mm-yyyy",width = 18)
        self.std_id_entry.place(relx=0.1, rely=0.43)

        self.std_id = Label(self.main, text="Gender", font=("calibri", 14), bg="white")
        self.std_id.place(relx=0.2, rely=0.5)
        self.std_id_entry = ttk.Combobox(self.main, font=("calibri", 14),textvariable = self.pob,value= (
"Male","Female"),width=18)
        self.std_id_entry.place(relx=0.1, rely=0.56)
        


        self.std_id = Label(self.main, text="Parent Name", font=("calibri", 14), bg="white")
        self.std_id.place(relx=0.2, rely=0.63)
        self.std_id_entry = Entry(self.main, font=("calibri", 14), bd=2,textvariable = self.guard)
        self.std_id_entry.place(relx=0.1, rely=0.7)

        self.std_id = Label(self.main, text="Phone Number", font=("calibri", 14), bg="white",)
        self.std_id.place(relx=0.62, rely=0.49)
        self.std_id_entry = Entry(self.main, font=("calibri", 14), bd=2,textvariable = self.tel)
        self.std_id_entry.place(relx=0.62, rely=0.56)

        self.std_id = Label(self.main, text="Class Enrolled", font=("calibri", 14), bg="white")
        self.std_id.place(relx=0.62, rely=0.37)
        self.std_id_entry = ttk.Combobox(self.main, font=("calibri", 14),textvariable = self.enroll,value= (
            "Basic 1","Basic 2","Basic 3","Basic 4","Basic 5","Basic 6","Basic 7","Basic 8","Basic 9","Creche","Nursery","KG 1","KG 2",
        ),width = 18)
        self.std_id_entry.place(relx=0.62, rely=0.43)

        self.std_id = Label(self.main, text="Residence", font=("calibri", 14), bg="white")
        self.std_id.place(relx=0.62, rely=0.24)
        self.std_id_entry = Entry(self.main, font=("calibri", 14), bd=2,textvariable = self.health)
        self.std_id_entry.place(relx=0.62, rely=0.3)

        self.footer = Frame(self.main, width=600, height=10, bg="orange")
        self.footer.place(relx=0, rely=0)

        """self.passport_frame = Frame(self.main,width = 200,height = 200,bd = 2,relief=SUNKEN)
        self.passport_frame.place(relx = 0.63,rely = 0.1)"""

        """self.passport = Label(self.passport_frame)
        self.pass_pic = PhotoImage(file = "img/id_1.png")
        self.passport.config(image =self.pass_pic)
        self.passport.place(relx = 0,rely = 0)"""

        self.date1_reg = Label(self.main,text = "Registration Date",font=('calibri',14),bg = "white")
        self.date1_reg.place(relx = 0.62,rely = 0.1)
        self.date_reg_entry=DateEntry(self.main,font = ("calibri",14),bd = 2,width = 18,textvariable =self.id,date_pattern = "dd-mm-yyyy")
        self.date_reg_entry.place(relx = 0.62,rely = 0.16)
        # =========================================button========================================================
        self.button_submit = Button(self.main,text = "SUBMIT",font = ("calibri",15,"bold"),fg = "white",bg= "blue",command = submit,)
        self.button_submit.place(relx =0.1,rely =0.8)
        self.button_submit.config(width = 25)
        self.button_submit = Button(self.main, text="RESET", font=("calibri", 15, "bold"), fg="white", bg="red",command = reset)
        self.button_submit.place(relx=0.54, rely=0.8)
        self.button_submit.config(width=25)


        self.footer = Frame(self.main,width = 600,height = 37,bg = "blue")
        self.footer.place(relx =0,rely = 0.92)






master = Tk()
obj = Register(master)
master.mainloop()