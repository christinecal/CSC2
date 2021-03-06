#Date: Wednesday 11 May
#Name: Christine Calantog

#Practice Assessment: ACHIEVED CRITERIA
#test commit

"""This program is so we know where camps are overnight
Need to ensure that the quit subroutine is added along with the main function which
needs to be called.
Then create the labels and buttons"""

from tkinter import *

#quit subroutine
def quit():
    main_window.destroy()

#print details of all the camps
def print_camp_details ():
    #global variables (accessible throughout the program)
    global j_names, total_entries, name_count
    name_count = 0
    #column headings
    Label(main_window, font='Helvetica 10 bold',text="Row").grid(column=0,row=7)
    Label(main_window, font='Helvetica 10 bold',text="Leader").grid(column=1,row=7)
    Label(main_window, font='Helvetica 10 bold',text="Location").grid(column=2,row=7)
    Label(main_window, font='Helvetica 10 bold',text="Number of Campers").grid(column=3,row=7)
    Label(main_window, font='Helvetica 10 bold',text="Weather").grid(column=4,row=7)
    #each row is the item on the list
    while name_count < total_entries :
        Label(main_window, text=name_count).grid(column=0,row=name_count+8) 
        Label(main_window, text=(camp_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(main_window, text=(camp_details[name_count][1])).grid(column=2,row=name_count+8)
        Label(main_window, text=(camp_details[name_count][2])).grid(column=3,row=name_count+8)
        Label(main_window, text=(camp_details[name_count][3])).grid(column=4,row=name_count+8)
        name_count +=  1

#check input data for validity
#if invalid entry, ask user to enter again
#if valid entry, program continues 

def check_inputs():
    #global variables
    global camp_details, entry_leader, entry_location, entry_campers, entry_weather, total_entries
    input_check = 0
    Label(main_window, text="               ") .grid(column=2, row=0)
    Label(main_window, text="               ") .grid(column=2, row=1)
    Label(main_window, text="               ") .grid(column=2, row=2)
    Label(main_window, text="               ") .grid(column=2, row=3)

    #camp leader cannot be blank and is specific to strings
    #set up an error message 
    if len(entry_leader.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=0)
        input_check = 1

    #location cannot be blank and is specific to strings
    #set up an error message
    if len(entry_location.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=1)
        input_check = 1

    #number of campers cannot be blank, specific to integers 5 to 10
    #set up an error message
    if (entry_campers.get().isdigit()):
        if int(entry_campers.get()) < 5 or int(entry_campers.get()) > 10:
            Label(main_window, fg="red", text="5-10 only") .grid(column=2, row=2)
            input_check = 1
    else:
        Label(main_window, fg="red", text="5-10 only") .grid(column=2, row=2)
        input_check = 1

    #weather cannot not blank, specific to strings
    #set up an error message
    if len(entry_weather.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=3)
        input_check = 1
    if input_check == 0:
        append_name()

#add the next camper to the list
def append_name ():
    #global variables
    global camp_details, entry_leader,entry_location,entry_campers,entry_weather, total_entries
    if len(entry_leader.get()) != 0 :
        camp_details.append([entry_leader.get(),entry_location.get(),entry_campers.get(),entry_weather.get()])
        entry_leader.delete(0,'end')
        entry_location.delete(0,'end')
        entry_campers.delete(0,'end')
        entry_weather.delete(0,'end')
        total_entries +=  1

#delete a row from the list
def delete_row ():
    #global variables
    global camp_details, delete_item, total_entries, name_count
    #deleting selected row
    del camp_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0,'end')
    #clear last item displayed
    Label(main_window, text="       ").grid(column=0,row=name_count+7) 
    Label(main_window, text="       ").grid(column=1,row=name_count+7)
    Label(main_window, text="       ").grid(column=2,row=name_count+7)
    Label(main_window, text="       ").grid(column=3,row=name_count+7)
    Label(main_window, text="       ").grid(column=4,row=name_count+7)
    #print the items as rows
    print_camp_details()

#create the buttons and labels
def setup_buttons():
    #global variables
    global camp_details, entry_leader,entry_location,entry_campers,entry_weather, total_entries, delete_item
    Button(main_window, text="Quit",command=quit) .grid(column=1, row=0)
    Button(main_window, text="Append Details",command=append_name) .grid(column=0,row=1)
    Button(main_window, text="Print Details",command=print_camp_details) .grid(column=1,row=1)
    Label(main_window, text="Leader") .grid(column=0,row=2)
    entry_leader = Entry(main_window)
    entry_leader.grid(column=1,row=2)
    Label(main_window, text="Location") .grid(column=0,row=3)
    entry_location = Entry(main_window)
    entry_location.grid(column=1,row=3)
    Label(main_window, text="Number of Campers") .grid(column=0,row=4)
    entry_campers = Entry(main_window)
    entry_campers.grid(column=1,row=4)
    Label(main_window, text="Weather") .grid(column=0,row=5)
    entry_weather = Entry(main_window)
    entry_weather.grid(column=1,row=5)
    Label(main_window, text="Row #") .grid(column=0,row=6)
    delete_item = Entry(main_window)
    delete_item .grid(column=1,row=6)
    Button(main_window, text="Delete",command=delete_row) .grid(column=2,row=6)

#start the program running
def main():
    #global variables
    global main_window
    global camp_details, entry_name,entry_age,entry_gender, total_entries
    #empty variables for entries and list for camp details
    camp_details = []
    total_entries = 0
    #GUI
    main_window =Tk()
    setup_buttons()
    main_window.mainloop()
    
main()
