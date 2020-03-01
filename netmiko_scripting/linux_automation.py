from netmiko import ConnectHandler

linux = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'chance',
        'password': 'baseball',
        'port': 22,
        'secret': 'baseba11',
        'verbose': True
    }

connection = ConnectHandler(**linux)

connection.enable()
ouptut = connection.send_command('apt-get update && apt-get -y install apache2')
print(output)

connection.disconnect()


