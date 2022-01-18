# This is the offical commands module for the robot
import serial
import time
import math

def servosOn():  #turn on all servos
	ser.write("@SRVO "+str(1)+chr(13)+chr(10))
	rec=ser.read(4)
	print("Servo On Reponse=",rec)	#can only return ok
	return

def point(x,y,speed):
    ser.write("@MOVD "+str(x)+","+str(y)+","+str(speed)+chr(13)+chr(10))
    rec=ser.read(4)
    print("Point Response=",rec)
    if rec[0]=="N":
        i=0
        rec=ser.read(1)
        while rec[i]!=chr(10):
            rec=rec+ser.read(1)
            i=i+1
        print(rec)
    return;

def origin():
    ser.write("@ORG "+chr(13)+chr(10))
    rec=ser.read(4)
    print("Origin Response=",rec)
    if rec[0]=="N":
        i=0
        rec=ser.read(1)
        while rec[i]!=chr(10):
            rec=rec+ser.read(1)
            i=i+1
        print(rec)
    else:
        i=0
        rec=ser.read(1)
        while rec[i]!=chr(10):
            rec=rec+ser.read(1)
            i=i+1
        print(rec)
        i=0
        rec=ser.read(1)
        while rec[i]!=chr(10):
            rec=rec+ser.read(1)
            i=i+1
        print(rec)
        i=0
        rec=ser.read(1)
        while rec[i]!=chr(10):
            rec=rec+ser.read(1)
            i=i+1
        print(rec)
    return;
