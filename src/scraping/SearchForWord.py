from SearchEngine import GoogleSearch
from NewsSource import sourceList


class SearchForWord():
    def __init__(self, word):
        se = GoogleSearch(word, source=sourceList[0])
