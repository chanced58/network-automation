import myserial

console = myserial.open_console()
myserial.check_initial_configuration_dialog(console)
myserial.run_command(console,'enable')
myserial.run_command(console,'configure terminal')
myserial.run_command(console,'username u1 secret cisco')
myserial.run_command(console,'end')

output = myserial.read_from_console(console)
print(output)

