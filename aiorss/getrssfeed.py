import httpx
import asyncio
from aiorss import newsparser, headerscache

class GetRSSFeed:

    def __init__(self, headers, feed):
        self.headers = headers
        self.feed = feed
