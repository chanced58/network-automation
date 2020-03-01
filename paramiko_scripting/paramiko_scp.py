import paramiko
from scp import SCPClient

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='10.0.2.15', port=22, username='chance', password='Baseba!!358cd', look_for_keys=False, allow_agent=False)

scp =SCPClient(ssh_client.get_transport())

#copy a single file
scp.put('devices.txt', '/tmp/aa.txt')

#copy a directory
scp.put('directory1', recursive=True, remote_path=/tmp)

scp.get('/etc/passwd', 'passwd')
scp.get('/etc/passwd', 'C:\\Users\\ad\\password-from-scp.txt')


scp.close()

