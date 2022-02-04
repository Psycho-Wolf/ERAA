#import serial #Dr. Isenbergs' python code to demo the FXYx robot.
#import math
import time
from Tkinter import *
import os
from PIL import ImageTk, Image
import tkMessageBox
from FUNCTIONS import *
import pickle
#from FXYx import *
# MAIN SCREEN #


root = Tk()
root.title("Lets Roll")
labelText3 = StringVar()
labelText3.set('''Welcome to Embry-Riddles Autonous Automaton''')
label3 = Label(root, textvariable=labelText3, height=4,width=45,bg='#CDC8B1',font=('Arial',16,'bold')).place(x=460,y=100)
labelOrder = Label(root,text=" ")

global drinkNames
drinkNames = ['Vodka', 'Gin', 'Rum', 'Tequila', 'Cranberry Juice', 'Lime Juice', 'Lemon Juice', 'Coca Cola', 'Campari', 'Cointreau', 'Grenadine', 'Simple Syrup', 'Tonic Water', 'Dry Veroumth', 'Kahlua', 'Ice']
amnts = [1, 20, 20, 1, 1, 2, 20, 20, 20, 1, 20, 3, 20, 1, 20, 20]
print amnts
def VolCheck(amnts):
    index = [] # Initializes an empty index array to be filled every time function is called
    flag = 0
    for idx, val in enumerate(amnts):
        if val <= 2:
            print 'item num: ' + str(idx) + ', ' + str(val) # CHANGE TO DISPLAY IN ERROR SECTION
            index.append(idx)
            flag += 1
    if flag > 0:
        errChk(index, amnts)

def errChk(index, amnts):
    global drinkNames
    drinkList = ""
    for i in index:
        drinkList+= str(drinkNames[i]) + '\n'
    print drinkList
    ErrMsg = 'The following ingredients need to be replaced:\n\n%s\n\nBottles Replaced?'%(drinkList)
    Msg = tkMessageBox.askquestion(title= 'Test titel', message = ErrMsg)
    if Msg == 'no':
        errChk(index, amnts)
    else:
        for pos in index:
            print 'amount: ' + str(amnts[pos])
            amnts[pos] = 20
    for pos in index:
        print 'amount: ' + str(amnts[pos])


    return

VolCheck(amnts)

root.mainloop()
