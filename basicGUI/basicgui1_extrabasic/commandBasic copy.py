#commanderBasic.py calls upon a data.py function/data via redis

# GETS A MESSAGE

#calling upon keyvalue and setting it as the variable msg
import redis

r = redis.Redis(host = 'localhost') #set to desired ip adress
msg = r.get("message")              #gets value from data file

# print(msg)                        #use print statement to test
                                    # if msg is properly set

# subsribe to channel here
# have it set up so it subsrcibes to the same channel as data.py
