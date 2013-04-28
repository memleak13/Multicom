#!/usr/bin/python

"""
Version:	0.3 
Author: 	Memleak13
Date: 		11.02.13

Takes a command and device list, reads them, telnets to each device and executes
the commands. The output is saved separately in a file named after the device.
Example of deviceList.txt:

LabSwitch1 172.18.0.193
LabSwitch2 172.18.0.191

Example of commandList.txt:

sh run
sh version
sh int desc
"""

import re
import sys
import time
import telnetlib

def telnet_login(host,ip):
    print ip
    
    #Opening filehandle for output
    fout = open(host, 'w')
        
    #Connecting to host
    tn = telnetlib.Telnet(ip)

    #Login prodedure (unpriv -> enable -> priv)

    tn.expect(regexlist) #regexlist is global
    tn.write(USER + "\n")
    tn.expect(regexlist)
    tn.write(PASSWORD + "\n")
    tn.expect(regexlist)
    tn.write("enable\n")
    tn.expect(regexlist)
    tn.write(PASSWORD + "\n")

    # This works as:
    # it is "pass by value" but all values are just references to objects.
    # http://en.wikipedia.org/wiki/Immutable_object#Python
    exe_command(tn, fout)
        
    # Closing handles
    tn.close()
    fout.close()

    print "Written File: " + host

def exe_command(tn, fout):   
    for command in commandList:
        fout.write("\n\n****************************\n")
        fout.write(command)
        fout.write("****************************\n\n")           
        tn.expect(regexlist) 
        tn.write(command)
        time.sleep(3)
        output = tn.read_very_eager()
        fout.write(output)
        tn.write("\n")
    
    
#Defining global parameters
USER = 'technik'
PASSWORD = 'technik'

# Defining regular expressions for the different prompts
unprivPrompt = re.compile ('.*>')
privPrompt = re.compile ('.*#')
regexlist = [unprivPrompt, privPrompt, 'Username:', 'Password:']

#Creating Filehandles, deviceList.txt, commandList.txt must exist!
fDevice = open ('/Users/business/Desktop/deviceList.txt', 'r')
fCommand = open ('/Users/business/Desktop/commandList.txt', 'r')

#Initializing Devicelist and Commandlist
deviceList = {}
for line in fDevice:
    device = line.split()
    deviceList [device[0]] = device[1]

commandList = []
for command in fCommand:
    commandList.append(command)

#Establishing Connection
for device in deviceList:
    telnet_login(device, deviceList[device])
