# Date: Thursday 24 March
# Name: Christine Calantog

from tkinter import * #imports everything from TK

root = Tk() #top level window
def callback():
    label.config(text='You clicked me!', fg='red', bg='yellow')
    #added font colour and background
    #colour on click

#create label
label = Label(root, text = "Hello Python")
label.pack()

#create button (now with the command function)
buttton = Button(root, text = 'Click Me!', command=callback)
buttton['state']='disabled' #can disable the button
buttton['state']='normal' #back tto normal
buttton.pack()

root.geometry("350x300")
root.mainloop()
