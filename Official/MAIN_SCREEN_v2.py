# This is the main control script of Benny
import serial #Dr. Isenbergs' python code to demo the FXYx robot.
import math
import time
from Tkinter import *
import os
from PIL import ImageTk, Image
import tkMessageBox
from FUNCTIONS import *
#import globals
#from FXYx import *
from ingPnts import *


servosOn() # Turns the servo motors of the FXYx
HomePos() # Moves the FXYx to the home position

# Profits stores the gross profit of all drinks ordered
# amnts is a 16 element array that stores the amnts of each ingredient left in the system
# tnP, where n = 0 to 4, are the variables storing the indiviual profits of the tables
global profit, amnts
global t1P, t2P, t3P, t4P, t0P
t1P = 0; t2P = 0; t3P = 0; t4P = 0; t0P = 0
global drinkNames # An arracy that stores all ingrendient names
global NumOfDrinks # Total number of drinks ordered across all tables
global tableDrinks # Number of drinks in an order
tableDrinks = 0
NumOfDrinks = 0
global queue    # a numeric array that stores the numbers corespoding to every drink in an order
queue = []      # Fn buildDrinks() shows which number corresponds to each drink

drinkNames = ['Vodka', 'Gin', 'Rum', 'Tequila', 'Cranberry Juice', 'Lime Juice', 'Lemon Juice', 'Coca Cola', 'Campari', 'Cointreau', 'Grenadine', 'Simple Syrup', 'Tonic Water', 'Dry Veroumth', 'Kahlua', 'Ice']
amnts = [1, 20, 20, 1, 1, 2, 20, 20, 20, 1, 20, 3, 20, 1, 20, 20]

# opens the ingredients binary file and stores the values to the amnts array
fAmnts = open('ingrAmnt.p', 'rb')
amnts = pickle.load(fAmnts)
fAmnts.close()

print "amounts of every: " + str(amnts)
profit = 0 # ensures starting profit for the run is set to
price = 11

def close():
    f = open('ingrAmnt.p', 'wb')
    pickle.dump(amnts, f, -1)
    f.close()
    root.destroy()
    return

# This function itterates through the queue array, building whatever drink corresponds to the number in
# a position in the array. Due to the funciton needing to itterate through every value of an array the POS
# system will not be usable until every drink has been made
def buildDrinks():
    global queue
    for drnkNum in queue:
        if drnkNum == 1:
            cosmoBuild()
        elif drnkNum == 2:
            negroniBuild()
        elif drnkNum == 3:
            russianBuild()
        elif drnkNum == 4:
            liitBuild()
        elif drnkNum == 5:
            cubaBuild()
        elif drnkNum == 6:
            johnBuild()
        elif drnkNum == 7:
            dryBuild()
    return


def ORDER():
    global labelOrder
    global NumOfDrinks
    global tableDrinks
    global queue
    global t1P, t2P, t3P, t4P, t0P
    NumOfDrinks += tableDrinks
    Stonks = tableDrinks*11
    table = var.get()
    list = text.get('1.0','end')
    if table == 1:
        # Removing the last line to get ride of the profit
        print list

        t1P += Stonks
        textfile = open("linDel.txt","r")
        t = textfile.read()
        textfile.close()
        m=t.split("\n")
        s="\n".join(m[:-1])
        textfile = open("linDel.txt","w")
        for i in range(len(s)):
            textfile.write(s[i])
        textfile.close()

        textfile = open("tab1.txt","a")
        a = textfile.write(str(Stonks) + '\n')
        a = textfile.write(list)
        text.delete("1.0","end")
        labelOrder.destroy()
        var.set(5)
    elif table == 2:
        t2P += Stonks
        textfile = open("tab2.txt","a")
        a = textfile.write(list)
        a = textfile.write(str(Stonks) + '\n')
        text.delete("1.0","end")
        labelOrder.destroy()
        var.set(5)
    elif table == 3:
        t3P += Stonks
        textfile = open("tab3.txt","a")
        a = textfile.write(list)
        a = textfile.write(str(Stonks) + '\n')
        text.delete("1.0","end")
        labelOrder.destroy()
        var.set(5)
    elif table == 4:
        t4P += Stonks
        textfile = open("tab4.txt","a")
        a = textfile.write(list)
        a = textfile.write(str(Stonks) + '\n')
        text.delete("1.0","end")
        labelOrder.destroy()
        var.set(5)
    else:
        t0P += Stonks
        textfile = open("tabNA.txt","a")
        a = textfile.write(list)
        a = textfile.write(str(Stonks) + '\n')
        text.delete("1.0","end")
        labelOrder.destroy()
        var.set(5)
    tableDrinks = 0
    Stonks = 0
    buildDrinks()
    queue = []
    return

def CheckOut(amnts):
    Stonks(amnts)
    global profit
    print profit   #FOR TESTING DELETE IN FINAL VERSION
    profit = 0
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
        t1P = 0
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
        t2P = 0
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
        t3P = 0
    elif table == 4:
        textfile = open("tab4.txt", "r")
        lines = textfile.readlines()
        textfile.close()
        textfile = open("tab4.txt", "w")
        for line in lines:
            textfile.write("")
        textfile.close()
        labelOrder.destroy()
        t4P = 0
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
        t0P = 0
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

def Stonks(amnts):
    global profit
    timestr = time.strftime("%Y%m%d-%H%M%S")
    stonks = open(timestr + '.txt', 'w')
    stonks.write("Vodka: " + str(amnts[0]) + '\n')
    stonks.write("Gin: " + str(amnts[1]) + '\n')
    stonks.write("Rum: " + str(amnts[2]) + '\n')
    stonks.write("Teqprofituila: " + str(amnts[3]) + '\n')
    stonks.write("Cranberry Juice: " + str(amnts[4]) + '\n')
    stonks.write("Lime Juice: " + str(amnts[5]) + '\n')
    stonks.write("Lemon Juice: " + str(amnts[6]) + '\n')
    stonks.write("Coca Cola: " + str(amnts[7]) + '\n')
    stonks.write("Campari: " + str(amnts[8]) + '\n')
    stonks.write("Cointreau: " + str(amnts[9]) + '\n')
    stonks.write("Grenadine: " + str(amnts[10]) + '\n')
    stonks.write("Simple Syrup: " + str(amnts[11]) + '\n')
    stonks.write("Tonic Water: " + str(amnts[12]) + '\n')
    stonks.write("Dry Vermouth: " + str(amnts[13]) + '\n')
    stonks.write("Kahlua: " + str(amnts[14]) + '\n')
    stonks.write("Ice: " + str(amnts[15]) + '\n')
    stonks.write("\nGross Profit: $" + str(profit))
    stonks.close()
    return

def errChk(index, amnts):
    global drinkNames
    drinkList = ""
    for i in index:
        drinkList+= str(drinkNames[i]) + '\n'
    ErrMsg = 'The following ingredients need to be replaced:\n\n%s\n\nBottles Replaced?'%(drinkList)
    Msg = tkMessageBox.askquestion(title= 'Test titel', message = ErrMsg)
    if Msg == 'no':
        errChk(index, amnts)
    else:
        for pos in index:
            amnts[pos] = 20
#    for pos in index:
#        print 'amount: ' + str(amnts[pos])
    return

# This function takes the amnts array as input and uses it to determine if any of the ingredient
# are low in volume (definied as having 2 or less units of ingredient)
# if there are any low ingredients the error display function is called with the indicies of each
# drink in the amnts array being passed to it
def VolCheck(amnts):
    index = [] # Initializes an empty index array to be filled every time function is called
    flag = 0
    for idx, val in enumerate(amnts):
        if val <= 2:
#            print 'item num: ' + str(idx) + ', ' + str(val) # CHANGE TO DISPLAY IN ERROR SECTION
            index.append(idx)
            flag += 1
    if flag > 0:
        errChk(index, amnts)


# Button called function for the Cosmopolitan
def cosmo(amnts): # POINTS DEFINED
    global queue
    queue.append(1)
    VolCheck(amnts)
    global profit
    profit += price
    amnts[0] -= 1 # full shot vodka
    amnts[4] -= 2 # half shots cran
    amnts[5] -= 1 # half shot lime
    amnts[9] -= 1 # half shot cointreau
    global tableDrinks
    tableDrinks += 1
    messageCosmo ='''cosmo\n'''
    text.insert('end', messageCosmo)
    return

# Button called function for the Negroni
def negroni(amnts): # POINTS DEFINED
    global queue
    queue.append(2)
    VolCheck(amnts)
    global profit
    profit += price
    amnts[1] -= 1  # full shots gin
    amnts[8] -= 1  # full shots campari
    amnts[13] -= 2 # half shots vermouth
    amnts[15] -= 1 # 1 full serving ice
    global tableDrinks
    tableDrinks += 1
    messageNegroni ='''negroni\n'''
    text.insert('end', messageNegroni)
    return

# Button called function for the Black Russian
def russian(amnts): # POINTS DEFINED
    global queue
    queue.append(3)
    VolCheck(amnts)
    amnts[0] -= 1  # full shots vodka
    amnts[14] -= 1 # half shots kahlua
    amnts[15] -= 1 # 1 full serving ice
    global tableDrinks
    tableDrinks += 1
    global profit
    profit += price
    messageRuss ='''black russian\n'''
    text.insert('end', messageRuss)
    return

# Button called function for the Long Island Iced Tea
def liit(amnts): # POINTS DEFINED
    global queue
    queue.append(4)
    VolCheck(amnts)
    amnts[0] -= 1  # full shots vodka
    amnts[1] -= 1  # full shots gin
    amnts[2] -= 1  # full shots rum
    amnts[3] -= 1  # full shots tequila
    amnts[6] -= 4  # half shots lemon
    amnts[7] -= 1  # full shots coke
    amnts[9] -= 2  # half shots cointreau
    amnts[11] -= 2  # half shots syrup
    amnts[15] -= 1 # 1 full serving ice
    global tableDrinks
    tableDrinks += 1
    global profit
    profit += price
    messageLiit ='''long island iced tea\n'''
    text.insert('end', messageLiit)
    return

# Button called function for the Cuba Libre
def cuba(amnts): # POINTS DEFINED
    global queue
    queue.append(5)
    VolCheck(amnts)
    amnts[2] -= 1 # full shots rum
    amnts[5] -= 1 # half shots lime
    amnts[7] -= 3 # full shots coke
    amnts[15] -= 1 # 1 full serving ice
    global tableDrinks
    tableDrinks += 1
    global profit
    profit += price
    messageCuba ='''cuba libre\n'''
    text.insert('end', messageCuba)
    return

# Button called function for the John Collins
def john(amnts): # POINTS DEFINED
    global queue
    queue.append(6)
    VolCheck(amnts)
    amnts[1] -= 1  # full shots gin
    amnts[6] -= 2  # half shots lemon
    amnts[11] -= 1 # half shots syrup
    amnts[12] -= 1 # full shots tonic
    amnts[15] -= 1 # 1 full serving ice
    global tableDrinks
    tableDrinks += 1
    global profit
    profit += price
    messageJohn ='''john collins\n'''
    text.insert('end', messageJohn)
    return

# Button called function for the Dry Martini
def dry(amnts): # POINTS DEFINED
    global queue
    queue.append(7)
    VolCheck(amnts)
    amnts[1] -= 1  # full shots gin
    amnts[13] -= 1 # half shot vermouth
    amnts[15] -= 1 # 1 full serving ice
    global tableDrinks
    tableDrinks += 1
    global profit
    profit += price
    messageDry ='''dry martini\n'''
    text.insert('end', messageDry)
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
button1 = Button(root, text="Cosmopolitan",             width=20,height=4, command=lambda: cosmo(amnts)).place(x=570,y=300)
button2 = Button(root, text="Negroni",                  width=20,height=4, command=lambda: negroni(amnts)).place(x=570,y=375)
button3 = Button(root, text="Black Russian",            width=20,height=4, command=lambda: russian(amnts)).place(x=570,y=450)
button4 = Button(root, text="Long Island Iced Tea",     width=20,height=4, command=lambda: liit(amnts)).place(x=790,y=300)
button5 = Button(root, text="Cuba Libre",               width=20,height=4, command=lambda: cuba(amnts)).place(x=790,y=375)
button6 = Button(root, text="John Collins",             width=20,height=4, command=lambda: john(amnts)).place(x=790,y=450)
button7 = Button(root, text="Dry Martini",              width=20,height=4, command=lambda: dry(amnts)).place(x=570,y=525)
button8 = Button(root, text="ORDER",                    width=20,height=4, command=ORDER,bg='#00FF7F').place(x=790,y=525)
button9 = Button(root, text="Check Out",                width=30,height=2, command=lambda: CheckOut(amnts),bg='#FF4040').place(x=640,y=600)
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
photo = Image.open('/home/robotics/Desktop/ERAA/ERAA/Official/LogoNoBack.png' )
resize_image = photo.resize((384,216))
img=ImageTk.PhotoImage(resize_image)
label = Label(root,image = img)
label.place(x=-30,y=30)

root.mainloop()
