#this code simply prints a greeting via redis

import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""


def howdy():
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        #print("howdy!")
        r.set("msg:howdy", "Howdy!!!")
        msg = r.get("msg:howdy")
        print(msg)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    howdy()
