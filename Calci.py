import sys
from tkinter import *

#main window
root = Tk()
root.title("Calculator")
root.geometry("360x480")
numb = StringVar()
entryBox = Entry(root, textvariable = numb, relief = FLAT, bd = 10, width = 22,
                 fg = "white",insertwidth = 2, font = ("Calibri",20),bg = "black")
entryBox.place(x = 15, y = 10)
entryBox.focus()


# function to update in entry box
global value
value = 0
def update_entry(n):
    global value
    current_value = numb.get()
    if n.isdigit():
        numb.set(current_value + n)        
    else:
        if len(current_value) == 0:  # to avoid * / at start
            if n in ["/", "*"]:
                pass
            else:
                numb.set(current_value + n)
        
        elif current_value[-1] in ["+","-","*","/"]: # To avoid unwanted expression (++,**,*/,..)
            numb.set(current_value[:-1] + n)
        else:
            if n==".": # To avoid extra . DOT
                if "." in str(value):
                    pass
                else:
                  value = current_value + n
                  numb.set(current_value + n)
            else:
                value = 0
                numb.set(current_value + n)
        
def clearAll():
    global value
    value = 0
    numb.set("")

def solv():
    try:
        numb.set((eval(numb.get())))
    except:
        pass
def backslash():
    current_value = numb.get()
    numb.set(current_value[:-1])

    
# function to create button    
def createButton(num,xplace,yplace,w = 5, h = 2, color="#352c51", fontc = "white"):
    if num !="C" and num !="=" and num !="<-":
        #button_image = PhotoImage(file = "kesari1.png")
        ButtonName = Button(root,text = str(num), width = w,
                            height = h, bg = color , bd = 0,
                            fg = fontc,font = ("Helvetica",18), command = lambda: update_entry(str(num)))
       
        #ButtonName.config(image = button_image)
    elif num =="C":
        ButtonName = Button(root,text = str(num), width = w,
                            height = h, bg = color, bd = 0,
                            fg = "black",font = ("Helvetica",18), command = lambda: clearAll())
    elif num =="<-":
        ButtonName = Button(root,text = str(num), width = w,
                            height = h, bg = color, bd = 0,
                            fg = "black",font = ("Helvetica",18), command = lambda: backslash())
    elif num =="=":
        ButtonName = Button(root,text = str(num), width = w,
                            height = h, bg = color, bd = 0,
                            fg = "white",font = ("Helvetica",18), command = lambda: solv())
    
    ButtonName.place(x = xplace,y = yplace)   
    return ButtonName
# ceateButton(num, xplace, yplace, width, height,color)
zerB = createButton(0,17,382, 11, color="#352c21")
oneB = createButton(1,17,302, color="#352c21")
twoB = createButton(2,100,302, color="#352c21")
thrB = createButton(3,182,302, color="#352c21")
forB = createButton(4,17,222, color="#352c21")
fivB = createButton(5,100,222, color="#352c21")
sixB = createButton(6,182,222, color="#352c21")
sevB = createButton(7,17,142, color="#352c21")
eigB = createButton(8,100, 142, color="#352c21")
ninB = createButton(9,182,142, color="#352c21")
decB = createButton(".", 182, 382, color="#352c21")
equB = createButton("=", 264, 301,5,5, color="#ce7304")
plsB = createButton("+", 264, 222, color="#ce7304")
minB = createButton("-", 264, 142, color="#ce7304")
mulB = createButton("*",  264, 66, color="#ce7304")
divB = createButton("/", 182, 66, color="#9b9893", fontc = "black")
clrB = createButton("C", 17, 66, color="#9b9893")
modB = createButton("<-", 100, 66, color="#9b9893", fontc = "black")
about = Label(root, text = "www.concretesteelbond.com",bg="black",fg = "white",font = ("Helvetica",14))
about.place(x=40,y=455)
#Locks the parent windows size.
root.maxsize(350,480);
root.minsize(350,480);
root.configure(background = 'black');
root.mainloop()


#www.concretesteelbond.com Learn Python
