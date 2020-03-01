import telnetlib
import getpass
import time

my_devices = ['10.1.1.10', '10.1.1.20', '10.1.1.30']
for device in my_devices:
    user = 'andrei'
    password = getpass.getpass()

    tn = telnetlib.Telnet(device)
    tn.read_until(b'Username: ')
    tn.write(user.encode() + b'\n')

    tn.read_until(b'Password: ')
    tn.write(password.encode() + b'\n')

    tn.write(b'enable\n')
    tn.write(b'cisco\n')
    tn.write(b'configure terminal\n')
    tn.write(b'ip route 0.0.0.0 0.0.0.0 e0/1 10.1.1.2\n')
    tn.write(b'end\n')
    tn.write(b'show ip route\n')

    result = tn.read_all().decode()
    print(result)
    print('##############')
    time.sleep(1)
