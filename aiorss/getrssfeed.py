import httpx
import asyncio
from aiorss.rssparser import RSSParser
from aiorss.constructrssheader import ConstructRSSHeader
from aiorss.rqparse import RedisParse

# TODO: Think of different ways of structing or aproaching the loop to fetch the rss feed.


class GetRSSFeed:

    def __init__(self, feed_url, source_name, clean_url):
        self.feed_url = feed_url
        self.source_name = source_name
        self.clean_url = clean_url


    async def start_loop(self):
        is_loop = True
        headers = {}
        max_age = 10
        while is_loop:
            async with httpx.AsyncClient() as client:
                try:
                    r = await client.get(url=self.feed_url, headers=headers)
                except httpx.ConnectTimeout as e:
                    print(e)
            if r.status_code == 200:
                try:
                    await self._parse(r.content)
                except Exception as e:
                    print(e, self.feed_url)
                header_obj = ConstructRSSHeader(r.headers)
                headers = await header_obj.headers()
                # print(await header_obj.get_max_age())
            elif r.status_code != 304:
                print(f'error in loop {self.feed_url}')
                break

            await asyncio.sleep(await header_obj.get_max_age())

    async def _parse(self, feed_str):
        parse = RSSParser(feed_str.decode('utf-8'))
        print(parse.entries)
        return parse.entries[0]
        # parse = RedisParse(feed_str.decode('utf-8'))
        # print(type(parse.entries))
        # return parse.send_worker()
