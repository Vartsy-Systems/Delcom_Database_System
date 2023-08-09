import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os,sqlite3,student_db
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#====================================================set school window=================================================
class schoolMain:
    def __init__(self,master):
        self.master = master
        self.master.geometry("1350x750+22+0")
        self.master.resizable(0,0)
        self.master.config(bg="white")
        self.master.title("Pentecost Int. ICT Department")


        #======================================================functions===========================


#====================================================set content frames================================================
        self.master_frame=Frame(self.master,width=1350,height=750,bg="white")
        self.master_frame.pack()
        self.nave_frame = Frame(self.master_frame,width= 1350,height = 85,bg = 'blue')
        self.nave_frame.pack()
        """self.brand_logo = Label(self.nave_frame,bg = "white")
        self.logo1 = PhotoImage(file="img/lol.png")
        self.brand_logo.config(image=self.logo1)
        self.brand_logo.place(relx=0.156, rely=0.14)"""

        self.side_nave =Frame(self.master_frame,width = 350,height = 750,bg = 'white',bd = 3,relief = RAISED)
        self.side_nave.pack(side=LEFT)
#===================================================================buttons for side navigation===========================================
        self.add_new = Button(self.side_nave,bg = "white",bd = 0)
        self.image = PhotoImage(file="img/new.png")
        self.add_new.config(image=self.image)
        self.add_new_label = Button(self.side_nave,text = "Add Staff",font = ("calibri",18,"bold"),bg = "white",fg = "blue",bd = 0,command = 'addNew')
        self.add_new_label.place(relx = 0.19,rely = 0.29)
        self.add_new.place(relx = 0.1,rely = 0.3)

        self.offer = Button(self.side_nave, bg="white", bd=0)
        self.image1 = PhotoImage(file="img/offer.png")
        self.offer.config(image=self.image1)
        self.add_offer_label = Button(self.side_nave, text="Salary & Allowance", font=("calibri", 18, "bold"), bg="white",
                                    fg="blue", bd=0,command ='fees' )
        self.add_offer_label.place(relx=0.19, rely=0.39)
        self.offer.place(relx=0.1, rely=0.4)

        self.add_new = Button(self.side_nave, bg="white", bd=0)
        self.image2 = PhotoImage(file="img/attend.png")
        self.add_new.config(image=self.image2)
        self.add_new_label = Button(self.side_nave, text="Staff Data", font=("calibri", 18, "bold"), bg="white",
                                    fg="blue", bd=0,command = 'Data')
        self.add_new_label.place(relx=0.19, rely=0.49)
        self.add_new.place(relx=0.1, rely=0.5)

        self.add_new = Button(self.side_nave, bg="white", bd=0)
        self.image3 = PhotoImage(file="img/dev.png")
        self.add_new.config(image=self.image3)
        self.add_new_label = Button(self.side_nave, text="Admin", font=("calibri", 18, "bold"), bg="white",
                                    fg="blue", bd=0,command = 'teacher_load')
        self.add_new_label.place(relx=0.19, rely=0.69)
        self.add_new.place(relx=0.1, rely=0.7)

        self.add_new = Button(self.side_nave, bg="white", bd=0)
        self.image4 = PhotoImage(file="img/add.png")
        self.add_new.config(image=self.image4)
        self.add_new_label = Button(self.side_nave, text="Records", font=("calibri", 18, "bold"), bg="white",
                                    fg="blue", bd=0,command = 'academics')
        self.add_new_label.place(relx=0.19, rely=0.59)
        self.add_new.place(relx=0.1, rely=0.6)

        self.add_new_label = Label(self.side_nave, text="-----------------------------------------------", font=("calibri", 18, "bold"), bg="white",
                                    fg="blue", bd=0)
        self.add_new_label.place(relx = 0,rely = 0.77)

        """self.add_new_label = Label(self.side_nave, text="-----------------------------------------------",
                                   font=("calibri", 18, "bold"), bg="white",
                                   fg="purple", bd=0)
        self.add_new_label.place(relx=0, rely=0.25)"""

        """self.brand_logo = Label(self.side_nave,bg ="white")
        self.logo = PhotoImage(file= "img/logo111.png")
        self.brand_logo.config(image= self.logo)
        self.brand_logo.place(relx = 0.27,rely = 0.005)"""

        self.schname = Label(self.nave_frame, text="DATABASE MANAGEMENT SYSTEM(C.O.C SCHOOL)", font=("arial", 20, 'bold'),
                             bg="blue",fg = "white")
        self.schname.place(relx=0.01, rely=0.23)
        def clock():
            hour = time.strftime("%I")
            minute =time.strftime("%M")
            seconds = time.strftime("%S")
            am_pm = time.strftime("%p")
            self.time_lbl.config(text =hour + " : "+minute + " : "+ seconds + " "+am_pm)
            self.time_lbl.after(1000,clock)

        self.time_lbl = Label(self.nave_frame,text = " ",font=("arial",20),bg = "blue",fg = "white")
        self.time_lbl.place(relx = 0.83,rely=0.23)
        clock()
        self.vartsy = "Powered by\n VARTSY TECHNOLOGIES"

        self.content = Frame(self.master_frame, width=1000, height=750, bg='white',relief=SUNKEN)
        self.content.pack(side = RIGHT)
#============================================================contents of content frame================================

        self.total_student = StringVar()

        self.card_1 = Frame(self.content,width = 250,height = 150,bg = 'white',bd = 1,relief=SUNKEN)
        self.card_1.place(relx= 0.05,rely =0.05)
        self.entry_1 = Entry(self.card_1,font = ('calibri',40,'bold'),width = 5,textvariable=self.total_student,bd = 0)
        self.entry_1.place(relx= 0.1,rely= 0.2)
        self.lbl_1 = Label(self.card_1,text = "Teaching Staff",bg='white',fg='black',font = ("calibri",15))
        self.lbl_1.place(relx= 0.1,rely =0.7)
        def count():
            self.entry_1.config(state="disable", disabledbackground="white", disabledforeground="black")
            conn = sqlite3.connect("student_info.db")
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM student")
            result = cur.fetchone()[0]
            self.total_student.set(result)
        count()

        self.footer_frame = Frame(self.content,width = 1000,height= 60 ,bg = "blue")
        self.footer_frame.place(relx = 0,rely =0.9)
        self.company = Label(self.footer_frame,text = self.vartsy,font = ("calibri",14,"bold"),fg="white",bg = 'blue')
        self.company.place(relx = 0.72,rely =0)


        self.total_teacher = StringVar()
        self.total_teacher.set(50)
        self.card_2 = Frame(self.content, width=250, height=150, bg='white', bd=1, relief=SUNKEN)
        self.card_2.place(relx=0.35, rely=0.05)
        self.entry_2 = Entry(self.card_2, font=('calibri', 40, 'bold'), width=5, textvariable=self.total_teacher, bd=0)
        self.entry_2.place(relx=0.1, rely=0.2)
        self.lbl_2 = Label(self.card_2, text="Non-Teaching Staff", bg='white', fg='black', font=("calibri", 15))
        self.lbl_2.place(relx=0.1, rely=0.7)

        self.total_admin = StringVar()
        self.total_admin.set(15)
        self.card_3 = Frame(self.content, width=250, height=150, bg='white', bd=1, relief=RAISED)
        self.card_3.place(relx=0.65, rely=0.05)
        self.entry_3 = Entry(self.card_3, font=('calibri', 40, 'bold'), width=5, textvariable=self.total_admin, bd=0)
        self.entry_3.place(relx=0.1, rely=0.2)
        self.lbl_3 = Label(self.card_3, text="Administration", bg='white', fg='black', font=("calibri", 15))
        self.lbl_3.place(relx=0.1, rely=0.7)

        self.department_graph = Frame(self.content,width = 550,height=350,bd = 1,relief = SUNKEN,bg= "white")
        self.department_graph.place(relx=0.05,rely=0.3)
        self.frame_lbl = Frame(self.department_graph, width=550, height=40, bg="blue")
        self.frame_lbl.place(relx=0, rely=0)
        self.dpt_label = Label(self.frame_lbl, text="Departmental Graph", font=("times new roman", 16), bg="blue",fg = "white")
        self.dpt_label.place(relx=0.03, rely=0.05)
        def graph():
            data1 = {'school': ['BS7', 'BS8', 'BS9', 'BS10', 'BS11'],
                     'population_per_class': [20,40,60, 80, 100]
                     }
            df1 = pd.DataFrame(data1)

            figure1 = plt.Figure(figsize=(8.5, 3.5), dpi=100)
            ax1 = figure1.add_subplot(111)
            bar1 = FigureCanvasTkAgg(figure1,self.department_graph )
            bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df1 = df1[['school', 'population_per_class']].groupby('school').sum()
            df1.plot(kind='bar', legend=True, ax=ax1,color = 'r')
            ax1.set_title('Population per a class')



        self.pie = Label(self.department_graph,bg="white")
        #self.piechart =PhotoImage(file="piechart.png",)
        #self.pie.config(image=self.piechart)
        #self.pie.place(relx=0.05,rely= 0.15)
        graph()






master= Tk()
obj = schoolMain(master)
master.mainloop()