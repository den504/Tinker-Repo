from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.geometry("400x400")
root.title("Learn to code")


#create a database or connect to one

conn = sqlite3.connect("address_book.db")

# Create cursor
c = conn.cursor()


#create table
# recall after running the code to create the database 
# we later comment it out so it doesn't keep on creating 
# a new db each time we run the code -removed table code 
# as it was creating errors- you can have code on onenote
# where we 



# Create edit function to Update
def edit():
	editor = Tk()
	editor.geometry("400x400")
	editor.title("Update A Record")


	# create a database or connect to one

	conn = sqlite3.connect("address_book.db")

	#Create cursor
	c = conn.cursor()

	record_id = select_box.get()

	#To Query the database and fetchs data 

	c.execute("SELECT * FROM addresses_book WHERE oid = " + record_id)


	records = c.fetchall()


	
	# Creating Text boxes for Editor Window

	f_name_editor = Entry(editor, width = 30)
	f_name_editor.grid(row=0, column = 1, padx = 20, pady = (10,0))

	l_name_editor = Entry(editor, width = 30)
	l_name_editor.grid(row=1, column = 1)

	address_editor = Entry(editor, width = 30)
	address_editor.grid(row=2, column = 1)

	city_editor = Entry(editor, width = 30)
	city_editor.grid(row=3, column = 1)

	state_editor = Entry(editor, width = 30)
	state_editor.grid(row=4, column = 1)

	zipcode_editor = Entry(editor, width = 30)
	zipcode_editor.grid(row=5, column =1)

	# Create Text Box Labels for Editor Window

	f_name_label_editor = Label(editor, text = "First Name")
	f_name_label_editor.grid(row = 0, column = 0, pady = (10,0))

	l_name_label_editor = Label(editor, text = "Last Name")
	l_name_label_editor.grid(row = 1, column = 0)


	address_label_editor = Label(editor, text = "Address")
	address_label_editor.grid(row = 2, column = 0)

	city_label_editor = Label(editor, text = "City")
	city_label_editor.grid(row = 3, column = 0)

	state_label_editor = Label(editor, text = "State")
	state_label_editor.grid(row = 4, column = 0)

	zipcode_label_editor = Label(editor, text = "Zipcode")
	zipcode_label_editor.grid(row = 5, column = 0)



	for record in records:
		f_name_editor.insert(0, record[0])
		l_name_editor.insert(0, record[1])
		address_editor.insert(0, record[2])
		city_editor.insert(0, record[3])
		state_editor.insert(0, record[4])
		zipcode_editor.insert(0, record[5])
		

    #Create A Save Button - save Edited Records
	Save_btn = Button( editor, text = "Save", command = edit )
	Save_btn.grid(row =11, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 163)


	# Loop through Results - Note the insert method is used to insert info into entry boxes



# Create function to Delete A Record
def delete():

		# create a database or connect to one

	conn = sqlite3.connect("address_book.db")


	# Create cursor
	c = conn.cursor()


	# Delete a Record
	c.execute("DELETE from addresses_book WHERE oid =" + select_box.get())



	#commit changes
	conn.commit()


	#close connection
	conn.close()




def submit():
	#create a database or connect to one

	conn = sqlite3.connect("address_book.db")

    # Create cursor
	c = conn.cursor()

	# Insert Into Table
	c.execute ("INSERT INTO addresses_book VALUES (:f_name,:l_name,:address, :city, :state, :zipcode)",
			{
			'f_name': f_name.get(),
			'l_name': l_name.get(),
			'address': address.get(),
			'city': city.get(),
			'state': state.get(),
			'zipcode': zipcode.get()
			}
		)

    # commit changes
	conn.commit()


	#close connection
	conn.close()



	#Clear the Text Boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	zipcode.delete(0, END)

	



# Create Query Function

def query():

	# create a database or connect to one

	conn = sqlite3.connect("address_book.db")

    #Create cursor
	c = conn.cursor()

	#To Query the database and fetchs data 

	c.execute("SELECT *, oid FROM addresses_book")

	records = c.fetchall()

	#print(records)


	# Loop through Results


	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6])  + "\n"

	# The below shows the output of the query and it's position on the GUI
	query_label = Label (root, text = print_records)
	query_label.grid(row=12, column =0, columnspan = 2)


	#commit changes
	conn.commit()


	#close connection
	conn.close()

# Creating Text boxes


f_name = Entry(root, width = 30)
f_name.grid(row=0, column = 1, padx = 20, pady = (10,0))

l_name = Entry(root, width = 30)
l_name.grid(row=1, column = 1)

address = Entry(root, width = 30)
address.grid(row=2, column = 1)

city = Entry(root, width = 30)
city.grid(row=3, column = 1)

state = Entry(root, width = 30)
state.grid(row=4, column = 1)

zipcode = Entry(root, width = 30)
zipcode.grid(row=5, column =1)

select_box = Entry(root, width = 30)
select_box.grid(row=9, column =1)

# Create Text Box Labels

f_name_label = Label(root, text = "First Name")
f_name_label.grid(row = 0, column = 0, pady = (10,0))

l_name_label = Label(root, text = "Last Name")
l_name_label.grid(row = 1, column = 0)


address_label = Label(root, text = "Address")
address_label.grid(row = 2, column = 0)

city_label = Label(root, text = "City")
city_label.grid(row = 3, column = 0)

state_label = Label(root, text = "State")
state_label.grid(row = 4, column = 0)

zipcode_label = Label(root, text = "Zipcode")
zipcode_label.grid(row = 5, column = 0)

select_label = Label(root, text = "Select ID")
select_label.grid(row = 9 , column = 0)


# Create Submit Button

submit_button = Button(root, text = "Add Record to Database", command = submit)
submit_button.grid(row= 6, column = 0 , columnspan = 2, pady = 10, padx = 10, ipadx = 100 )


#Create a Query Button
query_btn = Button( root, text = "Show Records", command = query )
query_btn.grid(row =7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 127)


#Create A Delete Button
delete_btn = Button( root, text = "Delete Record", command = delete )
delete_btn.grid(row =10, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 136)

#Create A Edit Button
Edit_btn = Button( root, text = "Edit", command = edit )
Edit_btn.grid(row =11, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 163)

# commit changes
conn.commit()


#close connection
conn.close()





root.mainloop()