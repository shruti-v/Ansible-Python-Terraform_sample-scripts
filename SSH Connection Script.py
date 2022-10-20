"""Lab for SSH Connection"""

from netmiko import ConnectHandler

##Inventory
r1 = {'device_type': 'cisco_ios',
      'host': '192.168.235.128' ,
      'username': 'admin',
      'password': 'admin',
      'secret': 'admin' }


##Connecting with the device:
node = ConnectHandler(**r1)
print(node.is_alive())

output = node.send_command('show ip int brief')
print(f'Below are the interface details \n\n{output}')
