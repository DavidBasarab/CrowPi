#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

RegisterSelect = 23
Enable = 24
DataPin0 = 4
DataPin1 = 17
DataPin2 = 27
DataPin3 = 22
DataPin4 = 5
DataPin5 = 6
DataPin6 = 13
DataPin7 = 19


def set_up_pin(pin_number):
    GPIO.setup(pin_number, GPIO.OUT)
    GPIO.output(pin_number, GPIO.LOW)


set_up_pin(RegisterSelect)
set_up_pin(Enable)
set_up_pin(DataPin0)
set_up_pin(DataPin1)
set_up_pin(DataPin2)
set_up_pin(DataPin3)
set_up_pin(DataPin4)
set_up_pin(DataPin5)
set_up_pin(DataPin6)
set_up_pin(DataPin7)

print("Going to turn the display on")

GPIO.output(RegisterSelect, GPIO.LOW)

GPIO.output(DataPin0, GPIO.HIGH)
GPIO.output(DataPin1, GPIO.HIGH)
GPIO.output(DataPin2, GPIO.HIGH)
GPIO.output(DataPin3, GPIO.HIGH)
GPIO.output(DataPin4, GPIO.LOW)
GPIO.output(DataPin5, GPIO.LOW)
GPIO.output(DataPin6, GPIO.LOW)
GPIO.output(DataPin7, GPIO.LOW)

GPIO.output(Enable, GPIO.HIGH)

# GPIO.setup(ledPin, GPIO.OUT)
# GPIO.output(ledPin, GPIO.LOW)
#
#
# def print_pin_status(pin_number):
#     GPIO.setup(pin_number, GPIO.IN)
#     value = GPIO.input(pin_number)
#     print(f'Current Value of {pin_number} is {value}')
#     GPIO.setup(pin_number, GPIO.OUT)
#
#
# while True:
#     print_pin_status(ledPin)
#
#     key = input("Action, press q to quit: ")
#
#     print(key)
#
#     if key == ' ':
#         print("space pushed")
#
#     if key == '1':
#
#         if pinOn:
#             print("turning led off")
#             GPIO.output(ledPin, GPIO.LOW)
#             pinOn = False
#         else:
#             print("turning led on")
#             GPIO.output(ledPin, GPIO.HIGH)
#             pinOn = True
#
#     if key == 'q':
#         print("Quiting. . .")
#         break


