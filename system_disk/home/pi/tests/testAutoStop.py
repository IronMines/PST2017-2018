#!/bin/usr/python
import RPi.GPIO as GPIO
import time
import serial
GPIO.setmode(GPIO.BCM)



inputs_IO = [5,6,13,19,26,12]
for i in inputs_IO:
	GPIO.setup(i, GPIO.IN)

ser = serial.Serial(
	port="/dev/ttyS0",
	baudrate=115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)
ser = serial.Serial(
	port="/dev/ttyS0",
	baudrate=115200,
	parity=serial.PARITY_NONE,
	stopbits=1,
	bytesize=8
)
ser.isOpen()
ser.write("z")
time.sleep(0.5)
ser.write("mc")
time.sleep(0.5)
ser.write("mw30")
time.sleep(0.05)
ser.write("z")
time.sleep(0.05)

print("Motor on")

run = True
while run:
	l = "0" if GPIO.input(5)==1 else "1"
	fl = "0" if GPIO.input(19)==1 else "1"
	f = "0" if GPIO.input(6)==1 else "1"
	fr = "0" if GPIO.input(26)==1 else "1"
	r = "0" if GPIO.input(13)==1 else "1"
	b = "0" if GPIO.input(12)==1 else "1"
	test = l + fl + f + fr + r + b
	if( test != "000000" ):
		ser.write("mc")
		time.sleep(0.05)
		ser.write("z")
		run = False
		print("Wall detected")
		print "Left\t| Front Left\t| Front\t| Front Right\t| Right\t| Behind"
		print " "+l+"\t| "+fl+"\t\t| "+f+"\t| "+fr+"\t\t| "+r+"\t|"+b
print("Bye")