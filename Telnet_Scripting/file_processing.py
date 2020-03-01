with open('devices.txt', 'r') as f:
    device = f.read().splitlines()

ip = list()
for item in device:
    tmp = item.split(':')
    ip.append(tuple(tmp))

print(ip)
