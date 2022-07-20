import sys
import subprocess
import redis
import json
#import somefirmware.somefirmware as foo
import somefirmware as foo
from time import sleep

print(50*"=",end="\n")
print("Starting Programme...")
print(50*"=",end="\n\n")

# load firmware config
# lambda method use for general purpose firmware loading
f="somefirmware" # can be a user input
jsonpath= lambda name : "./" + name + "/" + name + ".json"
cmdpath = lambda name : "./" + name + "/" + name + ".py"

# Reading JSON File
with open(jsonpath(f),'r') as cmdlist:
    command_obj=cmdlist.read()
command_dict=json.loads(command_obj)

print("Command List:")
print(35*"-")
for c in command_dict:
    print(f"{c} | cmd: {command_dict[c]} ")
print("\n")

print("This is howdyDrone.py. Run with howdyCommander.py")
print("Command List:")
print(30*"*")

for c in command_dict:
    print(f"{c} | cmd: {command_dict[c]} ")
    print("\n")

#starting new redis client
chnl = "python-channel"
print(f"Subscribing to \'{chnl}\'...")
r = redis.Redis()
p = r.pubsub(ignore_subscribe_messages=True)
p.subscribe(chnl)
print(f"Subscribed to \'{chnl}\'.\n")

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
            getattr(foo,command_dict[cmd])()
            print("")
        else:
            print("Invalid Command Entered")
    sleep(0.1)
    sys.stdout.write("\rReady to Recieve Messages. " + animation[i%4])
    sys.stdout.flush()
    i+=1
p.close()
print("Exiting.")
