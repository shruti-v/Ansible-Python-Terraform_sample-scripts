from napalm import get_network_driver

driver = get_network_driver('ios')

r1 = {
    "hostname": '192.168.235.128',
    "username": 'admin',
    "password": 'admin',
    "optional_args": {
        "secret": 'admin'
        }
    }

r2 = {
    "hostname": '192.168.235.129',
    "username": 'admin',
    "password": 'admin',
    "optional_args": {
        "secret": 'admin'
        }
    }

r3 = {
    "hostname": '192.168.235.130',
    "username": 'admin',
    "password": 'admin',
    "optional_args": {
        "secret": 'admin'
        }
    }

r4 = {
    "hostname": '192.168.235.131',
    "username": 'admin',
    "password": 'admin',
    "optional_args": {
        "secret": 'admin'
        }
    }

devices = [r1, r2, r3, r4]

for device in devices:
    node =  driver(**device)
    node.open()

    facts = node.get_facts()
    print(facts)

    arp = node.get_arp_table()
    print(arp)

    environment = node.get_environment()
    print(environment)

    interfaces = node.get_interfaces()
    print(interfaces)

    int_counters = node.get_interfaces_counters()
    print(int_counters)

    int_ip = node.get_interfaces_ip()
    print(int_ip)

    lldp = node.get_lldp_neighbors()
    print(lldp)

    mac = node.get_mac_address_table()
    print(mac)

    user = node.get_users()
    print(user)


    ping = node.ping(node.hostname)
    print(ping)

      
          
