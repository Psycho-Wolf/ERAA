# This is the functions file of Benny that contains many of the actual control functions
#imports
import serial #Dr. Isenbergs' python code to demo the FXYx robot.
import time
import math
from Tkinter import *
import os
from PIL import ImageTk, Image
import tkMessageBox
import cPickle as pickle
#import globals
#from FXYx import *
from ingPnts import *

# The block of code below initilizes the FXYx and turns on the servo motors
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

def servosOff():  #turn off all servos
	ser.write("@SRVO "+str(0)+chr(13)+chr(10))
	rec=ser.read(4)
	print "Servo Off Reponse=",rec	#can only return ok
	return


# This function controls the FXYx, moving back to the origin position
# Inputs: 	x, x, Speed
#	x: Desired position in the X position of the robot workspace
#		Expected values: 0 to 560
#	y: Desired position in the Y position of the robot workspace
#		Expected values: 0 to 460
#	Speed:	Sets the speed at which the robot will move to the desired position.
#	        Expected values: 1 to 100
# Return:	None
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

# This function controls the FXYx, moving back to the Home position
# Inputs: 	None
# Return:	None
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

# This function controls the FXYx, moving back to the origin position
# Inputs: 	None
# Return:	None
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

# This function resets the the ingredient amounts back to the default amount that can be held in
# a bottle which has calculated to be about 20.
# Inputs: 	None
# Return:	None
def ingrSetup():
	amnts = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
	f = open('ingrAmnt.p', 'wb')
	pickle.dump(amnts, f, -1)
	f.close()

	fAmnts = open('i# This is the build function of the Long Island Iced Tea. It controls the robot, moving it to all
# the X & Y positions of the ingredients, cups, and serving location.
# Inputs: 	None
# Return:	NonengrAmnt.p', 'rb')
	test = pickle.load(fAmnts)
	fAmnts.close()
	print test
	return

#def cupSelection(int cupType):
#    if(cupTpye == 1): # Martini glass selection
#        sleep(.5)
#        point(400,10,50)
#	# str(5) moves gripper to height for martini glass
#	ser.write("@DO "+str(5)+chr(44)+str(0)+chr(13)+chr(10))
#	# str(2) waits for martini glass height signal from arduino
#	ser.write("@WAIT "+str(2)+chr(44)+str(1)+chr(13)+chr(10))
#	point(420,10,50)
#	# str(3) closes gripper        
#	ser.write("@DO "+str(3)+chr(44)+str(0)+chr(13)+chr(10))
#        point(400,10,50)
#	# str (1) turns off port
#	ser.write("@DO "+str(5)+chr(44)+str(1)+chr(13)+chr(10))
#	# waits for arduino to zero to Z of the gripper
#	ser.write("@WAIT "+str(3)+chr(44)+str(1)+chr(13)+chr(10))
#	sleep(.5)
#   else if (cupType == 2):
#	
#
#    return

#def serveOp(int cupType):
#    if(cupTpye == 1): # Martini & Lowball glass serve
#    	sleep(.5)    
#	point(390,425,50)
#   	# str(8) moves gripper to height for martini glass out
#   	ser.write("@DO "+str(8)+chr(44)+str(0)+chr(13)+chr(10))
#	# str(2) waits for martini glass height signal from arduino
#	ser.write("@WAIT "+str(2)+chr(44)+str(1)+chr(13)+chr(10))
#	point(440,425,50)
#	# str(3) & str(1) opens the gripper
#	ser.write("@DO "+str(3)+chr(44)+str(1)+chr(13)+chr(10))
#	point(390,425,50)
#   	# str(8) moves gripper to zero height
#   	ser.write("@DO "+str(8)+chr(44)+str(1)+chr(13)+chr(10))
#	# str(2) waits for zero signal from arduino
#	ser.write("@WAIT "+str(3)+chr(44)+str(1)+chr(13)+chr(10))
#    else if(cupTpye == 2): # Highball
#    	sleep(.5)    
#	point(390,425,50)
#   	# str(9) moves gripper to height for martini glass out
#   	ser.write("@DO "+str(9)+chr(44)+str(0)+chr(13)+chr(10))
#	# str(2) waits for martini glass height signal from arduino
#	ser.write("@WAIT "+str(2)+chr(44)+str(1)+chr(13)+chr(10))
#	point(440,425,50)
#	# str(3) & str(1) opens the gripper
#	ser.write("@DO "+str(3)+chr(44)+str(1)+chr(13)+chr(10))
#	point(390,425,50)
#   	# str(9) moves gripper to zero height
#   	ser.write("@DO "+str(9)+chr(44)+str(1)+chr(13)+chr(10))
#	# str(2) waits for zero signal from arduino
#	ser.write("@WAIT "+str(3)+chr(44)+str(1)+chr(13)+chr(10))
#    return
#return
#
#def ingrPour(int cupType):
#    if(cupTpye == 1): # Martini & Lowball
#   	# str(6) moves gripper to ingr height
#   	ser.write("@DO "+str(6)+chr(44)+str(0)+chr(13)+chr(10))
#	# str(2) waits for confirmation signal from arduino
#	ser.write("@WAIT "+str(2)+chr(44)+str(1)+chr(13)+chr(10))
#   	# str(6) moves gripper to zero
#   	ser.write("@DO "+str(6)+chr(44)+str(1)+chr(13)+chr(10))
#	# str(2) waits for zero confirmation signal from arduino
#	ser.write("@WAIT "+str(3)+chr(44)+str(1)+chr(13)+chr(10))
#   else if (cupType == 2): # Highball
#  	# str(7) moves gripper to ingr height
#  	ser.write("@DO "+str(7)+chr(44)+str(0)+chr(13)+chr(10))
#	# str(2) waits for confirmation signal from arduino
#	ser.write("@WAIT "+str(2)+chr(44)+str(1)+chr(13)+chr(10))
#   	# str(7) moves gripper to zero0
#   	ser.write("@DO "+str(7)+chr(44)+str(1)+chr(13)+chr(10))
#	# str(2) waits for zero confirmation signal from arduino
#	ser.write("@WAIT "+str(3)+chr(44)+str(1)+chr(13)+chr(10))
#    return
#return
#
# This is the build function of the Long Island Iced Tea. It controls the robot, moving it to all
# the X & Y positions of the ingredients, cups, and serving location.
# Inputs: 	None
# Return:	None
# This is the build function of the Cosmopolitan. It controls the robot, moving it to all
# the X & Y positions of the ingredients, cups, and serving location.
# Inputs: 	None
# Return:	None
# Notes: 	This code contains various commented out functions that were never officialy
#		implemented due to hardware issues.
def cosmoBuild():
    #int cupType = 1 # Martini
    #cupSelection(cupType)
    vodkaPnt()
    #ingrPour(cupType)
    cranPnt()
    #ingrPour(cupType)
    limePnt()
    #ingrPour(cupType)
    coinPnt()
    #ingrPour(cupType)
    #serveOp(cupType)
    HomePos()
    return

# This is the build function of the Negroni. It controls the robot, moving it to all
# the X & Y positions of the ingredients, cups, and serving location.
# Inputs: 	None
# Return:	None
def negroniBuild():
    ginPnt()
    campPnt()
    dryPnt()
    sendIt()
    HomePos()
    return

# This is the build function of the Black Russian. It controls the robot, moving it to all
# the X & Y positions of the ingredients, cups, and serving location.
# Inputs: 	None
# Return:	None
def russianBuild():
    vodkaPnt()
    kahPnt()
    sendIt()
    HomePos()
    return

# This is the build function of the Long Island Iced Tea. It controls the robot, moving it to all
# the X & Y positions of the ingredients, cups, and serving location.
# Inputs: 	None
# Return:	None
def liitBuild():
    syrupPnt()
    vodkaPnt()
    ginPnt()
    rumPnt()
    tequilaPnt()
    lemonPnt()
    limePnt()
    cokePnt()
    sendIt()
    HomePos()
    return

# This is the build function of the Cuba Libre. It controls the robot, moving it to all
# the X & Y positions of the ingredients, cups, and serving location.
# Inputs: 	None
# Return:	None
def cubaBuild():
    rumPnt()
    limePnt()
    cokePnt()
    sendIt()
    HomePos()
    return

# This is the build function of the John Collins. It controls the robot, moving it to all
# the X & Y positions of the ingredients, cups, and serving location.
# Inputs: 	None
# Return:	None
def johnBuild():
    ginPnt()
    lemonPnt()
    syrupPnt()
    tonicPnt()
    sendIt()
    HomePos()
    return

# This is the build function of the Dry Martini. It controls the robot, moving it to all
# the X & Y positions of the ingredients, cups, and serving location.
# Inputs: 	None
# Return:	None
def dryBuild():
    ginPnt()
    dryPnt()
    sendIt()
    HomePos()

    return

# This function defines and creats the staff screen. Placing all buttons on the staff screen window
# and assigning the proper function to the buttons. Some of the controls of this window include:
#	1) Ending the day and clearing tabs
#	2) Resetting the ingredient ammounts
# Inputs: 	None
# Return:	None
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
        # volumeLabel = label("vodka: ", excelfile row1 col2).pack()

        return

    def errorDisplay():
        #errorLabel= label(text="check volumes or cups").pack()
        return

    def resolvedError():
        ingrSetup()
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
