from netmiko import ConnectHandler
import time
from queue import Queue
import threading

def connect_and_run(device, output_q, cmd='show run'):
    print('Connecting to device: ', device['ip'])
    connection = ConnectHandler(**device)

    print('Entering enable mode . . .')
    connection.enable()

    print('Executing command: ', cmd)
    output = connection.send_command(cmd)
    output_q.put(output)



if __name__ == '__main__':
    with open('devices.txt', 'r') as f:
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

    #print(device_list)

    #script starting time
    start = time.time()

    output_q = Queue()

    for device in device_list:
        my_thread = threading.Thread(target=connect_and_run, args=(device, output_q, 'show ip int br'))



    main_thread = threading.current_thread()
    for my_thread in threading.enumerate():
        if my_thread != main_thread:
            my_thread.join()


    while not output_q.empty():
        output = output_q.get()
        print(output)
        print('#' * 40)

    #script ending time
    end = time.time()

    print('Script execution time: ', end-start)