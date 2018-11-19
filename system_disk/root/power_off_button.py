#!/bin/python
import RPi.GPIO as GPIO
import os

power_off_pin=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(power_off_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    GPIO.wait_for_edge(power_off_pin, GPIO.FALLING)
    os.system("sudo shutdown -h now")

except:
    pass

GPIO.cleanup()
