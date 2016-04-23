import subprocess
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
import datetime

# Change to your own account information
# Account Information
to = 'XXXXXXXX' # Email to send to.
gmail_user = 'XXXXXXXX' # Email to send from. (MUST BE GMAIL)
gmail_password = 'XXXXXXXXt' # Gmail password.
smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.

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
