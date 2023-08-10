from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

# Create root window
root = Tk()
root.title("Fonsy's To-Do List")
# root.iconbitmap('C:/Users/Fonsy/Desktop/Python/ToDoList/ToDoList.ico')
root.geometry("500x500")

# Create fonts and colors
my_font = Font(
    family = "8514oem Regular",
    size = 30,
    weight = "bold"
    )

# frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#list box
my_list = Listbox(my_frame,
    font = my_font, 
    width = 25,
    height = 5,       
    bg = "SystemButtonFace",
    bd = 0,
    fg = "#464646",
    
    )

my_list.pack(side=LEFT, fill=BOTH)

# testing and putting in list box
test = ["get food", "study", "gym", "dance"]
for i in test:
    my_list.insert(END, i)
    
# Create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# add scrollbar
my_list.config(yscrollcommand= my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)
    
# create entry box - adds items to list
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

# create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)



# BUTTON FUNCTIONS
def delete_item():
   my_list.delete(ANCHOR) #anchor is whatever is highlighted

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0,END) # how to delete from entry box

def cross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede"
    )
    # Get rid of highlight
    my_list.selection_clear(0, END)

def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646"
    )
    my_list.selection_clear(0, END)
    
def deleteCross_item():
    i = my_list.size() -1
    while i >= 0:
        if my_list.itemcget(i, "fg") == "#dedede":
            my_list.delete(my_list.index(i))  
        i -= 1
            
    
    
# add buttons
delete_button = Button(button_frame, text="Delete Item", command = delete_item)
add_button = Button(button_frame, text="Add Item", command = add_item)
cross_button = Button(button_frame, text="Cross Off Item", command = cross_item)
uncross_button = Button(button_frame, text="Uncross Off Item", command = uncross_item)
deleteCross_button = Button(button_frame, text="Clear Completed Items", command = deleteCross_item)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_button.grid(row=0, column=2 )
uncross_button.grid(row=0, column=3,  padx=20)
deleteCross_button.grid(row=0, column=4)

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Items in Menus
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)

# file menu functions
def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="C:/Users/fonsy/Documents",
        title="Save File",
        filetypes=(("Dat Files","*.dat"),
                   ("All Files", "*.*"))
    )
    if file_name:
        if(file_name.endswith(".dat")):
            pass
        else:
            file_name = f'{file_name}.dat'
            deleteCross_item()
            
    #grab items from list
    items = my_list.get(0,END)
    
    # output file
    output_file = open(file_name, 'wb')
    
    # add items to file
    pickle.dump(items, output_file)

def open_list():
    pass

def clear_list():
    my_list.delete(0,END)

# Drop down items
file_menu.add_command(label="Save List", command=save_list) 
file_menu.add_command(label="Open List", command=open_list) 
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=clear_list) 
# file_menu.add_command(label="Save List", command=save_list) 


# Run Window
root.mainloop()