from tkinter import *

def btn_click():
    # print(txt_box1.get())
    # print(txt_box2.get())
    # get the first name and last name from the entry widgets
    first_name = txt_box1.get()
    last_name = txt_box2.get()
    # concatenate the first name and last name to create the full name
    full_name = f"{first_name} {last_name}"
    # open the file in write mode and write the full name to it
    with open("names.txt", "w") as f:
        f.write(full_name)

# create a window
window = Tk()

# set the window geometry
window.geometry('800x600+100+200')

# create the labels and entry widgets
label1 = Label(window, text='first name')
label1.pack()
txt_box1 = Entry(window, width=50)
txt_box1.pack()
label2 = Label(window, text='last name')
label2.pack()
txt_box2 = Entry(window, width=50)
txt_box2.pack()

# create the button and set the command
#window added here because the button widget needs to be added as a child of the main window in order to be displayed on the screen.
btn1 = Button(window, text="click me", command=btn_click)
btn1.pack()

# run the window mainloop
window.mainloop()
