# import xml.etree.ElementTree as ET

# # root = ET.parse('testing/rss.xml').getroot()

# # print(root.tag)

# parser = ET.XMLPullParser(['start', 'end'])
# feed = parser.feed('/testing/rss.xml')
# print(parser.feed('/testing/rss.xml'))
# # for event, elem in feed.read_events():
# #     print(event)

	
from aiorss import GetRSSFeed
import asyncio
import inspect


async def loop_1():
    newfeed1 = GetRSSFeed('https://www.cryptopolitan.com/rss', 'test', 'test')
    await newfeed1.start_loop()
    # print(await newfeed1._parse())

# async def loop_2():
#     newfeed2 = GetRSSFeed('https://cointelegraph.com/rss', 'test', 'test')
#     await newfeed2.start_loop()
#     await feed.run()

# async def loop_3():
#     newfeed3 = GetRSSFeed('https://beincrypto.com/feed', 'test', 'test')
#     await newfeed3.start_loop()

# async def loop_4():
#     newfeed4 = GetRSSFeed('https://feeds.feedburner.com/bitcoinnews/MyiC', 'test', 'test')
#     await newfeed4.start_loop()

# async def loop_5():
#     newfeed5 = GetRSSFeed('http://bitcoinist.net/feed', 'test', 'test')
#     await newfeed5.start_loop()


# , loop_2(), loop_3(), loop_4(), loop_5()



if __name__ == '__main__':
    current_loops = asyncio.gather(loop_1())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(current_loops)