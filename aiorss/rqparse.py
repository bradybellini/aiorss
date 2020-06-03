from redis import Redis
import rq
from aiorss.rssparser import RSSParser
from secret import redis_host, redis_pass, redis_port

class RedisParse:

    def __init__(self, content_string):
        self.content_string = content_string
        
    def _parse(self, feed_string):
        f = RSSParser(feed_string)
        

    def send_worker(self):
        redis_connection = Redis(host=redis_host, port=redis_port, password=redis_pass)
        q = rq.Queue('default', connection=redis_connection)
        job = q.enqueue(self._parse, self.content_string)
        # return job.result