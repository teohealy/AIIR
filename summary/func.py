import requests
from bs4 import BeautifulSoup


def summary(path):
    with open(path, 'r', encoding = 'utf-8') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'lxml')
        b = []
        for i in soup.find_all("span", attrs= {'data-tid':'4502216a'}):
            b.append(i.text)
    return b







