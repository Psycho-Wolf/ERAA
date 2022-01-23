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

#main screen
root = Tk()
root.title("Lets Roll")
root.attributes("-fullscreen",True)

labelText3 = StringVar()
labelText3.set('''Welcome to Embry-Riddles Autonous Automaton''')
label3 = Label(root, textvariable=labelText3, height=4,width=45,bg='#CDC8B1',font=('Arial',16,'bold')).place(x=460,y=100)

message ='''order:'''
text_box = Text(root,height=8,width=28,font=('Arial',16,'bold'))
text_box.pack(expand=True)
text_box.insert('end', message)
text_box.place(x=8,y=250)

radio1 = Radiobutton(root, text="table 1", value="1").place(x=620,y=220)
radio2 = Radiobutton(root, text="table 2", value="2").place(x=620,y=250)
radio3 = Radiobutton(root, text="table 3", value="3").place(x=830,y=220)
radio4 = Radiobutton(root, text="table 4", value="4").place(x=830,y=250)

button1 = Button(root, text="Cosmopolitan",             width=20,height=4, command=cosmo).place(x=570,y=300)
button2 = Button(root, text="Negroni",                  width=20,height=4, command=negroni).place(x=570,y=375)
button3 = Button(root, text="Black Russian",            width=20,height=4, command=russian).place(x=570,y=450)
button4 = Button(root, text="Long Island Iced Tea",     width=20,height=4, command=liit).place(x=790,y=300)
button5 = Button(root, text="Cuba Libre",               width=20,height=4, command=cuba).place(x=790,y=375)
button6 = Button(root, text="John Collins",             width=20,height=4, command=john).place(x=790,y=450)
button7 = Button(root, text="Dry Martini",              width=20,height=4, command=dry).place(x=570,y=525)
button8 = Button(root, text="ORDER",                    width=20,height=4,bg='#00FF7F').place(x=790,y=525)

labelText2 = StringVar()
labelText2.set("Staff Only:")
label2 = Label(root, textvariable=labelText2, height=1).place(x=5,y=705)
button8 = Button(root, text="Settings",              width=20, command=settings).place(x=2,y=725)
button9Close = Button(root,text="Close",width=20,command=close).place(x=1200,y=10)

phhot = Image.open('C:\GitHub\ERAA\Official\LogoNoBack.png' )
resize_image = phhot.resize((384,216))
img=ImageTk.PhotoImage(resize_image)
label = Label(root,image = img)
label.place(x=-30,y=30)

root.mainloop()
