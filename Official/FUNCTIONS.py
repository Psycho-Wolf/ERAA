# -*- coding: cp1252 -*-
#imports
import serial #Dr. Isenbergs' python code to demo the FXYx robot.
import time
import math
from Tkinter import *
import os
from PIL import ImageTk, Image
import tkMessageBox
#from FXYx import *


ser = serial.Serial('/dev/ttyS0')
ser.baudrate=9600
ser.parity=serial.PARITY_ODD
ser.stopbits=serial.STOPBITS_ONE
ser.bytesize=serial.EIGHTBITS
ser.xonxoff=1
ser.reset_input_buffer()
ser.reset_output_buffer()

def servosOn():  #turn on all servos
	ser.write("@SRVO "+str(1)+chr(13)+chr(10))
	rec=ser.read(4)
	print "Servo On Reponse=",rec	#can only return ok
	return

def point(x,y,speed):
    ser.write("@MOVD "+str(x)+","+str(y)+","+str(speed)+chr(13)+chr(10))
    rec=ser.read(4)
    print "Point Response=",rec
    if rec[0]=="N":
        i=0
        rec=ser.read(1)
        while rec[i]<>chr(10):
            rec=rec+ser.read(1)
            i=i+1
        print rec
    return;

def HomePos():
    ser.write("@MOVD "+str(0)+","+str(40)+","+str(50)+chr(13)+chr(10))
    rec=ser.read(4)
    print "Point Response=",rec
    if rec[0]=="N":
        i=0
        rec=ser.read(1)
        while rec[i]<>chr(10):
            rec=rec+ser.read(1)
            i=i+1
        print rec
    return;

def origin():
    ser.write("@ORG "+chr(13)+chr(10))
    rec=ser.read(4)
    print "Origin Response=",rec
    if rec[0]=="N":
        i=0
        rec=ser.read(1)
        while rec[i]<>chr(10):
            rec=rec+ser.read(1)
            i=i+1
        print rec
    else:
        i=0
        rec=ser.read(1)
        while rec[i]<>chr(10):
            rec=rec+ser.read(1)
            i=i+1
        print rec
        i=0
        rec=ser.read(1)
        while rec[i]<>chr(10):
            rec=rec+ser.read(1)
            i=i+1
        print rec
        i=0
        rec=ser.read(1)
        while rec[i]<>chr(10):
            rec=rec+ser.read(1)
            i=i+1
        print rec
    return;


def cosmoBuild():
    time.sleep(1)
    point(100,100,80)
    time.sleep(1)
    HomePos()
    return

def negroniBuild():
    time.sleep(1)
    point(100,200,80)
    time.sleep(1)
    HomePos()
    return

def russianBuild():
    time.sleep(1)
    point(200,100,80)
    time.sleep(1)
    HomePos()
    return

def liitBuild():
    time.sleep(1)
    point(200,200,80)
    time.sleep(1)
    HomePos()
    return

def cubaBuild():
    time.sleep(1)
    point(200,300,80)
    time.sleep(1)
    HomePos()
    return

def johnBuild():
    time.sleep(1)
    point(300,200,80)
    time.sleep(1)
    HomePos()
    return

def dryBuild():
    time.sleep(1)
    point(300,300,80)
    time.sleep(1)
    HomePos()
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
