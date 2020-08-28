#!/usr/bin/env python3
from netmiko import ConnectHandler

asw1 = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.1.253",
    "username" : "jay.borabo",
    "password" : "gabales07",
}
asw2 = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.1.252",
    "username" : "jay.borabo",
    "password" : "gabales07",
}
asw3 = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.1.251",
    "username" : "jay.borabo",
    "password" : "gabales07",
}
asw4 = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.1.250",
    "username" : "jay.borabo",
    "password" : "gabales07",
}
asw5 = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.1.249",
    "username" : "jay.borabo",
    "password" : "gabales07",
}
asw6 = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.1.240",
    "username" : "jay.borabo",
    "password" : "gabales07",
}
core = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.1.254",
    "username" : "jay.borabo",
    "password" : "gabales07"
}

all_devices = [asw1,asw2,asw3,asw4,asw5,asw6,core]
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = (net_connect.send_command('show run | inc hostname'))[9:29]
    print ()
    print (output)
    print ()
