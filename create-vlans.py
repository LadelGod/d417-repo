from netmiko import ConnectHandler
import os

device1 = {
    "device_type": "extreme_exos",
    "host": '10.10.1.24' ,
    "username": "admin",
    "password": "",
}
device2 = {
    "device_type": "extreme_exos",
    "host": '10.10.1.22' ,
    "username": "admin",
    "password": "",
}
device3 = {
    "device_type": "extreme_exos",
    "host": '10.10.1.32' ,
    "username": "admin",
    "password": "",
}
device4 = {
    "device_type": "extreme_exos",
    "host": '10.10.1.31' ,
    "username": "admin",
    "password": "",
}
device5 = {
    "device_type": "extreme_exos",
    "host": '10.10.1.30' ,
    "username": "admin",
    "password": "",
}

switchList = (device1, device2, device3, device4, device5)
def create_vlans() : 
    #Prints the starting configuration
    device = device1
    connection = ConnectHandler(**device)
    startingPoint = connection.send_command("show vlan")
    print(startingPoint)

    #Creates the User_Network VLAN
    creation = connection.send_command("create vlan User_Network tag 10")
    print(creation)

    #Adds ports to the User_network VLAN
    addPorts = connection.send_command("configure vlan User_Network add ports 2-5 {untagged}")
    print(addPorts)

    #Prints the new configuration
    newConfig = connection.send_command("show vlan")
    print(newConfig)

    return "New VLANs have been created"

print(create_vlans())