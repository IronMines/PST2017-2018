#!/bin/usr/python
import RPi.GPIO as GPIO
import time
import serial

ser = serial.Serial(
	port="/dev/ttyS0",
	baudrate=115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

GPIO.setmode(GPIO.BCM)

inputs_IO = [5,6,13,19,26,12]
for i in inputs_IO:
	GPIO.setup(i, GPIO.IN)


ser.isOpen()

print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

input=1
while 1 :
    # get keyboard input
    input = raw_input(">> ")
        # Python 3 users
        # input = input(">> ")
    if input == 'exit':
        ser.close()
        exit()

    if input == 'z':
	ser.write("zmw3030z")

    if input == 's':
        ser.write("zmwC0C0z")

    if input == 'q':
        ser.write("zmw0030z")

    if input == 'd':
        ser.write("zmw3000z")

    else:
        ser.write("zmw0000z")
