import re
from bs4 import BeautifulSoup
from .UrlCaller import UrlCaller


class SearchEnginSpider:
    source = ""
    links = []
    urlTemplate = 'https://www.bing.com/search?q=site%3A{}+%22{}%22'

    def __init__(self, source):
        self.source = source

    # We Searching on bing because google changing the way
    # it response to results and can not parsing them easily
    # but bing is so much stable about it
    def SearchOnBing(self, word):

        bingResult = UrlCaller().GetRequest(
            self.urlTemplate.format(self.source, word))

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
