#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

ledPin = 18
pinOn = False

GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)


def print_pin_status(pin_number):
    GPIO.setup(pin_number, GPIO.IN)
    value = GPIO.input(pin_number)
    print(f'Current Value of {pin_number} is {value}')
    GPIO.setup(pin_number, GPIO.OUT)


while True:
    print_pin_status(ledPin)

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


