import myparamiko

router_list = ['10.1.1.10']
userName = 'chance'
password = 'baseball'
enable = 'cisco'

def create_loopback(list, user, passwrd, ensecret):
    loop_count = 0
    for x in list:
        loop_count += 1
        ssh_client = myparamiko.connect(x, 22,user, passwrd)
        remote_connection = myparamiko.get_shell(ssh_client)
        command0 = 'configure terminal'
        command1 = 'int loopback' + str(loop_count)
        command2 = 'ip address ' + str(loop_count) + '.' + str(loop_count) + '.' + str(loop_count) + '.' + str(loop_count) + ' 255.255.255.0'
        command3 = 'no shut'
        command4 = 'end'
        command5 = 'show ip int br'
        myparamiko.send_command(remote_connection, 'enable')
        myparamiko.send_command(remote_connection, ensecret)
        myparamiko.send_command(remote_connection, command0)
        myparamiko.send_command(remote_connection, command1)
        myparamiko.send_command(remote_connection, command2)
        myparamiko.send_command(remote_connection, command3)
        myparamiko.send_command(remote_connection, command4)
        output1 = myparamiko.send_command(remote_connection, command5)
        with open('Output.txt', 'a', newline='') as file:
            file.writelines('CiscoRouter' + str(loop_count) + ' Interface Report \n')
            file.writelines('----------------------------- \n')
            file.writelines(output1.decode())
            file.close()

create_loopback(router_list, userName, password, enable)


