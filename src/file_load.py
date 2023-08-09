from tkinter import *
import time
from tkinter import ttk
from tkinter.ttk import Progressbar
import os
import sys

from PIL import Image,ImageTk
#=================================================setting up window=====================================================

main = Tk()
#image = PhotoImage(file =" asserts//background.png")
height = 430
width = 530
x= (main.winfo_screenwidth()//2)-(width//2)
y = (main.winfo_screenheight()//2)-(height//2)
main.geometry('{}x{}+{}+{}'.format(width,height,x,y))
main.overrideredirect(True)
main.config(background = "white")

#=================================================window content=====================================================
welcome_label = Label(main,text = "DELCOM MANAGEMENT SYSTEM",bg="white",font = ('arial',18,'bold'),fg ="blue")
welcome_label.place(relx = 0.1,rely =0.1)

image_lbl = Label(main,bg = 'white')
logo = Image.open('img/delcom.jpeg')
resized = logo.resize((400,300))
real_image = ImageTk.PhotoImage(resized)
image_lbl.config(image =real_image)
image_lbl.place(relx = 0.15,rely= 0.16)

progress_label = Label(main,text = "loading Data...",bg="white",font = ('arial',14,'bold'),fg ="blue")
progress_label.place(relx = 0.35,rely = 0.75)
progress_bar = Progressbar(main,length = 500,orient =HORIZONTAL,mode = 'determinate')
progress_bar.place(relx = 0.02,rely =0.88)
#=================================================window exit=====================================================
def exit_window():
    sys.exit(main.destroy())

#=================================================progressbar function=====================================================
i=0
def load():
    global i
    if i <=10:
        txt="Loading Data..."+(str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(1000,load)
        progress_bar['value'] = 10*i
        i += 1

        if progress_bar['value']==100:
            main.destroy()

            os.system("python school_payments.py")



load()

main.resizable(False,False)
main.mainloop()