from .SearchEnginSpider import SearchEnginSpider
from .NewsSource import sourceList
from .SourceScraper import SourceScraper


class SearchForWord():
    paragraphs = []

    def __init__(self, word, maxParagraph=10):
        # this should be for multiple sources
        spider = SearchEnginSpider(
            source=sourceList[0])
        searchResult = spider.SearchOnBing(word)
        foundCount = 0
        if len(searchResult) > 0:
            for item in searchResult:
                result = SourceScraper(item, word).Scrape()
                print(result)
                if result != '':
                    foundCount += 1
                    self.paragraphs.append(result)
                    if foundCount == maxParagraph:
                        return
