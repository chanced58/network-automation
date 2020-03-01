from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'} #cisco is the enable passowrd
ios = driver('10.1.1.10', 'chance', 'baseball', optional_args=optional_args)
ios.open()
#start code

#output0 = ios.get_facts()
#dump0 = json.dumps(output0, sort_keys=True, indent=4)
#print(dump0)

#output1 = ios.get_arp_table()
#dump1 = json.dumps(output1, sort_keys=True, indent=4)
#print(dump1)

#output2 = ios.get_interfaces()
#dump2 = json.dumps(output2, sort_keys=True, indent=4)
#print(dump2)

#output3 = ios.get_interfaces_counters()
#dump3 = json.dumps(output3, sort_keys=True, indent=4)
#print(dump3)

output4 = ios.get_interfaces_ip()
dump4 = json.dumps(output4, sort_keys=True, indent=4)
print(dump4)



#end code
ios.close()