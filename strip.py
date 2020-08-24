#!/usr/bin/env python
import getpass
import sys
import telnetlib
import datetime
user = raw_input("Enter your username: ")
password = getpass.getpass()

f = open('strip')

for line in f:
  line1 = line[:13]
  line2 = line[14:23]
  #current_date = datetime.datetime.today().strftime ('%b-%d-%Y')
  print "Configuring Switch " + (line1)
  HOST = line1.strip()
  #print(line1 + str(current_date))
  #print(line2 + str(current_date))
  tn = telnetlib.Telnet(HOST)
  tn.read_until("Username: ")
  tn.write(user + "\n")
  if password:
   tn.read_until("Password: ")
   tn.write(password + "\n")

  tn.write("sh clock\n")
  tn.write("exit\n")
  print tn.read_all()
