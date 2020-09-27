#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

ledPin = 4
pinOn = False

GPIO.setup(ledPin, GPIO.OUT)
GPIO.ouput(ledPin, 0)


while True:
    key = input("Action, press q to quit: ")

    print(key)

    if key == ' ':
        print("space pushed")

    if key == '1':

        if pinOn:
            print("turning led off")
            GPIO.ouput(ledPin, 0)
            pinOn = False
        else:
            print("turning led on")
            GPIO.ouput(ledPin, 1)
            pinOn = True

    if key == 'q':
        print("escape key pressed exiting. . .")
        break


