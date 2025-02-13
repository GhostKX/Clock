from tkinter import *
from tkinter.ttk import  *

from time import strftime

# Creating variable from TK
root = Tk()
root.title("Clock")

# Function to format the time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Showing time
label = Label(root, font=("ds_digital", 80), background = "black", foreground = "cyan" )
label.pack(anchor='center')
time()

mainloop()
