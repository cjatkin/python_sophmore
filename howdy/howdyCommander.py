'''
This file is paired with howdyDrone.py
When running, it will ask you to enter the key which is howdy...
Once howdy is entered, drone.py will accept the key and return the value "Howdy partner!"
'''
#redis server must be running

import redis
import sys
import json
from time import sleep
import somefirmware2 as foo

#loading firmwarel
# load firmware config
# lambda method use for general purpose firmware loading
f="somefirmware" # can be a user input
jsonpath= lambda name : "./"  + name + ".json"
cmdpath = lambda name : "./"  + name + ".py"

#read json file
with open(jsonpath(f),'r') as cmdlist:
    command_obj=cmdlist.read()
command_dict=json.loads(command_obj)


#bind host to redis server ip
r = redis.Redis(host = '10.153.62.255') #this keeps changing for some reason but his matches redis.conf
p = r.pubsub(ignore_subscribe_messages = True)

def check_chnls():
    chnls_open = check_chnls()
    print(f"Open channels: \'{chnls_open}..."")

    if len(chnls_open == 0):
        print("Need drone to subscribe to a channel...")
        animation = "|/-\\"

        i = 0
        while len(chnls_open) == 0:
            sleep(0.1)
            sys.stdout.write("\rWaiting for subscription..." + animation[i%4])
            sys.stdout.flush()
            i += 1
            chnls_open = check_chnls()

        while True:
            p.subscribe('borg')     #here is where I was struggling with code last time... wouldnt subsribe to a channel
            chnls_open = check_chnls()

            print("Publishing to " + str(drone))

            while True:

                # also here you would change the banner to "connected?"
                print("Command List:")
                print(35*"-")
                for c in command_dict:
                    print(f"{c} | cmd: {command_dict[c]} ")
                print("\n")
                print("To select a different drone enter 'change'.")
                command = str(input("Enter command from list.   "))
                try:
                    if command == 'stop':
                        r.publish(drone,command)
                        break
                    elif command == 'change':
                        print("Changing drone selection...")
                        break
                    elif hasattr(foo,command_dict[command]):
                        print(f"Sending \'{command_dict[command]}\' Command.\n")
                        r.publish(drone,command)
                        print("Sent")
                        while True:
                            msg = p.get_message()
                            if msg:
                                print(msg['data'].decode())
                                break
                    else:
                        print("Invalid command.")
                    sleep(0.1)
                except KeyError:
                    print("Please enter a valid key.")
            if command == 'stop':
                break # Breaks the outer while loop
            else:
                continue
        elif drone == 'stop':
            break
        else:
            print("Try a different channel.")
    except ValueError:
        print("Invalid input")
print("Exiting Commander")
usrInput()
