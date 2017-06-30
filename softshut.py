#!/usr/bin/env python

# Import the modules to send commands to the system and access GPIO pins
from subprocess import call
import RPi.GPIO as GPIO
from time import sleep

# Map pin seven and eight on the Pi Switch PCB to chosen pins on the Raspberry Pi header
# The PCB numbering is a legacy with the original design of the board
pinHalt = 22
pinWatchDog = 23
wdLevel = 1
GPIO.setmode(GPIO.BCM) # Set pin numbering to bcm numbering
GPIO.setup(pinHalt, GPIO.IN) # Set up pinHalt as an input
GPIO.setup(pinWatchDog, GPIO.OUT, initial=1) # Setup pinWatchDog as output

while True: # Setup a while loop to wait for a button press
 if (GPIO.input(pinHalt)): # Setup an if loop to run a shutdown command when button press sensed
  os.system("sudo shutdown -h now &") # Send shutdown command to os
  break
 
 else:
  GPIO.output(pinWatchDog, wdLevel) # alternate pin level every 100ms
  if (wdLevel):
   wdLevel=1
  else:
   wdLeve=0

 sleep(0.1)
