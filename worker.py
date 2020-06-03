import os
import redis
from secret import redis_pass, redis_host
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']
password = config(redis_pass)
conn = redis.from_url(config(redis_host))

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()