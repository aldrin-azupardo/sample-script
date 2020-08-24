#!/usr/bin/env python
import sys
from time import sleep
from netmiko import ConnectHandler
dev={
	'device_type': 'cisco_ios',
	'host': '192.168.1.x',
	'username': 'user',
	'password': 'passwd',
} # Use a dictionary to pass the login parameters
 
# Connect to the device
router_conn = ConnectHandler(**dev)

# Send the command and print the result
print(router_conn.send_command("show arp\n"))
