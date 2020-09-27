#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

ledPin = 21
pinOn = False

GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)

while True:
    key = input("Action, press q to quit: ")

    print(key)

    if key == ' ':
        print("space pushed")

    if key == '1':

        if pinOn:
            print("turning led off")
            GPIO.output(ledPin, GPIO.LOW)
            pinOn = False
        else:
            print("turning led on")
            GPIO.output(ledPin, GPIO.HIGH)
            pinOn = True

    if key == 'q':
        print("Quiting. . .")
        break


