#!/usr/bin/env python
import sys
from time import sleep
import paramiko
import os
import datetime

USER="username"
PASSWD="passwd"

f = open('cisco_routerswitch')
for line in f:
  print "Configuring Switch" + (line)
  HOST = line.strip()
# Create an ssh connection
  conn = paramiko.SSHClient()
  conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  conn.connect(HOST, username=USER, password=PASSWD)
  switch_conn = conn.invoke_shell()
  print('Successfully connected to %s' % HOST)
# Send the command and backup to tftp server file saved as config.txt
  switch_conn.send("copy running-config tftp://192.168.2.33/config.txt\n")
  switch_conn.send('\n')
  sleep(1)
  switch_conn.send('\n')
  sleep(1)
#config.txt renamed to ASW** with present date
  current_date = datetime.datetime.today().strftime ('%b-%d-%Y')
  os.rename(r'/tftpboot/config.txt',r'/tftpboot/PRCI-'+ str(line) + str(current_date) + '.cfg')
  print('Backup completed for %s' % HOST)
conn.close

