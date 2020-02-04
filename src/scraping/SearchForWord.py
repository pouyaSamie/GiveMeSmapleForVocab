from .SearchEnginSpider import SearchEnginSpider
from .NewsSource import sourceList
from .SourceScraper import SourceScraper
import asyncio


class SearchForWord():
    paragraphs = []

    def __init__(self):
        paragraphs = []

    # this should be for multiple sources

    async def Search(self, word, maxParagraph=10):
        spider = SearchEnginSpider(
            source=sourceList[0])

        searchResult = spider.SearchOnBing(word)

        foundCount = 0
        if len(searchResult) > 0:
            for item in searchResult:
                result = await SourceScraper(item, word).Scrape()
                if result != '':
                    print(result)
                    foundCount += 1
                    self.paragraphs.append(result)
                    if foundCount == maxParagraph:
                        return self.paragraphs
