#!/usr/bin/env python3
from netmiko import ConnectHandler

asw1 = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.1.x",
    "username" : "cisco",
    "password" : "admin",
}
asw2 = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.1.x",
    "username" : "cisco",
    "password" : "admin",
}
asw3 = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.1.x",
    "username" : "cisco",
    "password" : "admin",
}
asw4 = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.1.x",
    "username" : "cisco",
    "password" : "admin",
}
asw5 = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.1.x",
    "username" : "cisco",
    "password" : "admin",
}
asw6 = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.1.x",
    "username" : "cisco",
    "password" : "admin",
}
core = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.1.x",
    "username" : "cisco",
    "password" : "admin"
}

all_devices = [asw1,asw2,asw3,asw4,asw5,asw6,core]
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = (net_connect.send_command('show run | inc hostname'))[9:29]
    print ()
    print (output)
    print ()
