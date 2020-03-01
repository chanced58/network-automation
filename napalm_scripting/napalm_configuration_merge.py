from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'} #cisco is the enable passowrd
ios = driver('10.1.1.10', 'admin', 'cisco', optional_args=optional_args)
ios.open()
#start code

ios.load_merge_candidate('acl.txt')

diff = ios.compare_config()

#print(diff)
#if len(diff) > 0:
 #   print(diff)
  #  answer = input('Commit Changes?<yes|no>')
   # if answer == 'yes':
    #    print('Commit Changes')
     #   ios.commit_config()
      #  print('Done')
 #   else:
  #      print('No changes required')
   #     ios.discard_config()

answer = input('Rollback?<yes|no>')
if answer == 'yes':
    print('Rolling back. . .')
    ios.rollback()
    print('Done')

#end code
ios.close()