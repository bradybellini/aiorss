# from aiorss import GetRSSFeed
# import asyncio
# import inspect

# async def loop_1():
#     newfeed1 = GetRSSFeed('https://www.cryptopolitan.com/rss', 'test', 'test')
#     await newfeed1.start_loop()

# if __name__ == '__main__':
#     current_loops = asyncio.gather(loop_1())
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(current_loops)


from redis import Redis
from rq import Queue
from secret import redis_pass
from test2 import test

# f = rssparser('https://www.cryptopolitan.com/rss')
redis_connection = Redis(host='206.189.218.5', port=6379, password=redis_pass)
q = Queue(connection=redis_connection)

job = q.enqueue(test, 'https://www.cryptopolitan.com/rss')
print(job.result)