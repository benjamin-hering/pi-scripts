import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup([5,6,13], GPIO.OUT)
GPIO.output([5,6,13], False)
GPIO.cleanup()
