import requests
from bs4 import BeautifulSoup
import re


class SourceScraper():
    link = ""
    paragraph = ""
    word = ""

    def __init__(self, link, word):
        self.link = link
        self.word = word

    def Scrape(self):
        header = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'}
        newsReg = requests.get(
            self.link, headers=header)
        return self.text_from_html(newsReg.content, self.word)

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
