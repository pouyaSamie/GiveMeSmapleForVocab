from bs4 import BeautifulSoup
import re
from .UrlCaller import UrlCaller
import asyncio
from aiohttp import ClientSession


class SourceScraper():
    link = ""
    paragraph = ""
    word = ""
    loop = None

    def __init__(self, link, word):
        self.link = link
        self.word = word

    async def Scrape(self):

        newsReg = await UrlCaller().GetRequestAsync(self.link)
        return self.text_from_html(newsReg, self.word)

    def text_from_html(self, body, q):
        soup = BeautifulSoup(body, 'html.parser')

        texts = soup.find_all(text=re.compile(q),)
        result = ""
        for paragraph in texts:
            if paragraph.find_parent('p'):
                result = paragraph.find_parent('p').get_text()
                if result != "":
                    return result
        return ""
