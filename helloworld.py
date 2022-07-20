
import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""

def hello_redis():

    try:

        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        r.set("msg:hello", "Hello Redis!")

        msg = r.get("msg:hello")

        print(msg)


    except Exception as e:

        print(e)

if _name_ == '_main_':

    hello_redis()
                    
