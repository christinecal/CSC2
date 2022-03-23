# Date: Wednesday 23 March
# Name: Christine Calantog

from tkinter import * #imports everything from TK

root = Tk() #top level window

#create label
label = Label(root, text="Hello Python")
label.pack()

#create button (without command does not do anything)
button = Button(root, text="Click Me!")
button.pack()

root.geometry("350x350")
root.mainloop() #this is always at the end of the code
