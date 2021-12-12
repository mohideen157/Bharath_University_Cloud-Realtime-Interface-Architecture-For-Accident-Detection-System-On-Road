import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from subprocess import call
fromaddr = "laesrlabs001@gmail.com"
toaddr = "maabdulkhader157@gmail.com"

def mailt():
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "critical alert"
	body = "vibration detected"
	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "12345678910111213")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	print"mail sent"
	server.quit()
mailt()