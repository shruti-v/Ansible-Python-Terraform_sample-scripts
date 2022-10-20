from netmiko import ConnectHandler

SW1 = {'host': '192.168.235.128',
      'username': 'admin',
      'password': 'admin',
      'device_type': 'cisco_ios'}

node = ConnectHandler(**SW1)

for vlan in range(2,10):
    print("Creating Vlan" + str(vlan))

    outputs = []
    cmd = ['vlan'+ str(vlan) + " " + 'name_python_'+ str(vlan)]
    print(cmd)
    output = node.send_config_set(cmd)
    outputs.append(output)
    print(output)

vlan_info = []
vlan = node.send_command('show vlan')
vlan_info.append(vlan)
print(vlan)
