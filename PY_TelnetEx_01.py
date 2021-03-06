#!/usr/bin/python

import re
import sys
import time
import telnetlib

#Defining Parameters

HOST = "172.18.0.193"
user = 'technik'
password = 'technik'

# Defining regular expressions for the different prompts
unprivPrompt = re.compile ('.*>')
privPrompt = re.compile ('.*#')
regexlist = [unprivPrompt, privPrompt, 'Username:', 'Password:']

#Connecting to host
tn = telnetlib.Telnet(HOST)

#Login prodedure (unpriv -> enable -> priv)

#print tn.read_until("Username: ")
tn.expect(regexlist)
tn.write(user + "\n")

#print tn.read_until("Password: ")
tn.expect(regexlist)
tn.write(password + "\n")

tn.expect(regexlist)
tn.write("enable\n")

#print tn.read_until("Password: ")
tn.expect(regexlist)
tn.write(password + "\n")

# Executing commands
tn.expect(regexlist)
tn.write("show run\n")
time.sleep(5)
print tn.read_very_eager() 
tn.write("\n")

tn.expect(regexlist)
tn.write("show int des\n")
time.sleep(0.5)
print tn.read_very_eager() 
tn.write("\n")

tn.close()







