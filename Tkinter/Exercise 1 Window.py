# Date: Wednesday 23 March
# Name: Christine Calantog

from tkinter import * #imports everything from TK - tkinter is a module
from tkinter import ttk #ttk is a sub module of tkinter

root = Tk() #top level window

#create a label widget
label = Label(root, text = "Hello Python") #what you see
#on screen

#font colour, config is for properties
label.config(text="Hello Python", fg="red")
label.config(bg="yellow") #background colour
label.config(font="Times 20")

label.config(text="Python is a great program and we can do many things with it")
label.config(wraplength="150") #wrap text after 150 characters (put in another line) if long label
label.config(justify="right") #right alignment, where the text is placed

#showing it on the screen
label.pack()
root.geometry("300x250") #size of window

root.mainloop() #GUI is always looping -
#when you run your mouse over and you can click on any button
