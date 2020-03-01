import paramiko

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('10.58.85.18', port=22, username='chance', password='Baseba!!358cd', look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('sudo apt update && apt install nmap', get_pty=True)
stdin.write('Baseba!!358cd\n')

#print(stderr.read().decode())

output = stdout.read().decode()
print(output)

ssh_client.close()