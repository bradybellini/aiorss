from redis import Redis
from secret import redis_pass, redis_host, redis_port
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']
redis_connection = Redis(host=redis_host, port=redis_port, password=redis_pass)

import feedparser
import httpx


if __name__ == '__main__':
    with Connection(redis_connection):
        worker = Worker(map(Queue, listen))
        worker.work()