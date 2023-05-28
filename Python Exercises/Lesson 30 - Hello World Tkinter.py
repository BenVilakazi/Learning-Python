from tkinter import *

root = Tk() #how to create a TK class

label1 = Label(root, text="Hello World!") # Create an object in the tk class

label1.pack() # pack function adds a widget to the window

root.mainloop() # this creates a loop to keep the window open 

### Using Tkinter frames

root = Tk()

newframe = Frame(root) # This line creates a new frame
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side=BOTTOM)

button1 = Button(newframe, text="click here", fg="Red") # This line will create a button in each frame
button2 = Button(otherframe, text="click here", fg="Green")
button1.pack()
button2.pack()



root.mainloop()

### Grid Layout Tkinter

root = Tk()

label2 = Label(root, text ="FirstName")
label3 = Label(root, text ="LastName")

entry1 = Entry(root)
entry2 = Entry(root)

label2.grid(row = 0, column = 0)
label3.grid(row = 1, column = 0)

entry1.grid(row = 0, column = 1)
entry2.grid(row = 1, column = 1)
root.mainloop()

## Self Adjusting Widgets

root = Tk()

label4 = Label(root, text="First",bg="Black", fg="Grey")
label4.pack(fill=X) # this will increase the width

label5 = Label(root, text="Second",bg="Red", fg="Green")
label5.pack(fill=Y, side=LEFT)

label6 = Label(root, text="Third",bg="Blue",fg="White")
label6.pack(fill=Y, side = RIGHT)

root.mainloop()

### Handling Button Clicks Tkinter

root = Tk()

def deeds():
    print("Good Job")
    
button3 = Button(root, text="Click Here", command = deeds)
button3.pack()

root.mainloop()

### Using Classes in Tkinter

class MyButton:
    
    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()
        
        self.printbutton = Button(frame, text ="Click Here", command = self.printmessage)
        self.printbutton.pack()
        
        self.quitbutton = Button(frame, text="Exit", command = frame.quit)
        self.quitbutton.pack(side=LEFT)
        
    def printmessage(self):
        print("Button Clicked")
         
root = Tk()

b = MyButton(root)

root.mainloop()

### Using Drop Down Menus in Python

def function1():
    print("Menu Item clicked")

root = Tk()

myMenu = Menu(root)
root.config(menu = myMenu)

submenu = Menu(myMenu)

myMenu.add_cascade(label="file", menu=submenu) 

submenu.add_command(label="Project", command=function1)
submenu.add_command(label="Save", command=function1)

submenu.add_separator()

submenu.add_command(label="Exit", command=function1)

newMenu = Menu(myMenu)

myMenu.add_cascade(label="Edit", menu=newMenu)

newMenu.add_command(label="Undo", command=function1)
newMenu.add_command(label="Redo", command=function1)

newMenu.add_separator()

newMenu.add_command(label="Cut", command=function1)
newMenu.add_command(label="Copy", command=function1)
newMenu.add_command(label="Paste", command=function1)


## Toolbar with Tkinter

toolbar = Frame(root, bg="Black")
insertbutton =Button(toolbar, text="insert files", command = function1)
insertbutton.pack(side=LEFT, padx=2, pady=3)

printbutton = Button(toolbar, text="Print", command = function1)
printbutton.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)


### Statusbar with Tkinter

status = Label(root, text="I Am a Statusbar", bd=1, relief=SUNKEN, anchor = W)
status.pack(side=BOTTOM, fill=X)



root.mainloop()

### MessageBox in Python

import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Title","This is great!")

response = tkinter.messagebox.askquestion("Question 1", "Do you like coffee?")

if response == 'yes':
    print("Let's go for coffee sometime...")
    

root.mainloop()

### Drawing in Tkinter

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

newline = canvas.create_line(0, 0, 100, 100)
line2 = canvas.create_line(70, 10, 11, 86, fill="red")

root.mainloop()