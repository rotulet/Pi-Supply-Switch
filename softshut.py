#!/usr/bin/env python

# Import the modules to send commands to the system and access GPIO pins
import os
import RPi.GPIO as GPIO
from time import sleep

# Map pin seven and eight on the Pi Switch PCB to chosen pins on the Raspberry Pi header
# The PCB numbering is a legacy with the original design of the board
pinHalt = 23
pinWatchDog = 22
wdLevel = 1
GPIO.setmode(GPIO.BCM) # Set pin numbering to bcm numbering
GPIO.setup(pinHalt, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Set up pinHalt as an input
GPIO.setup(pinWatchDog, GPIO.OUT, initial=wdLevel) # Setup pinWatchDog as output

while True: # Setup a while loop to wait for a button press
 if GPIO.input(pinHalt)==1: # Setup an if loop to run a shutdown command when button press sensed
  os.system("sudo shutdown -h now &") # Send shutdown command to os
  sleep(1)
  break
 
 GPIO.output(pinWatchDog, wdLevel) # alternate pin level every 100ms
 if wdLevel==1:
  wdLevel=0
 else:
  wdLevel=1

 sleep(0.1)

GPIO.cleanup()
