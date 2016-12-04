import RPi.GPIO as GPIO
import time

# Set pin mode, set pins to output and clear outputs to false
GPIO.setmode(GPIO.BCM)
GPIO.setup([5,6,13], GPIO.OUT)
GPIO.output([5,6,13], False)

# Turns a pin on, waits and then turns off
def pinToggle(pin, duration):
	GPIO.output(pin, True)
	time.sleep(duration)
	GPIO.output(pin, False)

# Cycle through the colors
pinToggle(5, 2)
pinToggle(6, 2)
pinToggle(13, 2)

# Clear everything back to False, cleanup and exit
GPIO.cleanup()
