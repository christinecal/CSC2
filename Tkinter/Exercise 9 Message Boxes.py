#Date: Thursday 31 March
#Name: Christine Calantog

'''In this program we will create a message box.'''

#from msilib.schema import Icon
from tkinter import *
from tkinter import ttk
#if we do not import, we cannot use message box for our application
from tkinter import messagebox

root =  Tk()

def callback():
    #first parameter will be title and then the text
    mbox  = messagebox.askquestion("Delete", "Are you sure?", icon="warning")
    #can change icon by adding icon="warning"
    if mbox == 'yes':
        print("Deleted")
    else: 
        print("Not Deleted")

def callback2():
    messagebox.showinfo("Success", "Well done!")
    print("You clicked OK!")

#creating buttons

button1 = ttk.Button(root, text="Delete", command=callback).grid(row=0, column=0)
button2 = ttk.Button(root, text="Info", command = callback2).grid(row=0,column=1)

root.geometry("350x250") #size of window
root.mainloop()

#Homework:
#move to column 1, row 2 AND column 2, row 2
#make font larger
