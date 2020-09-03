from aiorss._hook import Hook
import asyncio

async def send():
    newhook = Hook('https://discordapp.com/api/webhooks/750917265624399892/3SLmaVtWyloXerm9QqMucFnT6GaOrbq00aOjR6mttLookZfRByh_r-EgR2uWgMSzN5Wg')
    await newhook.warning('A loop has failed or something')
    await newhook.emergency('some shit has gone down')

    
    
    
if __name__ == '__main__':
    current_loops = asyncio.gather(send())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(current_loops)