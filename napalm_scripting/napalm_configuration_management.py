from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'} #cisco is the enable passowrd
ios = driver('10.1.1.10', 'admin', 'cisco', optional_args=optional_args)
ios.open()
#start code

ios.load_replace_candidate(filename='config.txt')

diff = ios.compare_config()
if len(diff):
    print(diff)
    print('Commit changes. . . ')
    ios.commit_config()
    print('Done')
else:
    print('No Change Required')


#end code
ios.close()