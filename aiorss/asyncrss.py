from xml.etree import ElementTree
import asyncio

class RSSParser:
    
    async def __init__(self, feed):
        self.feed = feed