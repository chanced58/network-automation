class Device:
    def __init__(self, ip, username, password, connection=None):
        self.ip = ip
        self.username = username
        self.password = password
        self.connection = connection

    def connect(self):
        import telnetlib
        self.connection = telnetlib.Telnet(self.ip)


    def authenticate(self):
        self.connection.read_until(b'Username: ')
        self.connection.write(self.username.encode()+ b'\n')
        self.connection.read_until(b'Password: ')
        self.connection.write(self.password.encode() +b'\n')


    def execute(self):
        self.connection.write(command.encode() + b'\n')


    def show(self):
        output = self.connection.read_all().decode('utf-8')
        return output

with open('devices.txt', 'r') as f:
    device = f.read().splitlines()

ip = list()
for item in device:
    tmp = item.split(':')
    ip.append(tuple(tmp))

for element in ip:
    router1 = Device(element[0], 'andrei', 'cisco')
    router1.connect()
    router1.authenticate()
    router1.execute('enable')
    router1.execute('cisco')  #this is the enable password#
    router1.execute('configure terminal')
    router1.execute('interface loopback 0')
    router1.execute('ip address ' + str(element[1]) + ' 255.255.255.255')
    router1.execute('exit')
    router1.execute('router ospf 1')
    router1.execute('network 0.0.0.0 0.0.0.0 area 0')
    router1.execute('end')
    router1.execute('show ip protocol')
    router1.execute('exit')
    output = router1.show()
    print(output)

