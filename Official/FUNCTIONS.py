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

def cosmoBuild():
    time.sleep(5)
    point(540,300,80)
    time.sleep(5)
    origin()
    return

def negroniBuild():
#    time.sleep(5)
#    point(100,100,80)
#    time.sleep(5)
#    origin()
    return

def russianBuild():
#    time.sleep(5)
#    point(540,300,80)
#    time.sleep(5)
#    origin()
    return

def liitBuild():
#    time.sleep(5)
#    point(100,100,80)
#    time.sleep(5)
#    origin()
    return

def cubaBuild():
#    time.sleep(5)
#    point(540,300,80)
#    time.sleep(5)
#    origin()
    return

def johnBuild():
#    time.sleep(5)
#    point(100,100,80)
#    time.sleep(5)
#    origin()
    return

def dryBuild():
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
        file = open("tab.txt","r")
        lines = file.readlines()
        file.close()
        file = open("tab.txt","w")
        for line in lines:
            file.write(" ")
        file.close()
        
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
