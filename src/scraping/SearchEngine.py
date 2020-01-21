import sys
import getopt
from lxml import html
import requests
import re
from bs4 import BeautifulSoup


class GoogleSearch:
    source = ""
    maxSample = 1
    links = []

    def __init__(self, word, source, maxSampe=1):
        print("Search Engine")
        self.source = source
        self.maxSample = maxSampe
        # SearchOnGoogle(word)

    def SearchOnGoogle(word):
        header = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'}
        word = input("Enter a word : ")
        googleResult = requests.get(
            f'https://www.google.com/search?q=site%3Awww.nytimes.com+%22{word}%22', headers=header)

        nyregex = r"<a\s+(?:[^>]*?\s+)?href=([\"'])(https://www\.nytimes\.com.*?)\1"
        match = re.findall(nyregex, googleResult.text)

        if len(match) > 0:
            # for item in match:
            item = match[0]
            print(item[1])
            newsReg = requests.get(
                item[1], headers=header)

            print(text_from_html(newsReg.content, word))

    def text_from_html(body, q):
        soup = BeautifulSoup(body, 'html.parser')

        texts = soup.find_all(text=re.compile(q),)
        for paragraph in texts:
            if paragraph.find_parent('p'):
                print(paragraph.find_parent('p').get_text())
        return ""


# if __name__ == "__main__":
#     main()
