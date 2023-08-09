import os
import random
from tkinter import *
import time
from tkinter import ttk
import sqlite3
import student_db
from tkinter import messagebox
import pandas as pd,csv
import win32print
from reportlab.lib.pagesizes import A3
from reportlab.platypus import SimpleDocTemplate, Table,Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet
import subprocess




class Data:
    def search_data(self):
        search_string = self.search_entry.get()  # Get the search criteria from the entry widget
        if search_string:
            # clear current data
            self.treeview.delete(*self.treeview.get_children())

            # Open database
            conn = sqlite3.connect('student_info.db')
            # Construct the SELECT query with a WHERE clause
            query = f"SELECT * FROM student WHERE name LIKE ? OR gender LIKE ? OR level LIKE ?"
            # Execute the query with the search criteria and fetch the data
            cursor = conn.execute(query, ('%' + search_string + '%', '%' + search_string + '%', '%' + search_string + '%'))
            fetch = cursor.fetchall()
            count = 0
            for data in fetch:
                if count % 2 == 0:
                    self.treeview.insert('', 'end', values=data, tags=('evenrow'))
                else:
                    self.treeview.insert('', 'end', values=data, tags=('oddrow'))
                count += 1
            cursor.close()
            conn.close()


    def __init__(self,master):
        self.master = master
        self.master.geometry("950x700+200+0")
        self.master.resizable(0,0)
        self.master.config(bg="white")
        self.master.title("VARTSY TECHNOLOGIES")

        self.master_frame = Frame(self.master, width=950, height=700, bg="white")
        self.master_frame.pack()
        self.nave_frame = Frame(self.master_frame, width=950, height=50, bg='blue')
        self.nave_frame.pack()
       
        self.searchbar1 = StringVar()

        def sheet():
            cols = ["S/N", "student_id",  "Student Name","Date Of Birth","Place Of Birth", "Name Of Parent","Mobile Number", "class","Residence","Date Of Registration"]  # Your column headings here
            path = 'read.csv'
            excel_name = 'all_student_data{}.xlsx'.format(random.randint(1,1000))
            lst = []
            with open(path, "w", newline='') as myfile:
                csvwriter = csv.writer(myfile,delimiter=',')
                for row_id in self.treeview.get_children():
                    row = self.treeview.item(row_id, 'values')
                    lst.append(row)
                lst = list(map(list, lst))
                lst.insert(0, cols)
                for row in lst:
                    csvwriter.writerow(row)

            writer = pd.ExcelWriter(excel_name)
            df = pd.read_csv(path)
            df.to_excel(writer, 'sheetname{}'.format(random.randint(1,10)))
            writer.save()
            messagebox.showinfo("export message","Data Exported Successfully")

        def send_bulk():
            os.system('python bulk_sms.py')



        def delete():
            if self.treeview.selection():
                result = messagebox.askquestion('Python - Delete Data Row In SQLite',
                                                'Are you sure you want to delete this record?', icon="warning")
                if result == 'yes':
                    curItem = self.treeview.focus()
                    contents = (self.treeview.item(curItem))
                    selecteditem = contents['values']
                    self.treeview.delete(curItem)
                    student_db.delete(selecteditem[0])

                else:
                    DisplayData_tithe()
        def reload():
            DisplayData_tithe()

        def home():
            master.destroy()
            os.system("python index.py")

        def add_data():
            os.system("python registration.py")



        def generate_pdf():
            # Create a PDF document
            doc = SimpleDocTemplate("treeview.pdf", pagesize=A3)

            # Create a list to hold the data for the PDF table
            data = []

            # Get the column names
            columns = []
            for col in self.treeview["columns"]:
                column_heading = self.treeview.heading(col)["text"]
                columns.append(column_heading)
            data.append(columns)

            # Get the Treeview data
            for item in self.treeview.get_children():
                values = self.treeview.item(item)["values"]
                data.append(values)

            # Create a PDF table from the data
            table_data = Table(data)

            # Create the heading style
            styles = getSampleStyleSheet()
            heading_style = styles["Heading1"]
            heading_style.alignment = 1  # 0=left, 1=center, 2=right


            # Create the heading
            heading = Paragraph("<b>CHURCH OF CHRIST SCHOOL COMPLEX STUDENT DATA SHEET</b>", heading_style)

            # Build the PDF document
            elements = [heading, Spacer(1, 20), table_data]
            doc.build(elements)

            # Open the generated PDF file using the default PDF viewer
            subprocess.run(["start", "treeview.pdf"], shell=True)  # Windows
        def _dev():
            messagebox.showinfo('Developer','Contact Developer')

        self.side_nave = Frame(self.master_frame, width=200, height=750, bg='white', bd=3, relief=RAISED)
        self.side_nave.pack(side=LEFT)


        self.search_entry= Entry(self.side_nave,font = ("calibri",14),width =17,textvariable = self.searchbar1,fg = "blue",bd =2)
        self.search_entry.place(relx = 0.02,rely= 0.1)
        

        self.cmd1 =Button(self.side_nave,text = "Reload Data",bg= "white",fg = "blue",bd = 0,font = ("calibri",14),command = reload)
        self.cmd1.place(relx =0.1,rely = 0.4)

        self.cmd1 = Button(self.side_nave, text="Delete Data", bg="white", fg="blue", bd=0, font=("calibri", 14),command =delete)
        self.cmd1.place(relx=0.1, rely=0.45)
        
        self.cmd1 = Button(self.side_nave, text="Add New Data", bg="white", fg="blue", bd=0, font=("calibri", 14),command = add_data)
        self.cmd1.place(relx=0.1, rely=0.5)
        
        self.cmd1 = Button(self.side_nave, text="Convert to Excel", bg="white", fg="blue", bd=0, font=("calibri", 14),command = sheet)
        self.cmd1.place(relx=0.1, rely=0.55)
        
        self.cmd1 = Button(self.side_nave, text="import csv Data", bg="white", fg="blue", bd=0, font=("calibri", 14))
        self.cmd1.place(relx=0.1, rely=0.6)
        
        self.cmd1 = Button(self.side_nave, text="Send Bulk SMS", bg="white", fg="blue", bd=0, font=("calibri", 14),command= send_bulk)
        self.cmd1.place(relx=0.1, rely=0.65)
        self.cmd1 = Button(self.side_nave, text="Print Data", bg="white", fg="blue", bd=0, font=("calibri", 14),command =generate_pdf)
        self.cmd1.place(relx=0.1, rely=0.7)
        self.cmd1 = Button(self.side_nave, text="Check Academic Stat.", bg="white", fg="blue", bd=0, font=("calibri", 14), command = _dev)
        self.cmd1.place(relx=0.1, rely=0.75)
        
   

        self.schname = Label(self.nave_frame, text="All Students",
                             font=("arial", 15, 'bold'),
                             bg="blue", fg="white")
        self.schname.place(relx=0.01, rely=0.23)

        def clock():
            hour = time.strftime("%I")
            minute = time.strftime("%M")
            seconds = time.strftime("%S")
            am_pm = time.strftime("%p")
            self.time_lbl.config(text=hour + " : " + minute + " : " + seconds + " " + am_pm)
            self.time_lbl.after(1000, clock)

        self.time_lbl = Label(self.nave_frame, text=" ", font=("arial", 15), bg="blue", fg="white")
        self.time_lbl.place(relx=0.83, rely=0.23)
        clock()
        
        self.vartsy = "Powered by\n VARTSY TECHNOLOGIES"

        self.content = Frame(self.master_frame, width=950, height=650, bg='white', relief=SUNKEN)
        self.content.pack(side=RIGHT)

        self.footer_frame = Frame(self.content, width=800, height=40, bg="blue")
        self.footer_frame.place(relx=0, rely=0.938)
        self.company = Label(self.footer_frame, text=self.vartsy, font=("calibri", 12, "bold"), fg="white", bg='blue')
        self.company.place(relx=0.72, rely=0)

        self.tree_frame = Frame(self.content,width = 750,height = 610,bg = "white",bd = 5,relief = SUNKEN)
        self.tree_frame.place(relx = 0,rely = 0)
        
        def DisplayData_tithe():
            # clear current data
            self.treeview.delete(*self.treeview.get_children())
            # open databse
            conn = sqlite3.connect('student_info.db')
            # select query
            cursor = conn.execute("SELECT * FROM student")
            # fetch all data from database
            fetch = cursor.fetchall()
            # loop for displaying all data in GUI
            count = 0
            for data in fetch:
                if count % 2 == 0:
                    self.treeview.insert('', 'end', values=(data), tags=('evenrow'))
                else:
                    self.treeview.insert('', 'end', values=(data), tags=('oddrow'))
                count += 1

            cursor.close()
            conn.close()

        self.scrollbarx = Scrollbar(self.content, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.content, orient=VERTICAL)
        self.treeview = ttk.Treeview(self.tree_frame, columns=(
            "S/N", "student_id",  "Student Name","Date Of Birth","Place Of Birth", "Name Of Parent","Mobile Number", "class","Residence","Date Of Registration",
        ), selectmode="extended", height=15,yscrollcommand=self.scrollbary.set,xscrollcommand=self.scrollbarx.set)
        self.treeview.place(relx=0, rely=0)
        style = ttk.Style()
        # Pick a theme
        style.theme_use('clam')

        style.configure("Treeview.Heading", font=("times new roman", 16, "bold"), foreground='blue',
                        fieldbackground="silver")
        style.configure("Treeview", highlightthickness=4, bd=2, font=('calibri', 16,), background="silver",
                        fg="white"
                        , rowheight=40, fieldbackground="silver")
        style.map('Treeview', background=[('selected', 'red')])
        self.scrollbary.config(command=self.treeview.yview)
        self.scrollbary.place(relx=0.971, rely=0.01, height=580)
        self.scrollbarx.config(command=self.treeview.xview)
        self.scrollbarx.place(relx=0.01, rely=0.903, width=735)

        self.treeview.heading("S/N", text="S/N", anchor=W)
        self.treeview.heading("student_id", text="Student Number", anchor=W)
        self.treeview.heading("Student Name", text="Student Name", anchor=W)
        self.treeview.heading("Date Of Birth", text="Date Of Birth")
        self.treeview.heading("Place Of Birth", text="Place Of Birth", anchor=W)
        self.treeview.heading("Name Of Parent", text="Parent Name", anchor=W)
        self.treeview.heading("Mobile Number", text="Mobile Number", anchor=W)
        self.treeview.heading("class", text="Class/Basic", anchor =W)
        self.treeview.heading("Residence", text="Residence", anchor=W)
        self.treeview.heading("Date Of Registration", text="Admission Date", anchor=W)

        self.treeview.column('#0', stretch=NO, minwidth=0, width=0)
        self.treeview.column('#1', stretch=NO, minwidth=0, width=50)
        self.treeview.column('#2', stretch=NO, minwidth=0, width=250)
        self.treeview.column('#3', stretch=NO, minwidth=0, width=200)
        self.treeview.column('#4', stretch=NO, minwidth=0, width=200)
        self.treeview.column('#5', stretch=NO, minwidth=0, width=200)
        self.treeview.column('#6', stretch=NO, minwidth=0, width=200)
        self.treeview.column('#7', stretch=NO, minwidth=0, width=200)
        self.treeview.column('#8', stretch=NO, minwidth=0, width=200)
        self.treeview.column('#9', stretch=NO, minwidth=0, width=200)
        self.treeview.column('#10', stretch=NO, minwidth=0, width=200)
        self.treeview.tag_configure('oddrow', background='cyan')
        self.treeview.tag_configure('evenrow', background='white')

        self.treeview.place(relx=0., rely=0., width=720, height=582)

        def search_data():
            query = self.searchbar1.get()


            # Clear the Treeview
            self.treeview.delete(*self.treeview.get_children())

            # Get the data from Treeview
            for item in self.treeview.get_children():
                values = self.treeview.item(item)["values"]
                if any(query in str(value).lower() for value in values):
                    self.treeview.insert("", "end", values=values)



        self.searchbtn = Button(self.side_nave,text = "Search",font = ("calibri",14),width =10,bg = "red",fg= "white",command = self.search_data)
        self.searchbtn.place(relx = 0.1,rely = 0.16)
        DisplayData_tithe()

master = Tk()

obj = Data(master)
master.mainloop()