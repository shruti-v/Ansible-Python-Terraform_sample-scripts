"""Lab 2 SSH Connecton with Multiple Devices"""


from netmiko import ConnectHandler

##Inventory
r1 = {'device_type': 'cisco_ios',
      'host': '192.168.235.128' ,
      'username': 'admin',
      'password': 'admin',
      'secret': 'admin' }

r2 = {'device_type': 'cisco_ios',
      'host': '192.168.235.129' ,
      'username': 'admin',
      'password': 'admin',
      'secret': 'admin' }

r3 = {'device_type': 'cisco_ios',
      'host': '192.168.235.130' ,
      'username': 'admin',
      'password': 'admin',
      'secret': 'admin' }

r4 = {'device_type': 'cisco_ios',
      'host': '192.168.235.131' ,
      'username': 'admin',
      'password': 'admin',
      'secret': 'admin' }

devices = [r1,r2,r3,r4]

##Connecting with all devices

for device in devices:

    node = ConnectHandler(**device)
    print(node.is_alive())
    output = node.send_command('show ip int brief')
    print(output)
