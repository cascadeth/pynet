#!/usr/bin/python3

import system, platform

ping_statement = ""

if platform.system() == 'Windows':
    ping_statement = 'ping -n 2 '
elif: platform.system() == 'Linux':
    ping_statement = 'ping -c 2 '
else:
    print("Unsupported environment detected: {}".format(platform.system()))
    exit()

ip_range = []

# Eventually combine code from week1/exercise2 to accept and validate input
# For now - 

# HARD CODE IT YOU PLEB 

# (all caps provided to provide emphasis on situation (notice-ability and 
# conveying the current feeling of not having the motivation and time to 
# git gud); self insult provided for motivation to produce better, more 
# efficient, more interactive, and more user friendly code ... 
# _for a terminal application that no one will see_ ... :thinking_face: )

subnet_id = '10.0.0.0'

# From 1 to 255 (exclusive of 255; 1 to 254, inclusive of 254)
for i in range(1,255):
    # Append (the join of the items on the char '.' of 
    # (the subnet ID split on the char '.' but only grab the  first 3 fields) 
    # then contatenated with a '.' and i converted from int to str) 
    # to the list
    ip_range.append('.'.join(subnet_id.split('.')[:3]) + '.' + str(i))


