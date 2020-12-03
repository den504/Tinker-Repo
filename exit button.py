from tkinter import *

root = Tk()

#the root.quit command performs the exit operation

button_quit = Button(root, text = "Exit Program", command = root.quit)

button_quit.pack()



root.mainloop()