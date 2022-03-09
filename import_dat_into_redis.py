import redis
import time
from datetime import datetime

# docker redis cpu 4 memory 8G 에 100 만건 입력시 
# 2022-03-09 11:16:39.233451
# 2022-03-09 11:30:51.160277
# 14:11 min

# rump 로 data 를 redis1 에서 redis2 로 옮기는 중에 redis 1에 다시 import
# 2022-03-09 12:06:12.719894
# 2022-03-09 12:07:56.624879
# 1/10 만 넣어봤다. 1:44. 적당한 속도

# rump mig 는 매우 느리다. 그리고 key id 순차도 아니다. redis 가 원래 그렇다.

redis_host = 'localhost'
redis_port = 6379
redis_password = ''

r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

def insert_into_redis(id):
    try:
        r.set("key" + id, "hello redis from python this data is not so small but I have to test this further " + id)
        # msg = r.get("key1")
        # print(msg)
    except Exception as e:
        print(e)

def insert_many():
    for i in range(1000000):
        if i % 10000 == 0:
            print(i / 10000)
             
        insert_into_redis(str(i))

def insert_many_again():
    for i in range(1000000,1100000):
        if i % 10000 == 0:
            print(i / 10000)
             
        insert_into_redis(str(i))

def print_date():
    start = datetime.now()
    end = datetime.now()

    print(end - start)

if __name__ == '__main__':
    # insert_into_redis()
    print(datetime.now())
    insert_many()
    print(datetime.now())
    # print_date()


