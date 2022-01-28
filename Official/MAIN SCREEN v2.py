            # -*- coding: cp1252 -*-
#import serial #Dr. Isenbergs' python code to demo the FXYx robot.
#import math
import time
from Tkinter import *
import os
from PIL import ImageTk, Image
import tkMessageBox
from FUNCTIONS import *
#from FXYx import *

def close():
    root.destroy()
    return

def ORDER():
    global labelOrder
    table = var.get()
    list = text.get('1.0','end')
    if table == 1:
        textfile = open("tab1.txt","a")
        a = textfile.write(list)
        text.delete("1.0","end")
        labelOrder.destroy()
        var.set(5)
    elif table == 2:
        textfile = open("tab2.txt","a")
        a = textfile.write(list)
        text.delete("1.0","end")
        labelOrder.destroy()
        var.set(5)
    elif table == 3:
        textfile = open("tab3.txt","a")
        a = textfile.write(list)
        text.delete("1.0","end")
        labelOrder.destroy()
        var.set(5)
    elif table == 4:
        textfile = open("tab4.txt","a")
        a = textfile.write(list)
        text.delete("1.0","end")
        labelOrder.destroy()
        var.set(5)
    else:
        textfile = open("tabNA.txt","a")
        a = textfile.write(list)
        text.delete("1.0","end")
        labelOrder.destroy()
        var.set(5)
    return

def CheckOut():
    global labelOrder
    table = var.get()
    if table == 1:
        textfile = open("tab1.txt", "r")
        lines = textfile.readlines()
        textfile.close()
        textfile = open("tab1.txt", "w")
        for line in lines:
            textfile.write("")
        textfile.close()
        labelOrder.destroy()
        var.set(5)
    elif table == 2:
        textfile = open("tab2.txt", "r")
        lines = textfile.readlines()
        textfile.close()
        textfile = open("tab2.txt", "w")
        for line in lines:
            textfile.write("")
        textfile.close()
        labelOrder.destroy()
        var.set(5)
    elif table == 3:
        textfile = open("tab3.txt", "r")
        lines = textfile.readlines()
        textfile.close()
        textfile = open("tab3.txt", "w")
        for line in lines:
            textfile.write("")
        textfile.close()
        labelOrder.destroy()
        var.set(5)
    elif table == 4:
        textfile = open("tab4.txt", "r")
        lines = textfile.readlines()
        textfile.close()
        textfile = open("tab4.txt", "w")
        for line in lines:
            textfile.write("")
        textfile.close()
        labelOrder.destroy()
    else:
        textfile = open("tabNA.txt", "r")
        lines = textfile.readlines()
        textfile.close()
        textfile = open("tabNA.txt", "w")
        for line in lines:
            textfile.write("")
        textfile.close()
        labelOrder.destroy()
        var.set(5)
    return

def TableOrder():
    global labelOrder
    table = var.get()
    labelOrder.destroy()
    if table == 1:
        textfile = open("tab1.txt","r")
        order = textfile.read()
        labelOrder = Label(root,text = str(order))
        labelOrder.place(x=1200,y=400)
        var.set(5)
    elif table == 2:
        textfile = open("tab2.txt","r")
        order = textfile.read()
        labelOrder = Label(root,text = str(order))
        labelOrder.place(x=1200,y=400)
        var.set(5)
    elif table == 3:
        textfile = open("tab3.txt","r")
        order = textfile.read()
        labelOrder = Label(root,text = str(order))
        labelOrder.place(x=1200,y=400)
        var.set(5)
    elif table == 4:
        textfile = open("tab4.txt","r")
        order = textfile.read()
        labelOrder = Label(root,text = str(order))
        labelOrder.place(x=1200,y=400)
        var.set(5)
    else:
        textfile = open("tabNA.txt","r")
        order = textfile.read()
        labelOrder = Label(root,text = str(order))
        labelOrder.place(x=1200,y=400)
        var.set(5)
    return


    
def cosmo():
    messageCosmo ='''cosmo\n'''
    text_box.insert('end', messageCosmo)
    return
def negroni():
    messageNegroni ='''negroni\n'''
    text_box.insert('end', messageNegroni)
    return
def russian():
    messageRuss ='''black russian\n'''
    text_box.insert('end', messageRuss)
    return
def liit():
    messageLiit ='''long island iced tea\n'''
    text_box.insert('end', messageLiit)
    return
def cuba():
    messageCuba ='''cuba libre\n'''
    text_box.insert('end', messageCuba)
    return
def john():
    messageJohn ='''john collins\n'''
    text_box.insert('end', messageJohn)
    return
def dry():
    messageDry ='''dry martini\n'''
    text_box.insert('end', messageDry)
    return

# MAIN SCREEN #
root = Tk()
root.title("Lets Roll")
root.attributes("-fullscreen",True)

labelText3 = StringVar()
labelText3.set('''Welcome to Embry-Riddles Autonous Automaton''')
label3 = Label(root, textvariable=labelText3, height=4,width=45,bg='#CDC8B1',font=('Arial',16,'bold')).place(x=460,y=100)

labelOrder = Label(root,text=" ")


# TABLES #
var=IntVar()
var.set(5)
rb1 = Radiobutton(root, text="table 1", value=1,tristatevalue=0,variable=var,relief=RIDGE,bg='#F4A460').place(x=620,y=220)
rb2 = Radiobutton(root, text="table 2", value=2,tristatevalue=0,variable=var,relief=RIDGE,bg='#F4A460').place(x=620,y=250)
rb3 = Radiobutton(root, text="table 3", value=3,tristatevalue=0,variable=var,relief=RIDGE,bg='#F4A460').place(x=830,y=220)
rb4 = Radiobutton(root, text="table 4", value=4,tristatevalue=0,variable=var,relief=RIDGE,bg='#F4A460').place(x=830,y=250)
rb5 = Radiobutton(root, text="NA",      value=5,tristatevalue=0,variable=var,relief=RIDGE).place(x=740,y=650)

# MENU #
button1 = Button(root, text="Cosmopolitan",             width=20,height=4, command=cosmo).place(x=570,y=300)
button2 = Button(root, text="Negroni",                  width=20,height=4, command=negroni).place(x=570,y=375)
button3 = Button(root, text="Black Russian",            width=20,height=4, command=russian).place(x=570,y=450)
button4 = Button(root, text="Long Island Iced Tea",     width=20,height=4, command=liit).place(x=790,y=300)
button5 = Button(root, text="Cuba Libre",               width=20,height=4, command=cuba).place(x=790,y=375)
button6 = Button(root, text="John Collins",             width=20,height=4, command=john).place(x=790,y=450)
button7 = Button(root, text="Dry Martini",              width=20,height=4, command=dry).place(x=570,y=525)
button8 = Button(root, text="ORDER",                    width=20,height=4, command=ORDER,bg='#00FF7F').place(x=790,y=525)
button9 = Button(root, text="Check Out",                width=30,height=2, command=CheckOut,bg='#FF4040').place(x=640,y=600)
button10 = Button(root, text="Table Order",             width=30,height=2, command=TableOrder).place(x=640,y=650)


# ORDER #
labelText4 = StringVar()
labelText4.set('''Order:''')
label4 = Label(root, textvariable=labelText4, height=1,width=6,font=('Arial',16,'bold')).place(x=8,y=250)
message =''''''
text = Text(root,height=8,width=28,font=('Arial',16,'bold'))
text.pack(expand=True)
text.insert('end', message)
text.place(x=8,y=280)


# SETTINGS #
labelText2 = StringVar()
labelText2.set("Staff Only:")
label2 = Label(root, textvariable=labelText2, height=1).place(x=5,y=705)
button8 = Button(root, text="Settings",              width=20, command=settings).place(x=2,y=725)
button9Close = Button(root,text="Close",width=20,command=close).place(x=1200,y=10)


# LOGO #
photo = Image.open('C:\Users\cathe\OneDrive\Desktop\Python Code\LogoNoBack.PNG' )
resize_image = photo.resize((384,216))
img=ImageTk.PhotoImage(resize_image)
label = Label(root,image = img)
label.place(x=-30,y=30)

root.mainloop()
