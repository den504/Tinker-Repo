from tkinter import *

# creating the root window
root = Tk()

# creating a Label widget-defining widget
# Essentially answers the question of how the 
# widget should look 
myLabel = Label (root, text = "Hello World!")


#shoving it on the screen
# Essentially puts what it description of what it should
# look like and creates a GUI that fits, in this case
# it created a GUI that fits the text
myLabel.pack()

#this creates a loop around the GUI
root.mainloop()