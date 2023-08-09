from tkinter import *
import time
from tkinter import ttk
from tkinter.ttk import Progressbar
import os
import sys
#=================================================setting up window=====================================================

main = Tk()
#image = PhotoImage(file =" asserts//background.png")
main.geometry("550x100+450+300")

main.overrideredirect(True)
main.config(background = "grey")

#=================================================window content=====================================================


progress_label = Label(main,text = "loading SMS_SENDER...",bg="grey",font = ('arial',14,'bold'),fg ="#ffffff")
progress_label.place(relx = 0.25,rely = 0.25)
progress_bar = Progressbar(main,length = 500,orient =HORIZONTAL,mode = 'determinate')
progress_bar.place(relx = 0.02,rely =0.58)
#=================================================window exit=====================================================
def exit_window():
    sys.exit(main.destroy())
    
#=================================================progressbar function=====================================================
i=0
def load():
    global i
    if i <=10:
        txt="loading Messenger..."+(str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(1000,load)
        progress_bar['value'] = 10*i
        i += 1

        if progress_bar['value']==100:
            main.destroy()
            os.system("python bulk_sms.py")





load()

main.resizable(False,False)
main.mainloop()