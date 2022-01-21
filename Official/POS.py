# -*- coding: cp1252 -*-
#imports
from Tkinter import *
import os
#from PIL import ImageTk, Image
import tkMessageBox
import time

def recipe():
     orderVal = var.get()
          #tkMessageBox.showinfo("You're ordering", orderVal)
          # this is where the recipes for each drink goes
          # drinks are each assigned a value, the value will correspond
          # to the recipe and then be "imported" into the order function

     orderlistNames = ["Bob"]
     NeworderlistNames = [yourName.get()]
     orderlistNames.extend(NeworderlistNames)
          # AFTER 2 minutes take off the first place name to update list
          # NEED an IF statement for this pop of name
     #orderlistNames.pop(0)
     print(orderlistNames)

def order():
#     import recipe
     name = "Thank you for ordering " +yourName.get()
     labelText.set(name)
     yourName.delete(0,END)
     return var.set(8)

#main screen
root = Tk()
root.title("ERAA POS")
root.geometry('450x400')

#phhot = Image.open('D:\GitHUB\ERAA\Official\LogoNoBack.png' )
#resize_image = phhot.resize((256,144))
#img=ImageTk.PhotoImage(resize_image)
#label = Label(root,image = img)
#label.place(x=-50,y=256)

labelText = StringVar()
labelText.set("Welcome: Please enter your name and select a drink")
     
label1 = Label(root, textvariable=labelText, height=4,relief=GROOVE, width=50)
label1.pack()

custName = StringVar(None)
yourName = Entry(root, textvariable=custName)
yourName.pack(pady=10)

var = IntVar()
var.set(None)

rb1 = Radiobutton(root, text="Cosmopolitan",           value=1, variable = var,command=recipe).pack()
rb2 = Radiobutton(root, text="Negroni",                value=2, variable = var,command=recipe).pack()
rb3 = Radiobutton(root, text="Black Russian",          value=3, variable = var,command=recipe).pack()
rb4 = Radiobutton(root, text="Long Island Iced Tea",   value=4, variable = var,command=recipe).pack()
rb5 = Radiobutton(root, text="Cuba Libre",             value=5, variable = var,command=recipe).pack()
rb6 = Radiobutton(root, text="John Collins",           value=6, variable = var,command=recipe).pack()
rb7 = Radiobutton(root, text="Dry Martini",            value=7, variable = var,command=recipe).pack()
rb8 = Radiobutton(root, text="none",                   value=8, variable = var).pack(pady=20)

button = Button(root, text='ORDER', relief = RAISED, font=('Arial Bold',18), command=order)
button.place(x=175,y=300)

root.mainloop()
