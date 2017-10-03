import random
import smtplib
import time
import string
import subprocess

fromaddr = 'samrlipton@gmail.com'
username = 'samrlipton@gmail.com'
password = 'Zirconium@42'
server = smtplib.SMTP('smtp.gmail.com:587')
thelist = list(string.ascii_uppercase)
for x in thelist:
	toaddrs =  'V' + x + 'Stover@five-starbank.com'
	msg = "\r\n".join([
		"From: samrlipton@gmail.com",
		"To: " + toaddrs,
		"Subject: Dentist Appointment",
		"",
		"I'm experiencing a large amount of tooth pain and as such scheduled a dentist appointment for tomorrow at 10 am. I will come into work as as soon as the appointment is over."
	])
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit
