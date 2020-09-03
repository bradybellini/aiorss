import httpx
import asyncio

class Hook:
    
    def __init__(self, url:str):
        self.url = url
        
    async def _send(self, content, name):
        client = httpx.AsyncClient()
        await client.post(str(self.url), data={'content':content, 'username':name})
    
    async def warning(self, content:str):
        payload = f':warning: **WARNING** :warning:\n\n{content}'
        await self._send(payload, 'WARNING')
    
    async def emergency(self, content:str):
        payload = f':name_badge: **EMERGENCY** <@101563945462026240> :name_badge:\n\n{content}'
        await self._send(payload, 'EMERGENCY')