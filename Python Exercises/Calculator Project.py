from tkinter import *
import ast
#import parser

root = Tk()
root.title("Calculator")

## get user input and adding it into the textfield
i = 0
def getVar(num):
    global i 
    display.insert(i, num)
    i+=1
    
def clearAll():
    display.delete(0, END)
    
def clear():
    entireString = display.get()
    if len(entireString):
        new_string = entireString[:-1]
        clearAll()
        display.insert(0, new_string)
    else:
        clearAll()
        display.insert(0, "Error")
        
def getOperation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i+=length
    
def calc():
    entireString = display.get()
    try:
        a = ast.expr(entireString).compile()
        result = eval(a)
        clearAll()
        display.insert(0, result)
    except Exception:
        clearAll()
        display.insert(0,"Error")
    
    
#adding the input field
display = Entry(root) 
display.grid(row=1, columnspan=6, sticky=W+E)


#adding buttons to the calculator

Button(root, text="1",command = lambda :getVar(1)).grid(row=2,column=0)
Button(root, text="2", command = lambda :getVar(2)).grid(row=2,column=1)
Button(root, text="3",command = lambda :getVar(3)).grid(row=2,column=2)

Button(root, text="4",command = lambda :getVar(4)).grid(row=3,column=0)
Button(root, text="5",command = lambda :getVar(5)).grid(row=3,column=1)
Button(root, text="6",command = lambda :getVar(6)).grid(row=3,column=2)

Button(root, text="7",command = lambda :getVar(7)).grid(row=4,column=0)
Button(root, text="8",command = lambda :getVar(8)).grid(row=4,column=1)
Button(root, text="9",command = lambda :getVar(9)).grid(row=4,column=2)

#adding operator buttons

Button(root, text="AC", command = lambda :clearAll()).grid(row=5,column=0)
Button(root, text="0", command = lambda :getVar(0)).grid(row=5,column=1)
Button(root, text="=", command = lambda :calc()).grid(row=5,column=2)


Button(root, text="+", command = lambda :getOperation("+")).grid(row=2,column=3)
Button(root, text="-", command = lambda :getOperation("-")).grid(row=3,column=3)
Button(root, text="*", command = lambda :getOperation("*")).grid(row=4,column=3)
Button(root, text="/", command = lambda :getOperation("/")).grid(row=5,column=3)

#adding new operations


Button(root, text="pi",command = lambda :getOperation("*3.14")).grid(row=2,column=4)
Button(root, text="%",command = lambda :getOperation("%")).grid(row=3,column=4)
Button(root, text="(",command = lambda :getOperation("(")).grid(row=4,column=4)
Button(root, text="exp",command = lambda :getOperation("**")).grid(row=5,column=4)

Button(root, text="<-", command = lambda :clear()).grid(row=2,column=5)
Button(root, text="x!",command = lambda :getOperation()).grid(row=3,column=5)
Button(root, text=")",command = lambda :getOperation(")")).grid(row=4,column=5)
Button(root, text="^2",command = lambda :getOperation("**2")).grid(row=5,column=5)



root.mainloop()