import telnetlib
import getpass

host = '10.1.1.1'
user = 'andrei'
password = getpass.getpass()


tn = telnetlib.Telnet(host)
tn.read_until(b'Username: ')
tn.write(user.encode() + b'\n')

tn.read_until(b'Password: ')
tn.write(password.encode() + b'\n')

tn.write(b'enable\n')
tn.write(b'cisco\n')
tn.write(b'terminal length 0\n')
tn.write(b'show running-config\n')
tn.write(b'exit\n')

result = tn.read_all().decode()
print(result)

