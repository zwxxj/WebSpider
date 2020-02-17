from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs = BeautifulSoup(html, 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle('http://10jqka.com.cn')
if title == None:
    print('title is none')
else:
    print(title)
