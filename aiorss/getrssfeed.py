import httpx
import asyncio
from aiorss.rssparser import RSSParser
from aiorss.constructrssheader import ConstructRSSHeader
from aiorss.rqparse import RedisParse

# TODO: Think of different ways of structuring or aproaching the loop to fetch the rss feed.


class GetRSSFeed:

    def __init__(self, feed_url:str, source_name:str, clean_url:str, categories:list):
        self.feed_url = feed_url
        self.source_name = source_name
        self.clean_url = clean_url
        self.categories = categories

    async def start_loop(self):
        headers = {}
        max_age = 10
        while True:
            async with httpx.AsyncClient() as client:
                try:
                    r = await client.get(url=self.feed_url, headers=headers)
                except httpx.ConnectTimeout as e:
                    print(e) # TODO add webhook for error
            if r.status_code == 200:
                try:
                    await self._parse(r.content)
                except Exception as e:
                    print(e, self.feed_url) # TODO add webhook for error
                header_obj = ConstructRSSHeader(r.headers)
                headers = await header_obj.headers()
            elif r.status_code != 304:
                print(f'error in loop {self.feed_url}') # TODO add webhook for error
                break

            await asyncio.sleep(await header_obj.get_max_age())

    async def _parse(self, feed_str):
        parse = RSSParser(feed_str.decode('utf-8'))
        parse.url = self.clean_url
        parse.feed = self.feed_url
        parse.name = self.source_name
        parse.categories = self.categories
        print(parse.feed)
        return parse

        # parse = RedisParse(feed_str.decode('utf-8'))
        # print(type(parse.entries))
        # return parse.send_worker()

