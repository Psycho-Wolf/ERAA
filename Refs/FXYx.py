import serial #Dr. Isenbergs' python code to demo the FXYx robot.
import time
import math

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

def origin():
    ser.write("@ORG "+chr(13)+chr(10))  #move to origin
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

#while True:
#	r=100.0
#	theta=0.0
#	while theta<2*math.pi:
#		x=r*math.cos(theta)+100.0
#		y=r*math.sin(theta)+100.0
#		point(round(x,2),round(y,2),100)
#		theta=theta+0.05

#	for k in range(1,10,2):
#	    	point(400,300,20)
#  		point(0,0,20)
#    		point(0,300,20)
#    		point(400,300,20)
#    		point(400,0,20)
#    		point(0,0,20)

while True:
	point(540,300,80)
#time.sleep(2)
#for k in range(1,4,1):
#	point(540,300,40)
#	point(490,320,40)
	time.sleep(1)
	point(100,100,80)
	time.sleep(1)
	point(300,400,100)
	time.sleep(5)




##for k in range(0,100):
##    ser.write("@WRITE PRM "+chr(13)+chr(10))
##    i=0
##    rec=ser.read(1)
##    while rec[i]<>chr(10):
##        rec=rec+ser.read(1)
##        i=i+1
##    print rec
##    ser.write("PRM12="+str(int(speed))+chr(13)+chr(10))
##    ser.write(chr(26))
##    i=0
##    rec=ser.read(1)
##    while rec[i]<>chr(10):
##        rec=rec+ser.read(1)
##        i=i+1
##    print rec
##    ser.write("@X- "+chr(13)+chr(10))
##    
##    speed=(speed+1)
##    print speed
##    time.sleep(.2)
##    ser.write(chr(3))
          
##ser.write("@WRITE PRM"+chr(13)+chr(10))
##i=0
##rec=ser.read(1)
##while rec[i]<>chr(10):
##    rec=rec+ser.read(1)
##    i=i+1
##print rec
##ser.write("PRM12="+str(speed)+chr(13)+chr(10))          
##ser.write("^Z(=1AH)")
##i=0
##rec=ser.read(1)
##while rec[i]<>chr(10):
##    rec=rec+ser.read(1)
##    i=i+1
##print rec



##ser.write("@READ PRM "+chr(13)+chr(10))
##for k in range(0,118):
##    rec=ser.read(21)
##    print rec
##    
##    i=0
##    rec=ser.read(1)
##    while rec[i]<>chr(10):
##        rec=rec+ser.read(1)
##        i=i+1
##    print rec

    

##ser.write("@SRVO "+chr(1)+chr(13)+chr(10))
##i=0
##rec=ser.read(1)
##while rec[i]<>chr(10):
##    rec=rec+ser.read(1)
##    i=i+1
##print rec
          

##ser.write("@MOVD "+str(xposition)+","+str(yposition)+","+str(speed)+chr(13)+chr(10))
###ser.write("@ORG"+chr(32)+chr(13)+chr(32)+chr(10))  #move to origin
##rec=ser.read(4)
##print rec
##
##if rec[0]=="N":
##    i=0
##    rec=ser.read(1)
##    while rec[i]<>chr(10):
##        rec=rec+ser.read(1)
##        i=i+1
##    print rec

ser.close()
