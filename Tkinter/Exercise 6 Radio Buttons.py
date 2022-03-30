# Date: Wednesday 30 March
# Name: Christine Calantog

from tkinter import *
from tkinter import ttk

root=Tk()

def callback(): #callback function for outcome
    print("Your name: " + entry.get())
    print("Your password: " + entry2.get())
    if chvar.get()== 1: #means the checkbox is checked
        print("Remember Me - selected")
    else:
        print("Remember Me - not selected")
    print("Your gender: " + gender.get()) #gender value to show when we run the program 

#create entry boxes
entry = ttk.Entry(root, width=30) #size of field for entry
entry2 = ttk.Entry(root, width=30)
entry.insert(0, "Please enter your name: ") #0 is the index, first character
entry2.insert(0, "Please enter your password: ")

#add a button to the window
button = ttk.Button(root, text="Enter")
button.config(command=callback) #**configuring button with the callback function**

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
                   font="Arial 16").grid(row=4,column=0, sticky=E, columnspan=2) #in order to align it to the right

#create another variable
gender = StringVar()

#create radio button
#to get value from our radio button - in the callback function
ttk.Radiobutton(root, text="Female", value="Female", var=gender).grid(row=5,column=0)
ttk.Radiobutton(root, text="Male", value="Male",var=gender).grid(row=5,column=1)

root.geometry("500x450") #size of window
root.mainloop()
