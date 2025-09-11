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
    startingPoint = connection.send_command("show vlan | grep VR")
    print(startingPoint)

    #Creates the User_Network VLAN
    creation = connection.send_command("create vlan User_Network tag 10")
    print(creation)

    #Prints the new configuration
    newConfig = connection.send_command("show vlan | grep VR")
    print(newConfig)

    #Closes the connection with the switch
    connection.disconnect()

    #Prints the starting configuration
    device = device3
    connection = ConnectHandler(**device)
    startingPoint = connection.send_command("show vlan | grep VR")
    print(startingPoint)

    #Creates the ACCT_Network VLAN
    creation = connection.send_command("create vlan ACCT_Network tag 20")
    print(creation)

    #Prints the new configuration
    newConfig = connection.send_command("show vlan | grep VR")
    print(newConfig)

    #Closes the connection with the switch
    connection.disconnect()

    #Prints the starting configuration
    device = device4
    connection = ConnectHandler(**device)
    startingPoint = connection.send_command("show vlan | grep VR")
    print(startingPoint)

    #Creates the MGMT_Network VLAN
    creation = connection.send_command("create vlan MGMT_Network tag 30")
    print(creation)

    #Prints the new configuration
    newConfig = connection.send_command("show vlan | grep VR")
    print(newConfig)

    #Closes the connection with the switch
    connection.disconnect()

    #Prints the starting configuration
    device = device5
    connection = ConnectHandler(**device)
    startingPoint = connection.send_command("show vlan | grep VR")
    print(startingPoint)

    #Creates the IT_Network VLAN
    creation = connection.send_command("create vlan IT_Network tag 40")
    print(creation)

    #Prints the new configuration
    newConfig = connection.send_command("show vlan | grep VR")
    print(newConfig)

    #Closes the connection with the switch
    connection.disconnect()

    #Prints the starting configuration
    device = device1
    connection = ConnectHandler(**device)
    startingPoint = connection.send_command("show vlan | grep VR")
    print(startingPoint)

    #Creates all VLANs on the central switch
    creation = connection.send_command("create vlan User_Network tag 10")
    print(creation)
    creation = connection.send_command("create vlan ACCT_Network tag 20")
    print(creation)
    creation = connection.send_command("create vlan MGMT_Network tag 30")
    print(creation)
    creation = connection.send_command("create vlan IT_Network tag 40")
    print(creation)

    #Prints the new configuration
    newConfig = connection.send_command("show vlan | grep VR")
    print(newConfig)

    #Closes the connection with the switch
    connection.disconnect()
    return "New VLANs have been created"

print(create_vlans())