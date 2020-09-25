from aiorss import GetRSSFeed
import asyncio
import inspect

async def loop_1():
    newfeed1 = GetRSSFeed('https://www.cryptopolitan.com/rss', 'test', 'test', list('cryptocurrency'))
    await newfeed1.start_loop()

async def loop_2():
    newfeed1 = GetRSSFeed('https://www.gameinformer.com/news.xml', 'test', 'test', list('cryptocurrency'))
    await newfeed1.start_loop()
    
async def loop_3():
    newfeed1 = GetRSSFeed('https://www.pcgamesn.com/rss', 'test', 'test', list('cryptocurrency'))
    await newfeed1.start_loop()
    
async def loop_4():
    newfeed1 = GetRSSFeed('https://kotaku.com/rss', 'test', 'test', list('cryptocurrency'))
    await newfeed1.start_loop()

async def loop_5():
    newfeed1 = GetRSSFeed('https://www.pcgamer.com/rss', 'test', 'test', list('cryptocurrency'))
    await newfeed1.start_loop()
    
async def loop_6():
    newfeed1 = GetRSSFeed('https://www.gamesradar.com/all-platforms/news/rss/', 'test', 'test', list('cryptocurrency'))
    await newfeed1.start_loop()
    
async def loop_7():
    newfeed1 = GetRSSFeed('https://www.usgamer.net/rss', 'test', 'test', list('cryptocurrency'))
    await newfeed1.start_loop()
    
async def loop_8():
    newfeed1 = GetRSSFeed('https://www.nintendolife.com/feeds/latest', 'test', 'test', list('cryptocurrency'))
    await newfeed1.start_loop()
    
async def loop_9():
    newfeed1 = GetRSSFeed('https://twinfinite.net/feed/', 'test', 'test', list('cryptocurrency'))
    await newfeed1.start_loop()

if __name__ == '__main__':
    # current_loops = asyncio.gather(loop_1(), loop_3())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(loop_1(), loop_2(), loop_3(), loop_4(), loop_5(), loop_6(), loop_7(), loop_8(), loop_9()))
