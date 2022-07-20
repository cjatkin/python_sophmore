# data.py is called upon bu the commander via redis and returns data
# HAS A MESSAGE
# creating a key value pair... when message is called, Hello GUI will be returned

import redis

r = redis.Redis(host = 'localhost')     #set to desired ip adress
r.set("message", "Hello GUI!")          #sets up key value pair to be retrieved

# have it set up so it subsrcibes to the same channel as commandbasic.py
