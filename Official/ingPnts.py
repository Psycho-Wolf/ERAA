import serial #Dr. Isenbergs' python code to demo the FXYx robot.
import time
import math

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

ser = serial.Serial('/dev/ttyS0')
ser.baudrate=9600
ser.parity=serial.PARITY_ODD
ser.stopbits=serial.STOPBITS_ONE
ser.bytesize=serial.EIGHTBITS
ser.xonxoff=1
ser.reset_input_buffer()
ser.reset_output_buffer()

def vodkaPnt():
    time.sleep(.5)
    point(0,20,80) # Vodka   
    return

def ginPnt():
    #time.sleep(.5)
    point(0,125,80) # Gin   
    return

def rumPnt():
    time.sleep(.5)
    point(0,225,80) # Rum 
    return

def tequilaPnt():
    time.sleep(.5)
    point(0,325,80) # Tequila  
    return

def cranPnt():
    time.sleep(.5)
    point(0,425,80) # Cran
    return

def limePnt():
    point(260,20,80) # Lime
    time.sleep(.5)  
    return

def lemonPnt():
    time.sleep(.5)
    point(260,120,80) # Lemon  
    return

def campPnt():
    #time.sleep(.5)
    point(260,220,80) # Camp  
    return

def coinPnt():
    time.sleep(.5) 
    point(260,320,80) # Coin
    return

def grenPnt():
    time.sleep(.5)
    point(260,420,80) # Grenadine    
    return

def syrupPnt():
    time.sleep(.5)
    point(360,20,80) # Syrup   
    return

def tonicPnt():
    time.sleep(.5)
    point(360,120,80) # Tonic  
    return

def dryPnt():
    #time.sleep(.5)
    point(360,220,80) # Vermouth 
    return

def kahPnt():
    time.sleep(.5)
    point(360,320,80) # Kahlua  
    return

def cokePnt():
    time.sleep(.5)
    point(360,420,80) # Coke   
    return

def sendIt():
    time.sleep(.5)
    point(440,425,50) # Out Drink
    time.sleep(.5)
    return
