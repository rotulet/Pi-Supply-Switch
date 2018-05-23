#!/usr/bin/env python

# Import the modules to send commands to the system and access GPIO pins
import os
import RPi.GPIO as GPIO
from time import sleep

import oled

try:
 oled.init()
 oled.line1("Volumio!")
 oled.line2("Booting...")
finally:
 oled.cleanup()

# Map pin seven and eight on the Pi Switch PCB to chosen pins on the Raspberry Pi header
# The PCB numbering is a legacy with the original design of the board
pinHalt = 27 # GPIO 27
pinWatchDog = 22 # GPIO 22
wdLevel = 1
GPIO.setmode(GPIO.BCM) # Set pin numbering to bcm numbering

try:
 GPIO.setup(pinHalt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set up pinHalt as an input
 GPIO.setup(pinWatchDog, GPIO.OUT, initial=wdLevel) # Setup pinWatchDog as output

 while True: # Setup a while loop to wait for a button press
  if GPIO.input(pinHalt)==1: # Setup an if loop to run a shutdown command when button press sensed
   print("sudo shutdown -h now &\n")
   os.system("sudo shutdown -h now &") # Send shutdown command to os
   sleep(1)
   break

  GPIO.output(pinWatchDog, wdLevel) # alternate pin level pevery 100ms
  if wdLevel==1:
   wdLevel=0
  else:
   wdLevel=1

  sleep(0.1)

except KeyboardInterrupt:
 print("Interrupted!\n")

finally:
 GPIO.cleanup()


