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
    device = device2
    connection = ConnectHandler(**device)
    startingPoint = connection.send_command("show vlan")
    print(startingPoint)

    #Creates the User_Network VLAN
    creation = connection.send_command("create vlan User_Network tag 10")
    print(creation)

    #Adds ports & trunk to the User_network VLAN
    addPorts = connection.send_command("configure vlan 10 add port 2-5 untagged")
    addTrunk = connection.send_command("configure vlan 10 add port 1 tagged")
    print(addPorts)
    print(addTrunk)

    #Prints the new configuration
    newConfig = connection.send_command("show vlan")
    print(newConfig)

    #Closes the connection with the switch
    connection.disconnect()

    #Prints the starting configuration
    device = device3
    connection = ConnectHandler(**device)
    startingPoint = connection.send_command("show vlan")
    print(startingPoint)

    #Creates the User_Network VLAN
    creation = connection.send_command("create vlan ACCT_Network tag 20")
    print(creation)

    #Adds ports & trunk to the User_network VLAN
    addPorts = connection.send_command("configure vlan 20 add port 2 untagged")
    addTrunk = connection.send_command("configure vlan 20 add port 1 tagged")
    print(addPorts)
    print(addTrunk)

    #Prints the new configuration
    newConfig = connection.send_command("show vlan")
    print(newConfig)

    #Closes the connection with the switch
    connection.disconnect()

    #Prints the starting configuration
    device = device4
    connection = ConnectHandler(**device)
    startingPoint = connection.send_command("show vlan")
    print(startingPoint)

    #Creates the User_Network VLAN
    creation = connection.send_command("create vlan MGMT_Network tag 30")
    print(creation)

    #Adds ports & trunk to the User_network VLAN
    addPorts = connection.send_command("configure vlan 30 add port 2 untagged")
    addTrunk = connection.send_command("configure vlan 30 add port 1 tagged")
    print(addPorts)
    print(addTrunk)

    #Prints the new configuration
    newConfig = connection.send_command("show vlan")
    print(newConfig)

    #Closes the connection with the switch
    connection.disconnect()

    #Prints the starting configuration
    device = device5
    connection = ConnectHandler(**device)
    startingPoint = connection.send_command("show vlan")
    print(startingPoint)

    #Creates the User_Network VLAN
    creation = connection.send_command("create vlan IT_Network tag 40")
    print(creation)

    #Adds ports & trunk to the User_network VLAN
    addPorts = connection.send_command("configure vlan 40 add port 2 untagged")
    addTrunk = connection.send_command("configure vlan 40 add port 1 tagged")
    print(addPorts)
    print(addTrunk)

    #Prints the new configuration
    newConfig = connection.send_command("show vlan")
    print(newConfig)

    #Closes the connection with the switch
    connection.disconnect()

    #Prints the starting configuration
    device = device1
    connection = ConnectHandler(**device)
    startingPoint = connection.send_command("show vlan")
    print(startingPoint)

    #Creates the User_Network VLAN
    creation = connection.send_command("create vlan User_Network tag 10")
    print(creation)
    creation = connection.send_command("create vlan ACCT_Network tag 20")
    print(creation)
    creation = connection.send_command("create vlan MGMT_Network tag 30")
    print(creation)
    creation = connection.send_command("create vlan IT_Network tag 40")
    print(creation)
    
    #Adds ports & trunk to the User_network VLAN
    addPorts = connection.send_command("configure vlan 40 add port 3 untagged")
    print(addPorts)
    addPorts = connection.send_command("configure vlan 30 add port 5 untagged")
    print(addPorts)
    addPorts = connection.send_command("configure vlan 20 add port 7 untagged")
    print(addPorts)
    addPorts = connection.send_command("configure vlan 10 add port 9 untagged")
    print(addPorts)
    addTrunk = connection.send_command("configure vlan 10,20,30,40 add port 12 tagged")
    print(addPorts)
    print(addTrunk)

    #Prints the new configuration
    newConfig = connection.send_command("show vlan")
    print(newConfig)

    #Closes the connection with the switch
    connection.disconnect()
    return "New VLANs have been created"

print(create_vlans())