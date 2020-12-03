from tkinter import *

# creating the root window
root = Tk()


def myClick():
	myLabel = Label (root, text = "YOU JUST CLICKED")
	myLabel.pack()


# Notice we defined a lbel to appear called 
# myClick, since the function wasn't called it wouldn't run
# But if you use the function has a parameter on the mybutton ;
# it would performs the action of the function you defined.



#padx = increasing size of button horizontally
#pady = increases size of button vertically
# button command makes the a button
#fg = used amongst the parameters can change the buttons
mybutton = Button(root, text = "Click me!", command = myClick)



mybutton.pack()

root.mainloop()