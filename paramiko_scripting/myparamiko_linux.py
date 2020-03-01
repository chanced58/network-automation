import myparamiko


ssh_client = myparamiko.connect('10.58.85.18', 22, 'chance', 'Baseba!!358cd')
remote_connection = myparamiko.get_shell(ssh_client)
output1 = myparamiko.send_command(remote_connection, 'ifconfig')
print(output1.decode())