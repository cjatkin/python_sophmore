import sys
import subprocess
import redis
import json
import csv
#import somefirmware.somefirmware as foo
import somefirmware as foo
from time import sleep
import pandas as pd

# PART 2 ##################################################
# load firmware config
# lambda method use for general purpose firmware loading
f="somefirmware" # can be a user input
#jsonpath= lambda name : "./" + name + "/" + name + ".json"
cmdpath = lambda name : "./" + name + "/" + name + ".py"

#opening csv File

with open('somefirmware.csv', newline = '') as csvfile:
	file_reader = csv.reader(csvfile, delimiter = ',')
		#going through csv and creating a dictionary
	command_dict = {rows[0]:rows[1] for rows in file_reader}	#assigns each value/key command/function pair in dictionary

#pandas
#command_dict = pd.read_csv('somefirmware.csv', header = None, index_col = 0, squeeze = True).to_dict()



# PART 3 ##################################################
print("Command List:")
print(35*"-")
for c in command_dict:
    print(f"{c} | cmd: {command_dict[c]} ")
print("\n")

