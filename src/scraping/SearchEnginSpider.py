import requests
import re
from bs4 import BeautifulSoup


class SearchEnginSpider:
    source = ""
    links = []

    def __init__(self, source):
        self.source = source

    # We Searching on bing because google changing the way
    # it response to results and can not parsing them easily
    # but bing is so much stable about it

    def SearchOnBing(self, word):
        header = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'}

        bingResult = requests.get(
            f'https://www.bing.com/search?q=site%3A{self.source}+%22{word}%22', headers=header)

        soup = BeautifulSoup(bingResult.content, 'html.parser')
        olResult = soup.find("ol", {"id": "b_results"}).contents

        foundParagraph = 0
        for li in olResult:
            childElemnts = li.findChildren("a", recursive=True)
            for link in childElemnts:
                if 'href' in link.attrs:
                    if link.attrs['href'].startswith(f'https://{self.source}'):
                        self.links.append(link.attrs['href'])
        return self.links
