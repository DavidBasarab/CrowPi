#!/usr/bin/python

from msvcrt import getch
import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

ledPin = 4
escapeKey = b'\x1b'
spaceKey = b' '
oneKey = b'1'
pinOn = False

GPIO.setup(ledPin, GPIO.OUT)

GPIO.ouput(ledPin, 0)

while True:
    key = getch()

    print(key)

    if key == spaceKey:
        print("space pushed")

    if key == oneKey:

        if pinOn:
            print("turning led on")
            GPIO.ouput(ledPin, 0)
            pinOn = False
        else:
            print("turning led off")
            GPIO.ouput(ledPin, 1)
            pinOn = True

    if key == escapeKey:
        print("escape key pressed exiting. . .")
        break


