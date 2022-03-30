# Date: Monday 28 March
# Name: Christine Calantog

from tkinter import *
from tkinter import ttk

root=Tk()

def callback():    
    val1=entry.get()
    val2=entry2.get()
    print("Your name is: " +val1)
    print("Your password is: " +val2)

#create entry boxes
entry = ttk.Entry(root, width=30) #size of field for entry
entry2 = ttk.Entry(root, width=30)
entry.insert(0, "Please enter your name: ") #0 is the index, first character
entry2.insert(0, "Please enter your password: ")

#add a button to the window
button = ttk.Button(root, text="Enter")

#add lablel title
lbltitle = ttk.Label(text="Our Title Goes Here", font=(("Arial"),22))

lblname = ttk.Label(text="Your name: ")
lblpass = ttk.Label(text="Your password: ")
lbltitle.grid(row=0, column=0, columnspan=2)
lblname.grid(row=1, column=0, sticky=W)
lblpass.grid(row=2, column=0)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, sticky=W+E, pady=5)

#checkbox
chvar = IntVar() #checkbox variable
chvar.set(0) #set to 0 (zero) means not checked

#checkbox variable
cbox = Checkbutton(root, text="Remember Me", variable=chvar,
                   font="Arial 16").grid(row=4,column=0, sticky=E, columnspan=2) #in order to align in to the right

root.geometry("500x450") #size of window
root.mainloop()
