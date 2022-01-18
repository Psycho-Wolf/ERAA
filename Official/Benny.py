# Introducing Benny, the autonomous bartender robot!

import math
import numpy
from tkinter import *
#from Commands import *
from TestCommands import *

#ingr is an array that stores the available shots of every ingredient used for the recipes
# the order of the indredients is as follows: vodka, gin, rum, tequila, coke, cran, lime
# lemon, kahlua, campari, vermouth, cointreau, simple syrup, tonic, 
global ingr
ingr = numpy.array([20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20])

root = Tk()
root.title('Benny')
root.configure(bg = '#3CDFE4')
exit = Button(root, text = "Exit Program", command = root.quit).grid(row = 5, columnspan = 3)

def checkIngr():
    return

def clearErrors():
    return

def mvOrigin():
    origin()
    home = Button(root, text = "Move to origin", state = DISABLED).grid(row = 0, column = 0)
    return

def Cosmo():
    home = Button(root, text = "Move to origin", command = mvOrigin).grid(row = 0, column = 0)
    bCosmo()
    return

def Negroni():
    home = Button(root, text = "Move to origin", command = mvOrigin).grid(row = 0, column = 0)
    bNegroni()
    return

def Cuba():
    home = Button(root, text = "Move to origin", command = mvOrigin).grid(row = 0, column = 0)
    bCuba()
    return

def Collins():
    home = Button(root, text = "Move to origin", command = mvOrigin).grid(row = 0, column = 0)
    bCollins()
    return

def Russian():
    home = Button(root, text = "Move to origin", command = mvOrigin).grid(row = 0, column = 0)
    bRussian()
    return

def IceT():
    home = Button(root, text = "Move to origin", command = mvOrigin).grid(row = 0, column = 0)
    bIceT()
    return

def Martini():
    home = Button(root, text = "Move to origin", command = mvOrigin).grid(row = 0, column = 0)
    bMartini()
    return

def rmAlcohol():

    return

home = Button(root, text = "Move to origin", command = mvOrigin).grid(row = 0, column = 0)

Cosmo = Button(root, text = "Cosmopolitan", command = Cosmo, bg = '#1A6163', fg = '#FFFFFF', padx = 40, pady = 20).grid(row = 1, column = 1)
Negroni = Button(root, text = "Negroni", command = Negroni, bg = '#1A6163', fg = '#FFFFFF', padx = 40, pady = 20).grid(row = 1, column = 2)
Cuba = Button(root, text = "Cuba Libre", command = Cuba, bg = '#1A6163', fg = '#FFFFFF', padx = 42, pady = 20).grid(row = 2, column = 1)
Collins = Button(root, text = "John Collins", command = Collins, bg = '#1A6163', fg = '#FFFFFF', padx = 40, pady = 20).grid(row = 2, column = 2)
Russian = Button(root, text = "Black Russian", command = Russian, bg = '#1A6163', fg = '#FFFFFF', padx = 40, pady = 20).grid(row = 3, column = 1)
IceT = Button(root, text = "Long Island \nIce Tea", command = IceT, bg = '#1A6163', fg = '#FFFFFF', padx = 40, pady = 20).grid(row = 3, column = 2)
Martini = Button(root, text = "Dry Martini", command = Martini, bg = '#1A6163', fg = '#FFFFFF', padx = 40, pady = 20).grid(row = 4, column = 1)

drinks = Label(root, text = "Drinks:").grid(row = 0, column = 1, columnspan = 2)
errors = Label(root, text = "Errors:").grid(row = 1, column = 0)
clearErrors = Button(root, text = "Errors Resolved", command = clearErrors, bg = '#1A6163', fg = '#FFFFFF', padx = 20, pady = 10).grid(row = 4, column = 0)



root.mainloop()