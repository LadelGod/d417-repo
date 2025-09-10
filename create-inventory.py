import configparser

config = configparser.ConfigParser()

#This section adds the network switches
config.add_section('Local_Switch')
config['Local_Switch'] = {'name':'Local_Switch','ip':'10.10.1.24','RAM': '512MB','vCPU': '1','QEMU Binary': '/usr/bin/qemu-system-x86_64(v4.3.1)','Boot Priority': 'CD/DVD-ROM or HDD','On Close Behavior': 'Power off the VM','Console Type': 'telnet','# of Adapters': '13','Base MAC address': '0c:c0:5e:66:00:00','Adapter Type': 'Realtek 8139 Ethernet (rtl8139)','Replicate network connection states in QEMU': 'True'}
config.add_section('User_Network')
config['User_Network'] = {'name':'User_Network','ip':'10.10.1.22','RAM': '512MB','vCPU': '1','QEMU Binary': '/usr/bin/qemu-system-x86_64(v4.3.1)','Boot Priority': 'CD/DVD-ROM or HDD','On Close Behavior': 'Power off the VM','Console Type': 'telnet','# of Adapters': '13','Base MAC address': '0c:e0:f2:0b:00:00','Adapter Type': 'Realtek 8139 Ethernet (rtl8139)','Replicate network connection states in QEMU': 'True'}
config.add_section('ACCT_Network')
config['ACCT_Network'] = {'name':'ACCT_Network','ip':'10.10.1.32','RAM': '512MB','vCPU': '1','QEMU Binary': '/usr/bin/qemu-system-x86_64(v4.3.1)','Boot Priority': 'CD/DVD-ROM or HDD','On Close Behavior': 'Power off the VM','Console Type': 'telnet','# of Adapters': '13','Base MAC address': '0c:40:34:07:00:00','Adapter Type': 'Realtek 8139 Ethernet (rtl8139)','Replicate network connection states in QEMU': 'True'}
config.add_section('MGMT_Network')
config['MGMT_Network'] = {'name':'MGMT_Network','ip':'10.10.1.31','RAM': '512MB','vCPU': '1','QEMU Binary': '/usr/bin/qemu-system-x86_64(v4.3.1)','Boot Priority': 'CD/DVD-ROM or HDD','On Close Behavior': 'Power off the VM','Console Type': 'telnet','# of Adapters': '13','Base MAC address': '0c:cc:78:5d:00:00','Adapter Type': 'Realtek 8139 Ethernet (rtl8139)','Replicate network connection states in QEMU': 'True'}
config.add_section('IT_Network')
config['IT_Network'] = {'name':'IT_Network','ip':'10.10.1.30','RAM': '512MB','vCPU': '1','QEMU Binary': '/usr/bin/qemu-system-x86_64(v4.3.1)','Boot Priority': 'CD/DVD-ROM or HDD','On Close Behavior': 'Power off the VM','Console Type': 'telnet','# of Adapters': '13','Base MAC address': '0c:1c:b2:85:00:00','Adapter Type': 'Realtek 8139 Ethernet (rtl8139)','Replicate network connection states in QEMU': 'True'}

#This section add the end user devices on the network
config.add_section('WindowsDesktop-1')
config['WindowsDesktop-1'] = {'name':'WindowsDesktop-1','ip':'10.10.1.35','RAM': '4096MB','vCPU': '2','QEMU Binary': '/bin/qemu-system-x86_64(v4.2.1)','Boot Priority': 'HDD','On Close Behavior': 'Send the Shutdwon signal(ACPI)', 'Console Type':'vnc','# of Adapters': '1','Base MAC address': '0c:4b:3c:0a:00:00','Adapter Type':'Intel Gigabit Ethernet (e1000)','Replicate network connection states in QEMU': 'True'}
config.add_section('WindowsDesktop-2')
config['WindowsDesktop-2'] = {'name':'WindowsDesktop-2','ip':'10.10.1.36','RAM': '4096MB','vCPU': '2','QEMU Binary': '/bin/qemu-system-x86_64(v4.2.1)','Boot Priority': 'HDD','On Close Behavior': 'Send the Shutdwon signal(ACPI)', 'Console Type':'vnc','# of Adapters': '1','Base MAC address': '0c:59:fd:86:00:00','Adapter Type':'Intel Gigabit Ethernet (e1000)','Replicate network connection states in QEMU': 'True'}
config.add_section('WindowsDesktop-3')
config['WindowsDesktop-3'] = {'name':'WindowsDesktop-3','ip':'10.10.1.43','RAM': '4096MB','vCPU': '2','QEMU Binary': '/bin/qemu-system-x86_64(v4.2.1)','Boot Priority': 'HDD','On Close Behavior': 'Send the Shutdwon signal(ACPI)', 'Console Type':'vnc','# of Adapters': '1','Base MAC address': '0c:e2:07:f3:00:00','Adapter Type':'Intel Gigabit Ethernet (e1000)','Replicate network connection states in QEMU': 'True'}
config.add_section('WindowsDesktop-4')
config['WindowsDesktop-4'] = {'name':'WindowsDesktop-4','ip':'10.10.1.29','RAM': '4096MB','vCPU': '2','QEMU Binary': '/bin/qemu-system-x86_64(v4.2.1)','Boot Priority': 'HDD','On Close Behavior': 'Send the Shutdwon signal(ACPI)', 'Console Type':'vnc','# of Adapters': '1','Base MAC address': '0c:46:74:35:00:00','Adapter Type':'Intel Gigabit Ethernet (e1000)','Replicate network connection states in QEMU': 'True'}
config.add_section('Test_Box_1')
config['Test_Box_1'] = {'name':'Test_Box_1','ip':'10.10.1.56','RAM': '4096MB','vCPU': '2','QEMU Binary': '/bin/qemu-system-x86_64(v4.2.1)','Boot Priority': 'HDD','On Close Behavior': 'Send the Shutdwon signal(ACPI)', 'Console Type':'vnc','# of Adapters': '1','Base MAC address': '0c:cb:a8:90:00:00','Adapter Type':'Intel Gigabit Ethernet (e1000)','Replicate network connection states in QEMU': 'True'}
config.add_section('Test_Box_2')
config['Test_Box_2'] = {'name':'Test_Box_2','ip':'10.10.1.57','RAM': '4096MB','vCPU': '2','QEMU Binary': '/bin/qemu-system-x86_64(v4.2.1)','Boot Priority': 'HDD','On Close Behavior': 'Send the Shutdwon signal(ACPI)', 'Console Type':'vnc','# of Adapters': '1','Base MAC address': '0c:50:a2:8a:00:00','Adapter Type':'Intel Gigabit Ethernet (e1000)','Replicate network connection states in QEMU': 'True'}

#This section creates & writes the file to the disk
with open('inventory.ini', 'w') as f:
    try:
        config.write(f)
    except:
        print('An error has occured.')
    else:
        print('The inventory.ini file has been created successfully!')
