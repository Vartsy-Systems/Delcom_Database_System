import os
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import sqlite3
import win32api,requests
import win32gui
import win32print
from PIL import Image, ImageTk
import random,fees_backend
import tempfile
from tkinter.filedialog import asksaveasfilename
from tkinter import Tk, Text, Button
from fpdf import FPDF
from reportlab.lib.styles import getSampleStyleSheet
import subprocess
from reportlab.lib.pagesizes import A3
from reportlab.platypus import SimpleDocTemplate, Table,Paragraph,Spacer


class Fee:
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

    def search_data_fee(self):
        search_string = self.search_entry1.get()  # Get the search criteria from the entry widget
        if search_string:
            # clear current data
            self.treeview_fee.delete(*self.treeview_fee.get_children())

            # Open database
            conn = sqlite3.connect('fees_data.db')
            # Construct the SELECT query with a WHERE clause
            query = f"SELECT * FROM fees WHERE std_id LIKE ? OR name LIKE ?  OR tot_fees LIKE ?"
            # Execute the query with the search criteria and fetch the data
            cursor = conn.execute(query, ('%' + search_string + '%', '%' + search_string + '%','%' + search_string + '%'))
            fetch = cursor.fetchall()
            count = 0
            for data in fetch:
                if count % 2 == 0:
                    self.treeview_fee.insert('', 'end', values=data, tags=('evenrow'))
                else:
                    self.treeview_fee.insert('', 'end', values=data, tags=('oddrow'))
                count += 1
            cursor.close()
            conn.close()





    def __init__(self,master):
        self.master = master
        self.master.title("Vartsy Technologies - School Management System")
        self.master.resizable(False,False)
        self.master.geometry("950x700+200+0")
        self.master_frame = Frame(self.master,width = 950 , height = 700,bg = "white")
        self.master_frame.place(relx = 0,rely = 0)

        #variables
        self.msgline = StringVar()
        self.ID = StringVar()
        self.name =StringVar()
        self.basic = StringVar()
        self.total_pay = DoubleVar()
        self.amt_paid = DoubleVar()
        self.arrears = DoubleVar()
        self.Date = StringVar()
        self.id = StringVar()
        self.receipt1 = StringVar()
        self.id.set("COC_SCHOOL")
        self.SEARCH_fee = StringVar()

        self.msgline.set("0545742764")

        def Reset():
            DisplayData_tithe()
        def Reset_fee():
            DisplayData_Fee()
        

        def submit():
            if (len(self.ID.get())!=0):
                fees_backend.insert(self.ID.get(),self.name.get(),self.basic.get(),self.total_pay.get(),self.amt_paid.get(),self.arrears.get(),self.Date.get())

            else:
                messagebox.showwarning("Entry error","Enter Credentials before submitting!!!")

        def send_sms():
            api_url = "https://sms.arkesel.com/sms/api?action=send-sms"
            api_key = "OjBxSFBoQ1NrUFJ6Q0MwR0s="

            phone_number = self.msgline.get()
            sender_id = self.id.get()
            message = self.Display.get("1.0", END).strip()

            if not (phone_number and sender_id and message):
                messagebox.showwarning("Warning", "Please fill out all fields.")
                return

            try:
                response = requests.get(f"{api_url}&api_key={api_key}&to={phone_number}&from={sender_id}&sms={message}")

                if response.status_code == 200:
                    messagebox.showinfo("Success", "SMS sent successfully!")
                else:
                    messagebox.showerror("Error", f"Failed to send SMS. Status Code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"Error sending SMS: {e}")
            def send_multiple_sms(self):
                api_url = "https://sms.arkesel.com/sms/api?action=send-sms"
                api_key = "OjBxSFBoQ1NrUFJ6Q0MwR0s="

                phone_numbers = self.msgline.get().split(',')  # Split multiple phone numbers by comma
                sender_id = self.id.get()
                message = self.Display.get("1.0",END).strip()

                if not (phone_numbers and sender_id and message):
                    messagebox.showwarning("Warning", "Please fill out all fields.")
                    return

                for phone_number in phone_numbers:
                    try:
                        response = requests.get(f"{api_url}&api_key={api_key}&to={phone_number}&from={sender_id}&sms={message}")

                        if response.status_code == 200:
                            messagebox.showinfo("Success", f"SMS sent successfully to {phone_number}!")
                        else:
                            messagebox.showerror("Error", f"Failed to send SMS to {phone_number}. Status Code: {response.status_code}")
                    except requests.exceptions.RequestException as e:
                        messagebox.showerror("Error", f"Error sending SMS to {phone_number}: {e}")





        def print_receipt():
            receipt_text = self.Display.get("1.0", "end-1c")  # Get the contents of the Text widget

            # Create a temporary file for the PDF
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

            # Generate the PDF file
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, txt=receipt_text)
            pdf.output(temp_file.name)

            # Save the PDF file
            file_path = asksaveasfilename(defaultextension=".pdf")
            if file_path:
                temp_file.close()  # Close the temporary file before moving
                win32api.MoveFile(temp_file.name, file_path)

            # Open the PDF file
            win32api.ShellExecute(0, "print", file_path, None, ".", 0)
        def generate_pdf():
            # Create a PDF document
            doc = SimpleDocTemplate("treeview.pdf", pagesize=A3)

            # Create a list to hold the data for the PDF table
            data = []

            # Get the column names
            columns = []
            for col in self.treeview_fee["columns"]:
                column_heading = self.treeview_fee.heading(col)["text"]
                columns.append(column_heading)
            data.append(columns)

            # Get the Treeview data
            for item in self.treeview_fee.get_children():
                values = self.treeview_fee.item(item)["values"]
                data.append(values)

            # Create a PDF table from the data
            table_data = Table(data)

            # Create the heading style
            styles = getSampleStyleSheet()
            heading_style = styles["Heading1"]
            heading_style.alignment = 1  # 0=left, 1=center, 2=right


            # Create the heading
            heading = Paragraph("<b>DELCOM SCHOOL FEES DATA</b>", heading_style)

            # Build the PDF document
            elements = [heading, Spacer(1, 20), table_data]
            doc.build(elements)

            # Open the generated PDF file using the default PDF viewer
            subprocess.run(["start", "treeview.pdf"], shell=True)  # Windows
        
        




        self.title = Frame(self.master_frame,width = 950,height = 70,bg= "blue")
        self.title.place(relx = 0,rely = 0)

        self.side_frame = Frame(self.master,width = 180,height = 700,bg= "blue").pack(side = LEFT)

        self.schname1 = Label(self.side_frame, text="FEES PORTAL", font=("times new roman",15, "bold"), bg="blue",fg="white")
        self.schname1.place(relx=0.01, rely=0.27)

        self.logo1 = Label(self.side_frame,bg = "blue")
        self.logo = Image.open("img/money.png")
        resized_image = self.logo.resize((80, 80))
        self.limg = ImageTk.PhotoImage(resized_image)

        

        #self.logo1 = Label(self.side_frame,bg = "blue")
        #self.limg = PhotoImage(file ="img/money.png")
        self.logo1.config(image = self.limg)
        self.logo1.place(relx = 0.04,rely =0.15)

        self.logo2 = Button(self.side_frame, bg="blue",bd = 0)
        self.limg1 = PhotoImage(file="img/dgraph.png")
        self.logo2.config(image=self.limg1)
        self.logo2.place(relx=0.01, rely=.5)
       
        self.logo3 = Button(self.side_frame, bg="blue", bd=0)
        self.limg2 = PhotoImage(file="img/hlp.png")
        self.logo3.config(image=self.limg2)
        self.logo3.place(relx=0.01, rely=.6)
        

        self.logo4 = Button(self.side_frame, bg="blue", bd=0)
        self.limg3 = PhotoImage(file="img/close.png")
        self.logo4.config(image=self.limg3)
        self.logo4.place(relx=0.01, rely=.68)
        
        self.lbl1 = Button(self.side_frame,text = "Display Graph",font = ("calibri",14,"bold"),fg = "white",bg = "blue",bd = 0)
        self.lbl1.place(relx = 0.05,rely = 0.515)
        
        self.lbl1 = Button(self.side_frame, text="Display Help", font=("calibri", 14, "bold"), fg="white", bg="blue",
                           bd=0)
        self.lbl1.place(relx=0.05, rely=0.6)

        self.lbl1 = Button(self.side_frame, text="Home", font=("calibri", 14, "bold"), fg="white", bg="blue",
                           bd=0)
        self.lbl1.place(relx=0.06, rely=0.68)
        self.main_frame1 = Frame(self.master, width = 950,bg = "white",height = 700,bd=3,relief = RAISED).place(relx = 0.189,rely = 0.09)
        
        self.tabcontrol = ttk.Notebook(self.main_frame1, width=900, height=650)
        self.fees = Frame(self.tabcontrol,bg = "white")
        self.tithe = Frame(self.tabcontrol,bg = "white")
        self.pledge = Frame(self.tabcontrol,bg = "white")
        self.t_db = Frame(self.tabcontrol,bg ="white")
        self.tabcontrol.add(self.fees, text="SCHOOL FEES")


        self.tabcontrol.add(self.t_db, text="DATABASE")
        self.tabcontrol.place(relx=0.18, rely=0.08)
        self.content1 = Frame(self.t_db, width=950, height=650, bg='white', relief=SUNKEN)
        self.content1.pack(side=RIGHT)
        
        self.tree_frame = Frame(self.content1,width = 750,height = 600,bg = "white",bd = 5,relief = SUNKEN)
        self.tree_frame.place(relx = 0,rely = 0.05)
        self.search_entry1 = Entry(self.content1,width = 45,font = ("times new roman", 11),fg ="blue",textvariable = self.SEARCH_fee,bd= 2)
        self.search_entry1.place(relx= 0.38,rely = 0.01)
        self.get2 = Button(self.content1,text = "SEARCH",width = 7,font = ("times new roman", 11),fg = "white",bg ="red",command = self.search_data_fee)
        self.get2.place(relx = 0.76,rely =0)

        self.reset_btn = Button(self.content1,text = "RESET",width = 7,font = ("times new roman", 11),fg = "white",bg ="blue",command = Reset_fee)
        self.reset_btn.place(relx = 0.01,rely =0)

        self.reset_btn = Button(self.content1,text = "EXPORT",width = 7,font = ("times new roman", 11),fg = "white",bg ="black",command = generate_pdf)
        self.reset_btn.place(relx = 0.1,rely =0)

        def DisplayData_Fee():
            # clear current data
            self.treeview_fee.delete(*self.treeview_fee.get_children())
            # open databse
            conn = sqlite3.connect('fees_data.db')
            # select query
            cursor = conn.execute("SELECT * FROM fees")
            # fetch all data from database
            fetch = cursor.fetchall()
            # loop for displaying all data in GUI
            count = 0
            for data in fetch:
                if count % 2 == 0:
                    self.treeview_fee.insert('', 'end', values=(data), tags=('evenrow'))
                else:
                    self.treeview_fee.insert('', 'end', values=(data), tags=('oddrow'))
                count += 1

            cursor.close() 
            conn.close()

        self.scrollbarx = Scrollbar(self.content1, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.content1, orient=VERTICAL)
        self.treeview_fee = ttk.Treeview(self.tree_frame, columns=(
            "S/N", "student_id",  "Student Name","Total Fees","Fees Paid", "Arrears","date of payment", "class"
        ), selectmode="extended", height=15,yscrollcommand=self.scrollbary.set,xscrollcommand=self.scrollbarx.set)
        self.treeview_fee.place(relx=0, rely=0)
        style = ttk.Style()
        # Pick a theme
        style.theme_use('clam')

        style.configure("Treeview.Heading", font=("times new roman", 16, "bold"), foreground='blue',
                        fieldbackground="silver")
        style.configure("Treeview", highlightthickness=4, bd=2, font=('calibri', 16,), background="silver",
                        fg="white"
                        , rowheight=40, fieldbackground="silver")
        style.map('Treeview', background=[('selected', 'red')])
        self.scrollbary.config(command=self.treeview_fee.yview)
        self.scrollbary.place(relx=0.808, rely=0.059, height=550)
        self.scrollbarx.config(command=self.treeview_fee.xview)
        self.scrollbarx.place(relx=0.01, rely=0.903, width=735)

        self.treeview_fee.heading("S/N", text="S/N", anchor=W)
        self.treeview_fee.heading("student_id", text="Student Number", anchor=W)
        self.treeview_fee.heading("Student Name", text="Student Name", anchor=W)
        self.treeview_fee.heading("Total Fees", text="Class of Student")
        self.treeview_fee.heading("Fees Paid", text="Total Fees", anchor=W)
        self.treeview_fee.heading("Arrears", text="Amount Paid", anchor=W)
        self.treeview_fee.heading("date of payment", text="Arrears", anchor=W)
        self.treeview_fee.heading("class", text="Date Of Payment", anchor =W)
        
        

        self.treeview_fee.column('#0', stretch=NO, minwidth=0, width=0)
        self.treeview_fee.column('#1', stretch=NO, minwidth=0, width=50)
        self.treeview_fee.column('#2', stretch=NO, minwidth=0, width=250)
        self.treeview_fee.column('#3', stretch=NO, minwidth=0, width=200)
        self.treeview_fee.column('#4', stretch=NO, minwidth=0, width=200)
        self.treeview_fee.column('#5', stretch=NO, minwidth=0, width=200)
        self.treeview_fee.column('#6', stretch=NO, minwidth=0, width=200)
        self.treeview_fee.column('#7', stretch=NO, minwidth=0, width=200)
        self.treeview_fee.column('#8', stretch=NO, minwidth=0, width=200)
        
        
        self.treeview_fee.tag_configure('oddrow', background='cyan')
        self.treeview_fee.tag_configure('evenrow', background='white')

        self.treeview_fee.place(relx=0., rely=0., width=720, height=582)
        DisplayData_Fee()

        self.data_frame = Frame(self.fees,width =380,height = 330,bg= "white",bd = 2,relief =SUNKEN)
        self.data_frame.place(relx =0,rely = 0)

        self.student_id = Label(self.data_frame, text="MsgLine", font=("times new roman", 11), bg="white", fg="blue")
        self.student_id.place(relx=0, rely=.02)
        self.entry1 =Entry(self.data_frame, width=30,font=("times new roman", 11),bg = 'white',fg ='black',textvariable =self.msgline)
        self.entry1.place(relx=0.28, rely=.02)
        self.student_id = Label(self.data_frame,text = "Student ID",font =("times new roman", 11),bg = "white",fg = "blue")
        self.student_id.place(relx=0,rely =  .12)
     
        self.entry2 = Entry(self.data_frame,width = 30,bd = 2,relief = SUNKEN,font = ("times new roman", 11),textvariable =self.ID)
        self.entry2.place(relx = 0.28,rely =.12)
        self.student_id = Label(self.data_frame, text="Student Name", font=("times new roman", 11), bg="white", fg="blue")
        self.student_id.place(relx=0, rely=0.22)
        self.entry3 = Entry(self.data_frame, width=30, bd=2, relief=SUNKEN, font=("times new roman", 11),textvariable =self.name)
        self.entry3.place(relx=0.28, rely=0.22)
        

        self.student_id = Label(self.data_frame, text="Class/Basic", font=("times new roman", 11), bg="white", fg="blue")
        self.student_id.place(relx=0, rely=0.32)
        self.entry4 = ttk.Combobox(self.data_frame, width=29,font=("times new roman", 11),value= (
            "B-1","B-2","B-3","B-4","B-5","B-6","B-7","B-8","B-9","Creche","Nursery","KG-1","KG-2",
        ),textvariable =self.basic)
        self.entry4.place(relx=0.28, rely=0.32)

        self.student_id = Label(self.data_frame, text="Amount To Pay", font=("times new roman", 11), bg="white", fg="blue")
        self.student_id.place(relx=0, rely=0.42)
        self.entry5 = Entry(self.data_frame, width=30, bd=2, relief=SUNKEN, font=("times new roman", 11),textvariable =self.total_pay)
        self.entry5.place(relx=0.28, rely=0.42)

        self.student_id = Label(self.data_frame, text="Amount Paid", font=("times new roman", 11), bg="white", fg="blue")
        self.student_id.place(relx=0, rely=0.52)
        self.entry6 = Entry(self.data_frame, width=30, bd=2, relief=SUNKEN, font=("times new roman", 11),textvariable =self.amt_paid)
        self.entry6.place(relx=0.28, rely=0.52)

        self.student_id = Label(self.data_frame, text="Arrears", font=("times new roman", 11), bg="white", fg="blue")
        self.student_id.place(relx=0, rely=0.62)
        self.entry7 = Entry(self.data_frame, width=30, bd=2, relief=SUNKEN, font=("times new roman", 11),textvariable =self.arrears)
        self.entry7.place(relx=0.28, rely=0.62)

        self.student_id = Label(self.data_frame, text="Payment Date", font=("times new roman", 11), bg="white", fg="blue")
        self.student_id.place(relx=0, rely=.72)
        self.entry8 = DateEntry(self.data_frame, width=29, bd=2, relief=SUNKEN, font=("times new roman", 11),textvariable =self.Date,date_pattern = "dd-mm-yyyy")
        self.entry8.place(relx=0.28, rely=.72)
        
        self.student_id = Label(self.data_frame, text="Sender_ID", font=("times new roman", 11), bg="white", fg="blue")
        self.student_id.place(relx=0, rely=0.82)
        self.entry9 = Entry(self.data_frame, width=30, bd=2, relief=SUNKEN, font=("times new roman", 11),textvariable =self.id,)
        self.entry9.place(relx=0.28, rely=0.82)

        self.data_frame1 = LabelFrame(self.fees, width=380, height=300, bg="white", bd=2, relief=SUNKEN)
        self.data_frame1.place(relx=0.4, rely=0)
        

        self.Display = Text(self.data_frame1,width =35,height = 15,font = ("Georgia", 12),fg = "black",bd = 3,relief = SUNKEN)
        self.Display.place(relx=0.02,rely =0.02)

        self.SEARCH = StringVar()

        self.data_frame2 = Frame(self.fees, width=800, height=300, bg="white", bd=2, relief=SUNKEN)
        self.data_frame2.place(relx=0, rely=0.47)
        self.action_frame = Frame(self.data_frame2, width=800, height=60, bg="blue", relief=RAISED)
        self.action_frame.place(relx=0, rely=0)
        self.search_entry = Entry(self.action_frame,width = 45,font = ("times new roman", 11),fg ="blue",textvariable = self.SEARCH)
        self.search_entry.place(relx= 0.03,rely = 0.2)
        
        self.tree_frame = Frame(self.data_frame2,width=605,height =250,bg = "white",bd = 5,relief = SUNKEN)
        self.tree_frame.place(relx = 0,rely = 0.17)
       

        self.get = Button(self.action_frame,text = "Get",width = 7,font = ("times new roman", 14),fg = "white",bg ="red",command = self.search_data)
        self.get.place(relx = 0.61,rely =0.16)




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

        def receipt():
            self.Display.delete('1.0', END)
            self.Display.insert(END, f'         DELTA COMPLEX SCHOOL' + '\n')
            self.Display.insert(END, f'         School Fees Receipt' + '\n')
            self.Display.insert(END, f'__________________________________' + '\n\n')

            self.Display.insert(
                END, 'Identity No.              :    ' + self.ID.get() + '\n')
            self.Display.insert(END, 'Student Name         :    ' +
                                self.name.get() + '\n')
            self.Display.insert(END, 'Class/Basic               :    ' +
                                self.basic.get() + '\n')

            self.Display.insert(END, f'Fees                         :    GHC {self.total_pay.get()}' +
                                 '\n')

            self.Display.insert(END, f'Amount Paid          :    GHC {self.amt_paid.get() } ' +
                             '\n')

            self.Display.insert(END, f'Arrears                    :    GHC {self.arrears.get()}' +
                                 '\n')

            self.Display.insert(END, f'Date Of Payment  :    {self.Date.get()}'
                                 '\n')

            self.Display.insert(END, f'Paid to                     :    Administration'
                                     '\n')
        receipt()

        def on_item_select(event):
            try:
                global selected_tuple
                selected_item = self.treeview.focus()
                selected_tuple = self.treeview.item(selected_item)['values']

                self.entry2.delete(0, END)
                self.entry2.insert(END, selected_tuple[1])
                self.entry3.delete(0, END)
                self.entry3.insert(END, selected_tuple[2])


            except IndexError:
                pass

            selected_item =self.treeview.selection()[0]
            item_text = self.treeview.item(selected_item, "text")
            self.entry1.delete(0, "end")
            self.entry1.insert(0, item_text)


        

        self.treeview = ttk.Treeview(self.tree_frame, columns = (
            "S/N","stdname","gender", "dob"
        ), selectmode ="extended",height =30)
        self.treeview.place(relx =0,rely = 0)
        style = ttk.Style()
        # Pick a theme
        style.theme_use('clam')

        style.configure("Treeview.Heading", font=("times new roman", 12, "bold"), foreground='blue',
                        fieldbackground="silver")
        style.configure("Treeview", highlightthickness=4, bd=2, font=('times new roman', 13,), background="silver",
                        foreground="white"
                        , rowheight=20, fieldbackground="silver")
        style.map('Treeview', background=[('selected', 'red')])

        self.treeview.bind("<<TreeviewSelect>>", on_item_select)




        self.treeview.heading("S/N",text = "S/N",anchor = W)
        self.treeview.heading("stdname", text="Registration ID", anchor=W)
        self.treeview.heading("gender",text ="Name",anchor = W)
        self.treeview.heading("dob", text = "Date Of Birth")

        self.treeview.column('#0', stretch=NO, minwidth=0, width=0)
        self.treeview.column('#1', stretch=NO, minwidth=0, width=30)
        self.treeview.column('#2', stretch=NO, minwidth=0, width=150)
        self.treeview.tag_configure('oddrow', background='white')
        self.treeview.tag_configure('evenrow', background='lightblue')

        DisplayData_tithe()
       

    #===================================frame buttons ============================
        self.btn_frame = Frame(self.fees,width= 250,height = 300,bg = "blue")
        self.btn_frame.place(relx = 0.67,rely = 0.471)
        self.main_btn =Frame(self.btn_frame,width = 150,height = 200,bd= 2,relief = SUNKEN)
        self.main_btn.place(relx = 0.05,rely =0.2 )

        #===================================================bUTTONS==========================================================\
        self.students = Button(self.main_btn,text = "DISPLAY", font = ("times new roman", 11),bg = "blue",fg = "white",command = receipt)
        self.students.place(relx = 0.027,rely = 0)
        self.students.config(width = 15)

        self.students = Button(self.main_btn, text="SAVE", font=("times new roman", 11), bg="red", fg="white",command = submit)
        self.students.place(relx=0.027, rely=0.2)
        self.students.config(width=15)

        self.students = Button(self.main_btn, text="SEND", font=("times new roman", 11), bg="blue",
                               fg="white",command=send_sms)
        self.students.place(relx=0.027, rely=0.4)
        self.students.config(width=15)

        self.students = Button(self.main_btn, text="PRINT", font=("times new roman", 11), bg="green",
                               fg="white",command = print_receipt)
        self.students.place(relx=0.027, rely=0.6)
        self.students.config(width=15)
     

        self.students = Button(self.main_btn, text="RESET", font=("times new roman", 11), bg="red",
                               fg="white", command = Reset)
        self.students.place(relx=0.027, rely=0.8)
        self.students.config(width=15)


        self.search_entry = Entry(self.action_frame, width=45, font=("calibri", 15), fg="blue")
        self.search_entry.place(relx=0.03, rely=0.2)
       





master = Tk()
obj = Fee(master)
master.mainloop()