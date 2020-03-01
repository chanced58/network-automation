from netmiko import Netmiko
from netmiko import ConnectHandler

#connection = Netmiko(host='10.1.1.10', username='chance', password='baseball', device_type='cisco_ios')

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

prompt = connection.find_prompt()
if '>' in prompt:
    connection.enable()

prompt = connection.find_prompt()
print(prompt)

mode = connection.check_config_mode()
if not mode:
    connection.config_mode()

mode = connection.check_config_mode()

output = connection.send_command('username user2 secret cisco\n')

connection.disconnect()

