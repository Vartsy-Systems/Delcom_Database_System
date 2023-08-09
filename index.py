import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os,sqlite3,student_db
import time
from PIL import Image,ImageTk
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#====================================================set school window=================================================
class schoolMain:
    def __init__(self,master):
        self.master = master
        self.master.geometry("950x700+200+0")
        self.master.resizable(0,0)
        self.master.config(bg="white")
        self.master.title("Delcom Database")


        #======================================================functions===========================

        def addNew():
            os.system("python registration.py")

        def fees():

            os.system("python school_fees.py")

        def academics():
            os.system("python academics.py")

        def Data():
            os.system("python data.py")
        def teacher_load():
             os.system("python teacher_load.py")
        
        self.master.after(0, self.update_counts)
        self.colors = ['purple', 'green', 'orange', 'blue', 'red', 'yellow', 'brown', 'pink']    
#====================================================set content frames================================================
        self.master_frame=Frame(self.master,width=950,height=700,bg="white")
        self.master_frame.pack()
        self.nave_frame = Frame(self.master_frame,width= 950,height = 50,bg = 'blue')
        self.nave_frame.pack()
        
        self.side_nave =Frame(self.master_frame,width = 260,height = 750,bg = 'white',bd = 3,relief = RAISED)
        self.side_nave.pack(side=LEFT)
       
#===================================================================buttons for side navigation===========================================
        self.image_lbl = Label(self.side_nave,bg = 'white')
        self.logo = Image.open('img/delcom.jpeg')
        self.resized = self.logo.resize((240,150))
        self.real_image =ImageTk.PhotoImage(self.resized)
        self.image_lbl.config(image =self.real_image)
        self.image_lbl.place(relx = 0.02,rely= 0.05)

        
        self.add_new = Button(self.side_nave,bg = "white",bd = 0)
        self.image = PhotoImage(file="img/new.png")
        self.add_new.config(image=self.image)
        self.add_new_label = Button(self.side_nave,text = "Add New Student",font = ("calibri",16,"bold"),bg = "white",fg = "blue",bd = 0,command = addNew)
        self.add_new_label.place(relx = 0.24,rely = 0.29)
        self.add_new.place(relx = 0.1,rely = 0.3)
        
        self.offer = Button(self.side_nave, bg="white", bd=0)
        self.image1 = PhotoImage(file="img/offer.png")
        self.offer.config(image=self.image1)
        self.add_offer_label = Button(self.side_nave, text="Fee Payment", font=("calibri", 16, "bold"), bg="white",
                                    fg="blue", bd=0,command =fees )
        self.add_offer_label.place(relx=0.24, rely=0.39)
        self.offer.place(relx=0.1, rely=0.4)
      
        self.add_new = Button(self.side_nave, bg="white", bd=0)
        self.image2 = PhotoImage(file="img/attend.png")
        self.add_new.config(image=self.image2)
        self.add_new_label = Button(self.side_nave, text="Student Data", font=("calibri", 16, "bold"), bg="white",
                                    fg="blue", bd=0,command = Data)
        self.add_new_label.place(relx=0.24, rely=0.49)
        self.add_new.place(relx=0.1, rely=0.5)

        self.add_new = Button(self.side_nave, bg="white", bd=0)
        self.image3 = PhotoImage(file="img/dev.png")
        self.add_new.config(image=self.image3)
        self.add_new_label = Button(self.side_nave, text="Messenger", font=("calibri", 16, "bold"), bg="white",
                                    fg="blue", bd=0,command = teacher_load)
        self.add_new_label.place(relx=0.24, rely=0.6)
        self.add_new.place(relx=0.1, rely=0.61)

        
        self.add_new_label = Label(self.side_nave, text="_________________________",font=("calibri", 16, "bold"), bg="white",
                                    fg="blue", bd=0)
        self.add_new_label.place(relx = 0,rely = 0.77)
      


        self.schname = Label(self.nave_frame, text="DATABASE MANAGEMENT SYSTEM", font=("arial", 15, 'bold'),
                             bg="blue",fg = "white")
        self.schname.place(relx=0.01, rely=0.23)
       
        def clock():
            hour = time.strftime("%I")
            minute =time.strftime("%M")
            seconds = time.strftime("%S")
            am_pm = time.strftime("%p")
            self.time_lbl.config(text =hour + " : "+minute + " : "+ seconds + " "+am_pm)
            self.time_lbl.after(1000,clock)

        self.time_lbl = Label(self.nave_frame,text = " ",font=("arial",16),bg = "blue",fg = "white")
        self.time_lbl.place(relx = 0.76,rely=0.23)
        clock()
        self.vartsy = "Powered by\n VARTSY TECHNOLOGIES"

        self.content = Frame(self.master_frame, width=1000, height=750, bg='white',relief=SUNKEN)
        self.content.pack(side = RIGHT)
        
#============================================================contents of content frame================================

        self.total_student = StringVar()

        self.card_1 = Frame(self.content,width = 150,height = 100,bg = 'white',bd = 2,relief=SUNKEN)
        self.card_1.place(relx= 0.05,rely =0.05)
        self.entry_1 = Entry(self.card_1,font = ('calibri',25,'bold'),width = 6,textvariable=self.total_student,bd = 0)
        self.entry_1.place(relx= 0.1,rely= 0.2)
        self.lbl_1 = Label(self.card_1,text = "Total Students",bg='white',fg='black',font = ("calibri",12))
        self.lbl_1.place(relx= 0.1,rely =0.7)
        
       

        self.footer_frame = Frame(self.content,width = 690,height= 60 ,bg = "blue")
        self.footer_frame.place(relx = 0,rely =0.9)
        self.company = Label(self.footer_frame,text = self.vartsy,font = ("calibri",14,"bold"),fg="white",bg = 'blue')
        self.company.place(relx = 0.68,rely =0)


        self.total_teacher = StringVar()
        #self.total_teacher.set(f"{100}")
        self.card_2 = Frame(self.content, width=150, height=100, bg='white', bd=2, relief=SUNKEN)
        self.card_2.place(relx=0.35, rely=0.05)
        self.entry_2 = Entry(self.card_2, font=('calibri', 25, 'bold'), width=5, textvariable=self.total_teacher, bd=0)
        self.entry_2.place(relx=0.1, rely=0.2)
        self.lbl_2 = Label(self.card_2, text="Male Student", bg='white', fg='black', font=("calibri", 12))
        self.lbl_2.place(relx=0.1, rely=0.7)
        """def count2():
            self.entry_2.config(state="disable", disabledbackground="white", disabledforeground="black")
            conn = sqlite3.connect("student_info.db")
            cur = conn.cursor()

            # Count the number of male students
            cur.execute("SELECT COUNT(*) FROM student WHERE pob='Male'")
            result = cur.fetchone()[0]
            self.total_teacher.set(f"{result}")

            conn.close()

        count2()"""

        

        self.total_admin = StringVar()
        #self.total_admin.set(f"{15}")
        self.card_3 = Frame(self.content, width=150, height=100, bg='white', bd=2, relief=RAISED)
        self.card_3.place(relx=0.65, rely=0.05)
        self.entry_3 = Entry(self.card_3, font=('calibri', 25, 'bold'), width=5, textvariable=self.total_admin, bd=0)
        self.entry_3.place(relx=0.1, rely=0.2)
        self.lbl_3 = Label(self.card_3, text="Female Student", bg='white', fg='black', font=("calibri", 12))
        self.lbl_3.place(relx=0.1, rely=0.7)
        """def count3():
            self.entry_3.config(state="disable", disabledbackground="white", disabledforeground="black")
            conn = sqlite3.connect("student_info.db")
            cur = conn.cursor()

            # Count the number of male students
            cur.execute("SELECT COUNT(*) FROM student WHERE pob='Female'")
            result = cur.fetchone()[0]
            self.total_admin.set(f"{result}")

            conn.close()

        count3()"""

       
        self.department_graph = Frame(self.content,width = 550,height=350,bd = 1,relief = SUNKEN,bg= "white")
        self.department_graph.place(relx=0.05,rely=0.3)
        #self.frame_lbl = Frame(self.department_graph, width=700, height=40, bg="blue",bd = 2,relief= SUNKEN)
        #self.frame_lbl.place(relx=0, rely=0)
        #self.dpt_label = Label(self.frame_lbl, text="Departmental Graph", font=("times new roman", 16), bg="blue",fg = "white")
        #self.dpt_label.place(relx=0.03, rely=0.05)
        self.master.after(5000, self.update_graph)
        self.figure = plt.Figure(figsize=(5, 3), dpi=100, facecolor="white")
        self.ax1 = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.department_graph)
        self.canvas.get_tk_widget().place(relx = 0,rely = 0)
    
    

    def update_graph(self):
        # Clear the previous data and redraw the pie chart with updated values
        self.ax1.clear()
        self.graph()
        self.count()
        

        # Update the canvas and schedule the next update
        self.canvas.draw()
        self.master.after(2000, self.update_graph)
    def update_counts(self):
        # Call the count function to update student counts
        self.count()
        self.count_male()
        self.count_female()
        # Schedule the next update after 2 seconds
        self.master.after(2000, self.update_counts)
    def count(self):
        self.entry_1.config(state="disable", disabledbackground="white", disabledforeground="black")
        conn = sqlite3.connect("student_info.db")
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM student")
        result = cur.fetchone()[0]
        self.total_student.set(f"{result}")


    def count_male(self):
        conn = sqlite3.connect("student_info.db")
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM student WHERE pob='Male'")
        result = cur.fetchone()[0]
        conn.close()
        # Update the male count
        self.total_teacher.set(f"{result}")

    def count_female(self):
        conn = sqlite3.connect("student_info.db")
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM student WHERE pob='Female'")
        result = cur.fetchone()[0]
        conn.close()
        # Update the female count
        self.total_admin.set(f"{result}")
    

    def graph(self):
        conn = sqlite3.connect("student_info.db")
        cur = conn.cursor()
        cur.execute("SELECT level, COUNT(*) FROM student GROUP BY level")
        data = cur.fetchall()
        conn.close()
        if data:
            levels, population = zip(*data)
            self.ax1.clear()
            explode = [0.2 if level == 'Basic 3' else 0 for level in levels]

            # Create the pie chart with labels and colors for each level
            self.ax1.pie(population,explode = explode ,labels=levels, colors=self.colors,
                        autopct='%1.1f%%', shadow=True, startangle=140)

            self.ax1.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
            

            self.ax1.set_title('Population per class', fontsize=14, fontweight='bold')
            self.ax1.legend(title='Levels', loc='upper left', labels=levels, bbox_to_anchor=(0.8, 1), fontsize='medium')
        else:
            # If there is no data, clear the plot
            self.ax1.clear()
            self.ax1.set_title('No Data', fontsize=14, fontweight='bold')
            self.ax1.legend().remove()


if __name__ == '__main__':
    master= Tk()
    master.iconbitmap("db.ico")
    obj = schoolMain(master)
    obj.graph()
    master.mainloop()







       

