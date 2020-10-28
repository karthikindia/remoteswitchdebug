#Author RS
#Version 3.3
#Date 23-Oct-2020

import base64
import paramiko
import netifaces
import os
import datetime

# Test Ping Server
pingcount = 0
# Assign Date Time
timee = datetime.datetime.utcnow()


while pingcount <11:
	hostname = "8.8.8.8" #example
	response = os.system("ping " + hostname)

	if response == 0:
		print(hostname, 'is up!')
		pingcount = 0
		exit
	else:
		print (timee, hostname, 'is down!')
		pingcount+=1
		if pingcount > 9:
			break


# if you need with Keys - Add the following lines
#key = paramiko.RSAKey(data=base64.b64decode(b'AAA...'))
#sshclient.get_hostkeys().add(ConsoleHost,'ssh-rsa',key)
#sshclient.connect(ConsoleHost,username,password)

# Get Client Mac Address

cmacaddr = 'BB:0A:12:04:E0:13'


# Change the following 4 inputs to the required values
APHost = "10.0.0.2"
port = 22
username = "cisuser"
password = "password"

APcommand = "enable ; passwordxxx ; config ap client-trace address add " + cmacaddr + " ; config ap client-trace filter all enable ; config ap client-trace output console-log enable ; config ap client-trace start ; term mom"

sshclient = paramiko.SSHClient()
sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshclient.connect(APHost, port, username, password)

stdin, stdout, stderr = sshclient.exec_command(APcommand)

outputdata = stdout.readlines()
print(outputdata)


# Change the following 4 inputs to the required values

WLCHost = "10.0.0.3"
WLCport = 22
WLCusername = "cisuser"
WLCpassword = "password"

WLCcommand = "debug client" + cmacaddr

sshc = paramiko.SSHClient()
sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshc.connect(WLCHost, WLCport, WLCusername, WLCpassword)

stdin, stdout, stderr = sshc.exec_command(WLCcommand)

Secoutputdata = stdout.readlines()
print(Secoutputdata)
