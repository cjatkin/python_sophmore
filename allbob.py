# Sample code for creating a channel/subscribing to the channel/accessing the channel in redis
# https://kb.objectrocket.com/redis/basic-redis-usage-example-part-2-pub-sub-in-depth-using-redis-python-719
import redis

###################################################################################

bob_r = redis.Redis(host = 'localhost', port = 6379, db = 0) #connect w/ redis server as Bob
bob_p = bob_r.pubsub()

bob_p.subscribe('classical_music')  #subscribe the the channel "classical music"
'''
So I think that when something is subsrcibed to the channel, the channel is created?
'''

###################################################################################

alice_r = redis.Redis(host = 'localhost', port = 6379, db = 0)  #connect with redis server as Alice
alice_r.publish('classical_music', 'Alice Music')   #publish new music in the channel classical_music

###################################################################################

bob_p.get_message()   #fetch music from channel... Bob can get Alice's music with get_message method
new_music = bob_p.get_message()['data'] #this saves the music in the channel as new music
print(new_music)

###################################################################################

alice_r.publish('classical_music', 'Alice 2nd Music')   #Alice published more music to the channel
another_music = bob_p.get_message()['data']  #bob saves the music from channel and saves it in variable
print(another_music)

###################################################################################
