#commanderBasic.py calls upon a data.py function/data via redis

# GETS A MESSAGE

#calling upon keyvalue and setting it as the variable msg
import redis

r = redis.Redis(host = 'localhost') #set to desired ip adress
msg = r.get("message")              #gets value from data file

# print(msg)                        #use print statement to test
                                    # if msg is properly set

'''
data.py creates the graph
commandBasic.py acesses the graph that data.py creates (over redis?? how will that work...hmmm
	- gui just imports the jpeg to redis...?
	- data -> publish image to channel
	- commander -> saves the image
	- guibasic -> acesses the image via the commander

guibasic.py will display the graph 
'''

# subsribe to channel here
# have it set up so it subsrcibes to the same channel as data.py
