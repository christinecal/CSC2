# Date: Monday 28 March
# Name: Christine Calantog

#This program shows Grid  Manager - which helps us to organise our widgets easily

from tkinter import *
from tkinter import ttk

root = Tk()

#create entries
entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)

#create placeholder
entry.insert(0, "Please enter your name")
entry2.insert(0, "Please enter your password")

#create button and labels
button = ttk.Button(root, text="Enter")
lbltitle = ttk.Label(text="Our Title Here", font=(("Arial"), 22))
lblname = ttk.Label(text="Your name: ")
lblpass = ttk.Label(text="Your password: ")

#position of the butttons, labels, and entries as outcome
lbltitle.grid(row=0, column=0)
lblname.grid(row=1, column=0)
lblpass.grid(row=2, column=0)

entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1)

root.geometry("500x450")
root.mainloop()
