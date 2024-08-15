import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import sqlite3
from tkinter import messagebox

#Methods for the buttons in tab1
def send_receipt():
    print("hi")

def delete_from_list():
    for index in reversed(result_list.curselection()):
        result_list.delete(index)

def saveFile():
    fp = filedialog.asksaveasfile(initialdir="/",
                                    title="Select a File",
                                    filetypes=[ ("text file", "*.txt"), ("csv file", ".csv"), ("pdf files", "*.pdf"), ("All Files","*.*") ],
                                    defaultextension=".txt", mode="w")
    #To prevent the exception of AttributeError:'NoneType object has no attribute 'write' when we close the Save a File
    if fp is None:
        return
    
    #Here we will write the list box data to the file we selected on each line
    fp.write("\n".join(result_list.get(0,tk.END)))


window = tk.Tk()

window.title("Receipt Sender")
window.geometry("900x600") #WxH

# Notebook Widget
notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays
notebook.pack(expand=True, fill="both") #expand=tofill any space not otherwise used, fill=space on x and y axis

#tab 1
tab1 = ttk.Frame(notebook) #creating a seperate Frame tab of its own
notebook.add(tab1, text='Balance Sheet Sender') #adding the tab to the notebook widget

#Here we create a label to put in the tab1 window
label_results = tk.Label(tab1, text="Status Report:", font=('Arial', 20, 'bold'))  #Adding a label to the notebook widget in tab1
label_results.place(x= 30, y=155) #placing it at the given coordinates, this would label title for listbox

#The Send button
SendButton = tk.Button(tab1, text="START\n Sending Receipts", font=('Arial', 18), command= send_receipt) #Creating the Send Button into tab1
SendButton.place(height=90, width=160, x= 350, y=20,) #placing it at the coordinates

#Scroll bar 
yscrollbar = tk.Scrollbar(tab1) #Creating vertical scroll bar into tab1
yscrollbar.place(height=300,relx=0.98, rely=0.35) #placing it next to the listbox widget


#Our List Box
result_list = tk.Listbox(tab1, font=("Times New Roman", 30) ,selectmode="multiple", yscrollcommand=yscrollbar.set)
result_list.place(height=300, width=825, rely=0.35, relx=0)

#Here is the data that is being put into the List Box
for i in range(30):
    result_list.insert(i, str(i+1))

#Delete Button to delete selected items in our Listbox
delete_from_list = tk.Button(tab1, text="Delete from List", command=delete_from_list)
delete_from_list.place(relx=0.75, rely=0.93)

#Save Button to save the data in our list in a txt/csv/pdf/document 
save_Button = tk.Button(tab1, text="Save", command=saveFile)
save_Button.place(relx=0.10, rely=0.93)










#tab 2

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Add Clients to DB')

#Database stuff
#create a database or connect to one that exists
conn = sqlite3.connect('tree_crm.db')
#Create a cursor instance
c = conn.cursor()

c.execute("""CREATE TABLE if not exists Client_List (
          Client_Name text PRIMARY KEY,
          Email_Address text,
          Phone_Number text,
          Client_Num text)
          """)

 #Commit changes
conn.commit()
#Close out connection
conn.close()

def query_database():
    #create a database or connect to one that exists
    conn = sqlite3.connect('tree_crm.db')
    #Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT * FROM Client_List")
    records = c.fetchall()
    #print(records)

    global count
    count = 0

    for record in records:
        if count % 2 == 0 :
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        count += 1


    #Commit changes
    conn.commit()
    #Close out connection
    conn.close()



tree_frame = tk.Frame(tab2)
tree_frame.pack(pady=10)

tree_scroll = tk.Scrollbar(tree_frame)
tree_scroll.pack(side="right", fill="y")

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()
# my_tree.place(relx=0.18, rely=0.10)

tree_scroll.config(command=my_tree.yview)

my_tree['columns'] = ("Client_Name", "Email_Address", "Phone_Number", "Client_Num")

my_tree.column("#0", width=0, stretch= tk.NO)
my_tree.column("Client_Name", anchor="w", width=200)
my_tree.column("Email_Address", anchor="center", width=200)
my_tree.column("Phone_Number", anchor="center", width=200)
my_tree.column("Client_Num", anchor="w", width=200)

my_tree.heading("#0", text="", anchor="w")
my_tree.heading("Client_Name", text="Client_Name", anchor="w")
my_tree.heading("Email_Address", text="Email_Address", anchor="center")
my_tree.heading("Phone_Number", text="Phone_Number", anchor="center")
my_tree.heading("Client_Num", text="Client_Num", anchor="center")


my_tree.tag_configure('oddrow', background="#075264")
my_tree.tag_configure('evenrow', background="lightblue")



#Add record entry boxes
data_frame = tk.LabelFrame(tab2, text="Record")
data_frame.pack(fill="x", expand=tk.YES, padx=20)

name_label = tk.Label(data_frame, text="Client Name")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(data_frame)
name_entry.grid(row=0, column=1, padx=10, pady=10)

email_label = tk.Label(data_frame, text="Email Address")
email_label.grid(row=0, column=2, padx=10, pady=10)
email_entry = tk.Entry(data_frame)
email_entry.grid(row=0, column=3, padx=10, pady=10)

phone_label = tk.Label(data_frame, text="Phone Number")
phone_label.grid(row=1, column=0, padx=10, pady=10)
phone_entry = tk.Entry(data_frame)
phone_entry.grid(row=1, column=1, padx=10, pady=10)

num_label = tk.Label(data_frame, text="Client Num")
num_label.grid(row=1, column=2, padx=10, pady=10)
num_entry = tk.Entry(data_frame)
num_entry.grid(row=1, column=3, padx=10, pady=10)

#Button functionality
def insert_client():
    #create a database or connect to one that exists
    conn = sqlite3.connect('tree_crm.db')
    #Create a cursor instance
    c = conn.cursor()

    #Add new record
    try:
        c.execute("INSERT INTO Client_List VALUES (:name, :email, :number, :num)",
                    {
                    'name': name_entry.get(),
                    'email': email_entry.get(),
                    'number': phone_entry.get(),
                    'num': num_entry.get(),
                    })
    except sqlite3.IntegrityError:
        messagebox.showinfo("Duplicate", "Client Already Exists in Database")    

    #Commit changes
    conn.commit()
    #Close out connection
    conn.close()

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    num_entry.delete(0, tk.END)

    #Clear the treeview
    my_tree.delete(*my_tree.get_children())
    #Run to pull data from database on start
    query_database()


def update_client():
    selected = my_tree.focus()
    my_tree.item(selected, text="", values=(name_entry.get(), email_entry.get(), phone_entry.get(), num_entry.get(),))
    
    #create a database or connect to one that exists
    conn = sqlite3.connect('tree_crm.db')
    #Create a cursor instance
    c = conn.cursor()

    c.execute("""UPDATE Client_List SET
            Email_Address = :email,
            Phone_Number = :number,
            Client_Num = :num  
        
            WHERE Client_Name = :name""",
            {
                'email': email_entry.get(),
                'number': phone_entry.get(),
                'num': num_entry.get(), 
                'name': name_entry.get(),
            })

    #Commit changes
    conn.commit()
    #Close out connection
    conn.close()

    #Clear entry boxes
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    num_entry.delete(0, tk.END)

def delete_client():
    response = messagebox.askyesno("Are you sure you want to delete this record?")
    if response == 1:
        #create a database or connect to one that exists
        conn = sqlite3.connect('tree_crm.db')
        #Create a cursor instance
        c = conn.cursor()

        c.execute("""DELETE FROM Client_List WHERE Client_Name = :name""",  #:name is a variable 
                {
                    'name': name_entry.get(),   #and we insert value into that variable here
                })

        #Commit changes
        conn.commit()
        #Close out connection
        conn.close()

        #Clear the Entry Boxes
        clear_entries()

        #Add a little mesage box to let you know its been deleted
        messagebox.showinfo("Deleted", "Your Record Has Been Deleted")

        #Clear the treeview
        my_tree.delete(*my_tree.get_children())
        #Run to pull data from database on start
        query_database()

def delete_selected_clients():
    response = messagebox.askyesno("Are you sure you want to delete the Selected Records?")
    if response == 1:
        #Designate selection
        x = my_tree.selection()
        
        #Create a List of ID's
        ids_to_delete = []
        #Add selection to ids_to_delete list
        for record in x:
            ids_to_delete.append(my_tree.item(record, 'values')[0])

        #Delete From Treeview
        for record in x:
            my_tree.delete(record)
        #create a database or connect to one that exists
        conn = sqlite3.connect('tree_crm.db')
        #Create a cursor instance
        c = conn.cursor()

        #Delete selection
        c.executemany("DELETE FROM Client_List WHERE Client_Name = ?", [(a,) for a in ids_to_delete])

        #Commit changes
        conn.commit()
        #Close out connection
        conn.close()

        #Clear the Entry Boxes
        clear_entries()

        #Add a little mesage box to let you know its been deleted
        messagebox.showinfo("Deleted", "Your Selected Records Have Been Deleted")

def clear_entries():
    #Clear entry boxes
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    num_entry.delete(0, tk.END)

def select_record(e):
    #Clear entry boxes
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    num_entry.delete(0, tk.END)

    #Grab record Number
    selected = my_tree.focus()
    #Grab recrod values
    values = my_tree.item(selected, 'values')

    #output to entry boxes
    name_entry.insert(0, values[0])
    email_entry.insert(0, values[1])
    phone_entry.insert(0, values[2])
    num_entry.insert(0, values[3])




#Add Buttons
button_frame = tk.LabelFrame(tab2, text="Commands")
button_frame.pack(fill="x", expand=tk.YES, padx=20)

Add_Button = tk.Button(button_frame, text="Add Record", command=insert_client)
Add_Button.grid(row=0, column=0, padx=10, pady=10)

Update_Button = tk.Button(button_frame, text="Update Client information", command=update_client)
Update_Button.grid(row=0, column=1, padx=10, pady=10)

Delete_Button = tk.Button(button_frame, text="Delete Client", command=delete_client)
Delete_Button.grid(row=0, column=2, padx=10, pady=10)

Delete_many_Button = tk.Button(button_frame, text="Delete Selected Clients", command=delete_selected_clients)
Delete_many_Button.grid(row=0, column=3, padx=10, pady=10)

Select_record_Button = tk.Button(button_frame, text="Clear Entries", command=clear_entries)
Select_record_Button.grid(row=0, column=4, padx=10, pady=10)

#Bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

#Run to pull data from database on start
query_database()

notebook.pack()

window.mainloop()

