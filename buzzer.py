#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time

buzzer_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

# Make buzzer sound
GPIO.output(buzzer_pin, GPIO.HIGH)
time.sleep(2.5)
# Stop buzzer sound
GPIO.output(buzzer_pin, GPIO.LOW)

time.sleep(0.5)
# Make buzzer sound
GPIO.output(buzzer_pin, GPIO.HIGH)
time.sleep(0.5)
# Stop buzzer sound
GPIO.output(buzzer_pin, GPIO.LOW)

time.sleep(0.1)
# Make buzzer sound
GPIO.output(buzzer_pin, GPIO.HIGH)
time.sleep(0.1)
# Stop buzzer sound
GPIO.output(buzzer_pin, GPIO.LOW)

time.sleep(0.2)
# Make buzzer sound
GPIO.output(buzzer_pin, GPIO.HIGH)
time.sleep(0.2)
# Stop buzzer sound
GPIO.output(buzzer_pin, GPIO.LOW)

time.sleep(.02)
# Make buzzer sound
GPIO.output(buzzer_pin, GPIO.HIGH)
time.sleep(.02)
# Stop buzzer sound
GPIO.output(buzzer_pin, GPIO.LOW)

GPIO.cleanup()