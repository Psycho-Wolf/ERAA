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

ser=serial.Serial('/dev/ttyS0')
ser.baudrate=9600
ser.parity=serial.PARITY_ODD
ser.stopbits=serial.STOPBITS_ONE
ser.bytesize=serial.EIGHTBITS
ser.xonxoff=1
ser.reset_input_buffer()
ser.reset_output_buffer()

servosOn()
origin()

while True:
	point(350,100,20)
	time.sleep(1)
	point(100,300,100)
	time.sleep(1)
	point(500,400,50)
	time.sleep(5)

ser.close()
