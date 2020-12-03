from tkinter import *

# creating the root window
root = Tk()

# creating a Label widget-defining widget
# Essentially answers the question of how the 
# widget should look 
myLabel1 = Label (root, text = "Hello World!")
myLabel2 = Label (root, text = "My name is Dennis")

#shoving it on the screen
# Essentially puts what it description of what it should
# look like and creates a GUI that fits, in this case it we 
# position the onjects on the widget using a grid system.


# it does this by calling the the grid method and making row and columns as parameters 
myLabel1.grid(row= 0, column = 0)
myLabel2.grid(row= 0, column = 2)



#this creates a loop around the GUI
root.mainloop()