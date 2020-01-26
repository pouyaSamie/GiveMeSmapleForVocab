import requests
import re


class GoogleSearch:
    source = ""
    maxSample = 10
    links = []

    def __init__(self, source, maxSample=10):
        self.source = source
        self.maxSample = maxSample

    def SearchOnGoogle(self, word):
        header = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'}
        googleResult = requests.get(
            f'https://www.google.com/search?q=site%3A{self.source}+%22{word}%22', headers=header)

        nyregex = rf"<a\s+(?:[^>]*?\s+)?href=([\"'])(https://{self.source}.*?)\1"
        match = re.findall(nyregex, googleResult.text)
        return [i[1] for i in match][:self.maxSample]
