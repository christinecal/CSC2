# Date: Thursday 24 March
# Name: Christine Calantog

from importlib.metadata import entry_points
from tkinter import * #imports everything from TK
from tkinter import ttk #submodule of tkinter with more widgets

root = Tk()
def callback():
    val1=entry.get()
    val2=entry2.get()
    print("Your name is: " + val1)
    print("Your password is: " +val2)

#create entry boxes
entry=ttk.Entry(root, width=30) #size of field for entry
entry2=ttk.Entry(root, width=30)
entry.insert(0, "Please enter your name") #0 is the index - first character
entry2.config(show='*') #this will hide the password or text entered

#add a button to the window
button=ttk.Button(root, text="Click ME!", command=callback)
#when you put in a command, you need to write a function under root

#pack 2 entries and then the button
entry.pack()
entry2.pack()
button.pack() #this needs to be after entry pack so it shows below entries
