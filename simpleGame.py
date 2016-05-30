import RPi.GPIO as GPIO
import time
import random

# Set variables for pins
switchR = 19 
switchB = 26
ledR = 5
ledG = 6
ledB = 13

# Initialize GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup([switchR, switchB], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup([ledR, ledG, ledB], GPIO.OUT)

# Function to monitor the switches
def monitorSwitches(seconds):
	# loop for the number of seconds, checking for switch press
	timeEnd = time.time() + seconds
	while time.time() < timeEnd:
		if GPIO.input(switchR) == True:
			return announceWinner(switchR)
		if GPIO.input(switchB) == True:
			return announceWinner(switchB)
	return False

# Function to announce a winner
def announceWinner(switch):
	# determine which button was pressed first
	frstBtn = ledR if switch == switchR else ledB
	lastBtn = ledB if switch == switchR else ledR
	# determine which player one
	winner = frstBtn if ledColor == ledG else lastBtn
	# turn of active color and flash winning color
	GPIO.output(ledColor, False)
	for i in range (0, 10):
		GPIO.output(winner, True)
		time.sleep(0.5)
		GPIO.output(winner, False)
		time.sleep(0.5)

# Play the game, loop until a switch pressed
winner = False
while winner == False:
	# select random LED color
	ledColor = random.choice([ledR, ledG, ledB])
	
	GPIO.output(ledColor, True)   # Turn on LED
	winner = monitorSwitches(5)   # Monitor switches
	GPIO.output(ledColor, False)  # turn off LED

# End and cleanup
GPIO.cleanup()
