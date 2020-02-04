from fake_useragent import UserAgent
import requests
import asyncio
from aiohttp import ClientSession


class UrlCaller():
    user_agent = None

    def __init__(self):
        self.user_agent = UserAgent()

    def GetRequest(self, url):

        return requests.get(
            url, headers={"user-agent": self.user_agent.chrome})

    async def GetRequestAsync(self, url):
        async with ClientSession() as session:
            async with session.get(url) as response:
                response = await response.read()
                return response

    async def fetch(url, session):
        async with session.get(url) as response:
            return await response.read()

    async def GetUrlsAsync(self, urls):
        tasks = []
        async with ClientSession() as session:
            for url in urls:
                task = asyncio.ensure_future(fetch(url, session))
                tasks.append(task)

        responses = asyncio.gather(*tasks)
        return await responses
