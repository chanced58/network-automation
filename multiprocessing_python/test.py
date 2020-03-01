from netmiko import ConnectHandler

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

    output = connection.send_command('show ip int br')
    print(output)