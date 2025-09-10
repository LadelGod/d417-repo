from netmiko import ConnectHandler

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

switchList = [device1, device2, device3, device4, device5]

outputList = []
def show_vlans(switchList) : 
    i = 0       
    for switch in switchList :
        device = switchList[i]
        connection = ConnectHandler(**device)
        output = connection.send_command("show vlan")
        outputList = outputList.append(output)
        i += 1
    connection.disconnect()
    return outputList


print(show_vlans(switchList))