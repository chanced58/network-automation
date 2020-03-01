from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.10',
    'username': 'chance',
    'password': 'baseball',
    'port': 22,
    'secret': 'cisco',
    'verbose':True
    }

connection = ConnectHandler(**cisco_device)

print('Entering enable mode...')
connection.enable()

connection.send_config_from_file('ospf.txt')

connection.disconnect()