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
#i = 0
def show_vlans(switchList) : 
    for index, switch in enumerate(switchList) :
        device = switchList(index)
        connection = ConnectHandler(**device)
        output = connection.send_command("show vlan")
        print(output + '\n' + str(index) + '\n')
        if index == 0:
            with open('vlans-list.txt', 'w') as f:
                try:
                    f.write(output)
                except:
                    print('An error has occured while writing to vlans-list.txt. Moving on to next device.')
                else:
                    continue
        else :
            with open('vlans-list.txt', 'a') as f:
                try:
                    f.write(output)
                except:
                    print('An error has occured while writing to vlans-list.txt. Moving on to next device.')
                else:
                    continue
        connection.disconnect()
#        i = i + 1
    return "All VLANs have been queried."


print(show_vlans(switchList))