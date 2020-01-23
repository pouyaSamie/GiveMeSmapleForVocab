from .SearchEngine import GoogleSearch
from .NewsSource import sourceList
from .SourceScraper import SourceScraper


class SearchForWord():
    paragraphs = []

    def __init__(self, word):
        # this should be for multiple sources
        googleSearch = GoogleSearch(source=sourceList[0])
        googleResult = googleSearch.SearchOnGoogle(word)
        if len(googleResult) > 0:
            for item in googleResult:
                result = SourceScraper(item, word).Scrape()
                print(result)
                print("\r\n")
                self.paragraphs.append(result)
