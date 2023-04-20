from tkinter import *
root = Tk()



root.title("Registration Form")

# create the username label and entry widget
username_label = Label(root, text="Username:")
username_label.pack()
username_entry = Entry(root)
username_entry.pack()

# create the password label and entry widget
password_label = Label(root, text="Password:")
password_label.pack()
password_entry = Entry(root, show="*")
password_entry.pack()

# create the submit button
submit_button = Button(root, text="Submit")
submit_button.pack()

# start the main event loop
root.mainloop()
