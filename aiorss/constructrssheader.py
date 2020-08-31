from abc import ABC, abstractmethod

class ConstructRSSHeader:

    # _etag: str = ''
    # _max_age: int = None
    # user_agent: str = 'Change Later'
    # from_header: str = ''
    # header_contruct: dict = {}

    def __init__(self, h):
        self.h = h
        self._etag: str = ''
        self._max_age: int = None
        self.user_agent: str = 'Change Later'
        self.from_header: str = ''
        self.header_construct: dict = {}

    @abstractmethod
    async def _check_etag(self):
        if 'etag' in self.h:
            self._etag = self.h['etag']
            return True
        else:
            self._etag = None
            return False

    @abstractmethod
    async def _check_max_age(self):
        if 'cache-control' in self.h:
            _cache_control = self.h['cache-control']
            if 'max-age=' in _cache_control:
                _cache_control_ints = ''.join(
                    (l if l in '0123456789' else ' ') for l in _cache_control)
                _max_age_lowest = min(int(m)
                                      for m in _cache_control_ints.split())
                if _max_age_lowest > 3600 or _max_age_lowest < 300:
                    self._max_age = 600
                else:
                    self._max_age = _max_age_lowest
            else:
                self._max_age= 30
        else:
            self._max_age = 30

    async def get_etag(self):
        await self._check_etag()
        return self._etag

    async def get_max_age(self):
        await self._check_max_age()
        return self._max_age

    async def headers(self):
        if await self._check_etag():
            self.header_construct = {'If-None-Match': self._etag}
        # add other header when there is no etag detected
        return self.header_construct

