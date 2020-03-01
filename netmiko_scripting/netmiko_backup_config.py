from netmiko import ConnectHandler
import datetime

with open('devices.txt') as f:
    devices = f.read().splitlines()

print(devices)

for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'chance',
        'password': 'baseball',
        'port': 22,
        'secret': 'cisco',
        'verbose': True
    }
    print('Connecting to ' + ip)
    connection = ConnectHandler(**cisco_device)

    print('Entering enable mode . . .')
    connection.enable()

    output = connection.send_command('show run')
    #print(output)

    prompt = connection.find_prompt()
    hostname = prompt[:-1]

    now = datetime.datetime.now()
    today = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    file = today + '-' + hostname + '.txt'

    with open(file + '.txt', 'w') as backup:
        backup.write(output)
        print('Backup of ' + hostname + ' completed successfully')
        print('#' * 30)

    connection.disconnect()
