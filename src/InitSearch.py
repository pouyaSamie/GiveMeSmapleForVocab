from src.scraping.ReadFromCsv import ReadFromCsv
from src.scraping.SearchForWord import SearchForWord
import asyncio


def Search(maxParagNumber):
    word = input("Enter your word: ")
    loop = asyncio.get_event_loop()
    task = SearchForWord().Search(word, maxParagraph=maxParagNumber).paragraphs

    result = loop.run_until_complete(asyncio.gather(*task))
    for item in result:
        print(item)

    return result


def SearchFormFile(maxParagNumber, filePath):
    wordList = ReadFromCsv(filePath).readCsv()
    tasks = []

    for word in wordList:
        tasks.append(SearchForWord().Search(
            word, maxParagraph=maxParagNumber))

    loop = asyncio.get_event_loop()
    paragraphs = loop.run_until_complete(asyncio.gather(*tasks))

    return paragraphs[0]
