# -*- coding: cp1252 -*-
#imports
#import serial #Dr. Isenbergs' python code to demo the FXYx robot.
import time
#import math
from Tkinter import *
import os
from PIL import ImageTk, Image
import tkMessageBox

#from FXYx import *

def cosmo():
    print("making cosmopolitan")
#    time.sleep(5)
#    point(540,300,80)
#    time.sleep(5)
#    origin()
    return

def negroni():
    print("making negroni")
#    time.sleep(5)
#    point(100,100,80)
#    time.sleep(5)
#    origin()
    return

def russian():
    print("making black russian")
#    time.sleep(5)
#    point(540,300,80)
#    time.sleep(5)
#    origin()
    return

def liit():
    print("making long island iced tea")
#    time.sleep(5)
#    point(100,100,80)
#    time.sleep(5)
#    origin()
    return

def cuba():
    print("making cuba libre")
#    time.sleep(5)
#    point(540,300,80)
#    time.sleep(5)
#    origin()
    return

def john():
    print("making john collins")
#    time.sleep(5)
#    point(100,100,80)
#    time.sleep(5)
#    origin()
    return

def dry():
    print("making dry martini")
#    time.sleep(5)
#    point(100,100,80)
#    time.sleep(5)
#    origin()
    return

def settings():
    #staff screen
    boot = Tk()
    boot.title("Lets Fix")
    boot.geometry('350x300')

    def turnOff():
        print("end of the day")
        # ser.close()
        
    # tally up overall profits of day
        
        # volumeLabel = label("vodka: ", excelfile row1 col2).pack()
    # repeat for each ingredient
        return

    def errorDisplay():
        #errorLabel= label(text="check volumes or cups").pack()
        return

    def resolvedError():
        print("errors are fixed")
        #errorLabel= label(text="No errors present").pack()
        return

    def closeSettings():
        boot.destroy()
        return

    buttonReset = Button(boot, text="Shut off",width=20, command=turnOff).pack(padx=5,pady=5)
    buttonErrorResolved = Button(boot, text="Errors Resolved", width=20, command=resolvedError).pack(padx=5,pady=5)
    buttonClose = Button(boot,text="Close",width=20,command=closeSettings).pack(padx=5,pady=5,side=BOTTOM)
    return
