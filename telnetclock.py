#!/usr/bin/env python
import getpass
import sys
import telnetlib
user = raw_input("Enter your username: ")
password = getpass.getpass()

f = open('cisco_routerswitch')

for line in f:
  print "Configuring Switch " + (line)
  HOST = line.strip()
  tn = telnetlib.Telnet(HOST)
  tn.read_until("Username: ")
  tn.write(user + "\n")
  if password:
   tn.read_until("Password: ")
   tn.write(password + "\n")

  tn.write("sh arp\n")
  tn.write("exit\n")
  print tn.read_all()
