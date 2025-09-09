from netmiko import ConnectHandler
import re

def show_vlans(device) :
    connection = ConnectHandler(**device)

    output = connection.send_command("show vlan")
    connection.disconnect()

    vlans = []
    for line in output.splitlines() :
        match = re.match(r"(10.10.\d{1,3}\.\d{1,3})",line)
        if match :
            vlan_ip = match
            vlans.append((vlan_ip))
    return vlans

device = {
    "device_type": "extreme_exos",
    "host": "10.10.1.22",
    "username": "admin",
    "password": "",
}
print(show_vlans(device))
