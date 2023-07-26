from tkinter import *
from tkinter.font import Font

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

my_list.pack()

# testing and putting in list box
test = ["get food", "study", "gym", "dance"]
for i in test:
    my_list.insert(END, i)
    
# Run Window
root.mainloop()