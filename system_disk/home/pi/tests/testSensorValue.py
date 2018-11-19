#!/bin/usr/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

inputs_IO = [5,6,13,19,26,12]
for i in inputs_IO:
	GPIO.setup(i, GPIO.IN)

pass
#print "Left : " + GPIO.input(5)
#print "Right : " + GPIO.input(13)
#print "Behind : " + GPIO.input(12)
#print "Front : " + GPIO.input(6)
#print "Front Left : " + GPIO.input(19)
#print "Front Right : " + GPIO.input(26)
print "Left\t| Front Left\t| Front\t| Front Right\t| Right\t| Behind"
while True:
	l = "0" if GPIO.input(5)==1 else "1"
	fl = "0" if GPIO.input(19)==1 else "1"
	f = "0" if GPIO.input(6)==1 else "1"
	fr = "0" if GPIO.input(26)==1 else "1"
	r = "0" if GPIO.input(13)==1 else "1"
	b = "0" if GPIO.input(12)==1 else "1"
	print " "+l+"\t| "+fl+"\t\t| "+f+"\t| "+fr+"\t\t| "+r+"\t|"+b
	time.sleep(0.5)
