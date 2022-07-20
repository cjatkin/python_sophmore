#publishes and reads a list from a redis server

import redis

#connect with redis server as r
r = redis.Redis(host = 'localhost', port = 6379, db = 0)
p = r.pubsub()

chnl = 'test-channel'
p.subscribe(chnl)	#subscribes r to specific channel

##########################################################################

#list = [1,2,3,4,5]
#list = 3
#connect with redis server as r2
r2 = redis.Redis(host = 'localhost', port = 6379, db = 0)
r2.publish(chnl, 4)	#publishes the list to the server

##########################################################################

r.get_message()
#list2 = r.get_message()['data']	#????? idk if this will work
#print(list2)

#x = list2[2]
#print(x)
