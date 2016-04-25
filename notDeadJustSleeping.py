import RPi.GPIO as GPIO
import time
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
import datetime
import ConfigParser

# Set variables for pins
switchR = 19 
switchB = 26
ledR = 5
ledG = 6
ledB = 13

# get info from config
config = ConfigParser.ConfigParser()
config.read("./.piScriptsConfig")
gmail_user = config.get("email","gmail_user")
gmail_password = config.get("email","gmail_password")
to = config.get("notDead","to")

# Initialize GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup([switchR, switchB], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup([ledR, ledG, ledB], GPIO.OUT)

# Function to monitor the switches
def monitorSwitch(seconds):
	# loop for the number of seconds, checking for switch press
	timeEnd = time.time() + seconds
	while time.time() < timeEnd:
		if GPIO.input(switchR) == True:
			return notDead()
	return False

# Function to send a "Not dead, just sleeping" message
def notDead():
	# Set LED to red for setup
	GPIO.output(ledR, True)	

	# Setup Gmail SMTP server to send
	smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.
	smtpserver.ehlo()  # Says 'hello' to the server
	smtpserver.starttls()  # Start TLS encryption
	smtpserver.ehlo()
	smtpserver.login(gmail_user, gmail_password)  # Log in to server
	
	# Building email
	msg = MIMEMultipart()
	msg['From'] = gmail_user
	msg['To'] = to
	msg['Subject'] = ""
	text = "Not dead. Just sleeping. Love Max."
	
	# Switch LED to blue for sending
	GPIO.output(ledR, False)
	GPIO.output(ledB, True)
	
	# Send the email to SMS gateway
	smtpserver.sendmail(gmail_user, to, text)
	
	# Closes the smtp server connection
	smtpserver.quit()

	# Switch LED to green for sent
	GPIO.output(ledB, False)
	GPIO.output(ledG, True)
	time.sleep(1)
	GPIO.output(ledG, False)

# Loop until a switch pressed
btnPress = False
while btnPress == False:
	btnPress = monitorSwitch(5)   # Monitor switches

# End and cleanup
GPIO.cleanup()
