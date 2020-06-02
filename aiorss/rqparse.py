from redis import Redis
import rq
import aiorss.rssparser

class RedisParse:

    def __init__(self, content_string):
        self.content_string = content_string
        
