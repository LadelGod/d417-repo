from netmiko import ConnectHandler
import re

def show_vlans(device) :
    connection = ConnectHandler(**device)

    output = connection.send_command("show vlan")
    connection.disconnect()

    vlans = []
    for line in output.splitlines() :
        match = re.match(r"^(\d+)\s+(\S+)", line)
        if match :
            vlan_id = match.group(1)
            name = match.group(2)
            vlans.append((vlan_id, name))
    return vlans

device = {
    "device_type": "EXOS",
    "host": "10.10.1.1",
    "username": "admin",
    "password": "",
}
print(show_vlans())