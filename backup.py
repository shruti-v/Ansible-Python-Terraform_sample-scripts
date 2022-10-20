from netmiko import ConnectHandler

file = open("device.txt")

for ip in file.readlines():
    print(ip)

    Router = {'device_type': 'cisco_ios',
      'host': ip,
      'username': 'admin',
      'password': 'admin',
      'secret': 'admin' }

    node = ConnectHandler(**Router)
    node.enable()
    print(f'Connecting to {node.host}' )

    Backup = node.send_command('show run')
    file = open(f"{node.host}.txt" , "w")
    file.writelines(Backup)
    file.close()
