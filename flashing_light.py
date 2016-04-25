# import the necessary libraries
import RPi.GPIO as GPIO
import time

# initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

# define a function to turn the light on and off
def blinkOnce(pin, wait):
	GPIO.output(pin,True)
	time.sleep(wait)
	GPIO.output(pin,False)
	time.sleep(wait)
	return

# use blinkOnce function in a loop, then cleanup
for i in range(0,100):
	blinkOnce(4,.1)
GPIO.cleanup()
