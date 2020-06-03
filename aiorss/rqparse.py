from redis import Redis
import rq
import aiorss.rssparser
from secret import redis_host, redis_pass, redis_port

class RedisParse:

    def __init__(self, content_string):
        self.content_string = content_string
        
    def _parse(self, feed_string):
        f = rssparser(feed_string)
        print(f)

    def send_worker(self):
        redis_connection = Redis(host=redis_host, port=redis_port, password=redis_pass)
        q = rq.Queue(connection=redis_connection)
        job = q.enqueue(self._parse, self.content_string)
        return job.result