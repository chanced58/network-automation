from netmiko import ConnectHandler

with open('devices.txt') as f:
    devices = f.read().splitlines()

device_list = list()
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
    device_list.append(cisco_device)

device_count = 0
for device in device_list:
    device_count += 1
    print('Connecting to ' + device['ip'])
    connection = ConnectHandler(**device)

    print('Entering enable mode . . . ')
    connection.enable()

    loopback_command = 'network ' + str(device_count) + '.' + str(device_count) + '.' + str(device_count) + '.' + str(device_count) + ' 0.0.0.0 area 0'
    commands = ['exit', 'wr']
    output = connection.send_config_set(commands)
    print(output)



    connection.disconnect()

    