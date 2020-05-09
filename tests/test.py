# import xml.etree.ElementTree as ET

# # root = ET.parse('testing/rss.xml').getroot()

# # print(root.tag)

# parser = ET.XMLPullParser(['start', 'end'])
# feed = parser.feed('/testing/rss.xml')
# print(parser.feed('/testing/rss.xml'))
# # for event, elem in feed.read_events():
# #     print(event)

	
from concurrent.futures import ThreadPoolExecutor
from time import sleep
 
def return_after_5_secs(message):
    sleep(5) 
    return message
 
pool = ThreadPoolExecutor(20)
 
future = pool.submit(return_after_5_secs, ("hello"))
print(future.done())
sleep(5)
print(future.done())
print(future.result())