from tkinter import *

root = Tk()

# The below is the Entry class- sort of 
#creates an input box, to put in stuff
# having parameters of root and width

e = Entry(root, width=50)
e.pack()

# This actually creates words in the input box
# usually used as an instuction

e.insert(0, "Enter Your Name")


# e.get fetches whatever your input into the box
# label does the work of pushing the output 

def myClick():
	hello = "Hello" + e.get()
	myLabel = Label(root, text = hello )
	myLabel.pack()

# The below creates a button
# myclick worked without a lambda in this case 
#  as there was no parameter in the 

myButton = Button(root, text = "Enter Your Name", command = myClick)
myButton.pack()


root.mainloop()