
import RPi.GPIO as GPIO ## Import GPIO library
import time
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(11, GPIO.OUT) 
GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT) 
GPIO.setup(16, GPIO.OUT) 

#forward
def forward():
GPIO.output(11,True)
GPIO.output(12,False)
GPIO.output(15,False)
GPIO.output(16,True)
time.sleep(80)

def turn_right():
GPIO.output(11,True)
GPIO.output(12,False)
GPIO.output(15,True)
GPIO.output(16,False)
time.sleep(20)

def turn_left():
GPIO.output(11,False)
GPIO.output(12,True)
GPIO.output(15,False)
GPIO.output(16,True)
time.sleep(20)


forward()
turn_right()
forward()
turn_right()
forward()
turn_right()
forward()
turn_left()
forward()


GPIO.cleanup()
