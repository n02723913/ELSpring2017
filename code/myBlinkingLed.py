#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
def Blink1():
	 for i in range(0,3):
		 print "blink1 #" + str(i+1)
		 GPIO.output(17,True)
		 time.sleep(1)
		 GPIO.output(17,False)
		 time.sleep(1)
	 print "done blink 1!!"
	 GPIO.cleanup()
def Blink2():
	 for i in range(0,4):
		 print "blink2 #" + str(i+1)
		 GPIO.output(17,True)
		 time.sleep(0.5)
		 GPIO.output(17,False)
		 time.sleep(0.5)
	 print "done!!"
	 GPIO.cleanup()
Blink1()
time.sleep(5)
Blink2()