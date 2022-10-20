import schedule
import time
from netmiko import ConnectHandler

def Backup():
    
    file = open("device.txt")


    for ip in file.readlines():


        Router = {'device_type': 'cisco_ios',
                  'host': ip,
                  'username': 'admin',
                  'password': 'admin',
                  'secret': 'admin' }

        node = ConnectHandler(**Router)
        node.enable()
        print(f'Connecting to {node.host}' )

        Backup = node.send_command('show run')
        file = open(f"{node.host}.txt" , "a")
        file.writelines(Backup)
        file.close()

schedule.every(5).seconds.do(Backup)

while True:
    schedule.run_pending()
    time.sleep(1)
