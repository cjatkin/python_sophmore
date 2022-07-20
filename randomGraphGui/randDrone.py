##################################################################################
# droneFun.py
# Sends command to DroneFun.py using fun.json file value keys
##################################################################################

import sys
import subprocess
import redis
import csv
import rand as foo       #marries fun.py and fun.json
from time import sleep

# PART 1 ##################################################
# Ensures that the correct veresion of python is present
if sys.version_info < (3,7): #checking for python version...
        sys.exit("Please use Python >=3.7")
subprocess.run("clear")
print(50*"=",end="\n")
print("Starting Programme...")
print(50*"=",end="\n\n")

# PART 2 ##################################################
# load firmware config
# lambda method use for general purpose firmware loading
f = "rand" # can be a user input
cmdpath = lambda name : "./" + name + "/" + name + ".py"

# Reading CSV File
with open('rand.csv', newline = '') as csvfile:
        file_reader = csv.reader(csvfile, delimiter = ',')
        #goes through csv file and creates a dictionary
        command_dict = {rows[0]:rows[1] for rows in file_reader}


#connects variable command_dict to fun.py/.json and can be used to reference
#   either file

# PART 3 ##################################################
print("Command List:")
print(35*"-")
for c in command_dict:
    print(f"{c} | cmd: {command_dict[c]} ") #will only have one command (00: funHello)
print("\n")

# PART 4 ##################################################
# Starting Redis client
chnl ="python-channel"
chnl2 = "borg"
print(f"Subscribing to \'{chnl}\'...")
r = redis.Redis(host = '10.153.40.1')
p = r.pubsub(ignore_subscribe_messages=True)    #the messages for sub/unsub are read but won't send confirmation messages
p.subscribe(chnl)                       #drone subscribes to channel here
print(f"Subscribed to \'{chnl}\'.\n")

# PART 5 ##################################################
animation = "|/-\\"
i=0
while True:
    msg = p.get_message()
    if msg:
        cmd=msg['data'].decode()
        print(f"Message Recieved: \"{cmd}\"")
        if cmd == 'stop':
            break
        elif hasattr(foo,command_dict[cmd]):
            print(f"Running \'{command_dict[cmd]}\' Command.\n")
            words = getattr(foo,command_dict[cmd])()	#changed... saves retur
            r.publish(chnl, words)
        else:
            print("Invalid Command Entered")
    sleep(0.1)
    sys.stdout.write("\rReady to Recieve Messages. " + animation[i%4])
    sys.stdout.flush()
    i+=1
p.close()
print("Exiting")

