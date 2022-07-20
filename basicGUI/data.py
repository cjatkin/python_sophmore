# data.py is called upon bu the commander via redis and returns data
# HAS A MESSAGE
# creating a key value pair... when message is called, Hello GUI will be returned

import redis
import matplotlib.pyplot as plt

r = redis.Redis(host = 'localhost')     #set to desired ip adress
r.set("message", "Hello GUI!")          #sets up key value pair to be retrieved

# have it set up so it subsrcibes to the same channel as commandbasic.py

###########################################################################################

# next, have it so the gui displays data from a plot
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
plt.savefig('saved_data.jpeg')

'''
//drone builds the graph, saves it as a file
//commander accesses that file and sends it to the gui file
//gui file displays the image
'''
###########################################################################################

# finally, have the gui display live data from a plot...
# this means it either (1) refreshes the graph when prompted or
# (2) constantly live-updates independently


