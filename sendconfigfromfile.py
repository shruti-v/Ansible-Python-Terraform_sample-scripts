from netmiko import ConnectHandler


R1 = {'device_type': 'cisco_ios',
      'host': '192.168.235.128',
      'username': 'admin',
      'password': 'admin',
      'secret': 'admin' }

R2 = {'device_type': 'cisco_ios',
      'host': '192.168.235.129',
      'username': 'admin',
      'password': 'admin',
      'secret': 'admin' }

R3 = {'device_type': 'cisco_ios',
      'host': '192.168.235.130',
      'username': 'admin',
      'password': 'admin',
      'secret': 'admin' }

R4 = {'device_type': 'cisco_ios',
      'host': '192.168.235.131',
      'username': 'admin',
      'password': 'admin',
      'secret': 'admin' }

devices = [R1, R2, R3, R4]

for device in devices:
    node = ConnectHandler(**device)
    node.enable()
    output = node.send_config_from_file("lines.txt")
    print(output)
    
