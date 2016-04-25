import subprocess
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
import datetime
import ConfigParser

# Change to your own account information
# Account Information
config = ConfigParser.ConfigParser()
config.read("./.piScriptsConfig")
gmail_user = config.get("email","gmail_user")
gmail_password = config.get("email","gmail_password")
to = config.get("ipMailStart","to")

smtpserver.ehlo()  # Says 'hello' to the server
smtpserver.starttls()  # Start TLS encryption
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)  # Log in to server

arg='ifconfig | grep -Po "inet addr:.+Bcast"'  # Linux command to retrieve ip addresses.
# Runs 'arg' in a 'hidden terminal'.
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()  # Get data from 'p terminal'.
#print data
datastring = str(data)
#print datastring
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = to
msg['Subject'] = "IP Address"

msg.attach(MIMEText(datastring, 'plain'))
text = msg.as_string()
smtpserver.sendmail(gmail_user, to, text)
# Closes the smtp server.
smtpserver.quit()
