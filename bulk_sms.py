from tkinter import *
import requests
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import pandas as pd

class Bulk_SMS:
    def __init__(self,window):
        self.window = window
        self.window.geometry('600x500+380+50')
        self.window.resizable(0,0)
        self.window.config(bg ='white')
        self.window.title("Delcom_Bulk_SMS")

        self.msgline = StringVar()
        self.id = StringVar()
        



        def load_contacts_from_excel():
            file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
            if file_path:
                try:
                    df = pd.read_excel(file_path, dtype={'Phone Number': str})
                    contacts = df['Phone Number'].tolist()  # Assuming the phone numbers are in a column named 'Phone Number'
                    self.msgline.set(','.join(contacts))
                    messagebox.showinfo('Success', 'Contacts loaded successfully!')
                except Exception as e:
                    messagebox.showerror('Error', f'Failed to load contacts: {e}')


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

        def send_multiple_sms():
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
                        messagebox.showinfo("Success", f"SMS sent successfully!")
                    else:
                        messagebox.showerror("Error", f"Failed to send SMS to {phone_number}. Status Code: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    messagebox.showerror("Error", f"Error sending SMS to {phone_number}: {e}")


        self.nav_frame = Frame(self.window,width = 600,height = 40,bg= 'blue')
        self.nav_frame.place(relx = 0,rely = 0)
        self.frame_name = Label(self.nav_frame,text='Bulk Messenger',font = ('times new roman',15),bg = 'blue',fg = 'white')
        self.frame_name.place(relx = 0.02,rely = 0.2)

        self.data_frame = LabelFrame(self.window,text = 'Payment Information',width = 550,height = 100,bd = 3,relief =SUNKEN,bg='white')
        self.data_frame.place(relx = 0.02,rely =0.1 )

        
        self.data_frame3 = LabelFrame(self.window,text = 'Body',width = 400,height = 300,bd = 3,relief =SUNKEN,bg ='white')
        self.data_frame3.place(relx = 0.02,rely =0.3 ) 
        self.Display = Text(self.data_frame3,width =34,height = 10,font = ("calibri",16),fg = "black",bd = 3)
        self.Display.place(relx=.02,rely =0)
        self.data_frame2 = LabelFrame(self.window,text = 'commands',width = 150,height = 200,bd = 3,relief =SUNKEN,bg ='white')
        self.data_frame2.place(relx = 0.7,rely =0.5 ) 

        self.btn_send = Button(self.data_frame2,text = "SEND",bg = "blue",fg = "white",width = 10,font = ("times new roman",13),command = send_sms)
        self.btn_send.place(relx = 0.15,rely =0.24)

        self.btn_send = Button(self.data_frame2,text = "SEND BULK",bg = "black",fg = "white",width = 10,font = ("times new roman",13),command = send_multiple_sms)
        self.btn_send.place(relx = 0.15,rely =0.55)

        self.student_id = Label(self.data_frame,text = "Msg Line",font =("calibri",11),bg = "white",fg = "blue")
        self.student_id.place(relx=0,rely =  .02)
        self.entry2 = Entry(self.data_frame,width = 30,bd = 2,relief = SUNKEN,font = ("calibri",11),
                            textvariable =self.msgline)
        self.entry2.place(relx = 0.25,rely =.02)
        self.btn_load = Button(self.data_frame,text ="CONTACTS",fg = "white",bg = "black",font = ("times new roman",11),command = load_contacts_from_excel)
        self.btn_load.place(relx =0.69,rely= 0.02 )

        self.student_id = Label(self.data_frame, text="Sender_ID", font=("calibri", 11), bg="white", fg="blue")
        self.student_id.place(relx=0, rely=0.36)
        self.entry3 = Entry(self.data_frame, width=30, bd=2, relief=SUNKEN, font=("calibri", 11),textvariable=self.id)
        self.entry3.place(relx=0.25, rely=0.36)

window = Tk()
obj = Bulk_SMS(window)
window.iconbitmap("db.ico")
window.mainloop()