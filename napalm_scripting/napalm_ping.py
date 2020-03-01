from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'} #cisco is the enable passowrd
ios = driver('10.1.1.10', 'chance', 'baseball', optional_args=optional_args)
ios.open()
#start code

output = ios.ping(destination='10.1.5.10', count=2, source='1.1.1.1')
ping = json.dumps(output, sort_keys=True, indent=4)
print(ping)







#end code
ios.close()