from .SearchEnginSpider import SearchEnginSpider
from .NewsSource import sourceList
from .SourceScraper import SourceScraper


class SearchForWord():
    paragraphs = []

    def __init__(self, word, maxParagraph=10):
        # this should be for multiple sources
        spider = SearchEnginSpider(
            source=sourceList[0], maxSample=maxParagraph)
        searchResult = spider.SearchOnBing(word)
        if len(searchResult) > 0:
            for item in searchResult:
                result = SourceScraper(item, word).Scrape()
                print(result)
                print("\r\n")
                if result != '':
                    self.paragraphs.append(result)
