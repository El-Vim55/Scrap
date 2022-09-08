import requests
from bs4 import BeautifulSoup
from re import compile, search
import asyncio
#import aiohttp


headers = (
    {'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/103.0.5060.53 Safari/537.36',
                        'Accept-language': 'en-AU, en;q=0.5'}
                        )

BASE_URL = 'https://core-electronics.com.au/catalogsearch/result/?q=raspberry+pi+compute+module+4'


def req(url) -> requests.models.Response or str:
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return r
    else:
        print(f"The Status code is: {r.status_code}")
        exit()

res = []
soup = BeautifulSoup(req(BASE_URL).content, 'html.parser')

for data in soup.find_all('a', 'product-item-link'):
    res.append(data['href'])
    pattrn = compile('compute-module-4')
    dataset = list(filter(lambda x: search(pattrn, x) != None, res))

# Title
def Title() -> list:
    res = ''

    for links in dataset[2:8]:
        soup1 = BeautifulSoup(req(links).content, 'html.parser')

        for title in soup1.find_all('h1', attrs={'class': 'page-title'}):
            title = title.get_text(strip=True)
            res += title
    return res.split(',')

# Stock
def Stock() -> list:
    res = []

    for links in dataset[2:8]:
        soup = BeautifulSoup(req(links).content, 'html.parser')

        for stock in soup.find_all(
                            'div', attrs={'class': 'product alert stock'}):
            notInStock = ''.join(stock.find('p'))
            res.append(notInStock)

        for stock in soup.find_all(
                            'p', attrs={'class': 'single-product-ship-note'}):
            inStock = stock.get_text(strip=True)[:8]
            res.append(inStock)
    return res

# Price
def Price() -> list:
    res = []

    for links in dataset[2:8]:
        soup = BeautifulSoup(req(links).content, 'html.parser')

        for data in soup.find_all('span', attrs={'class': 'price'}):
            for price in data:
                res.append(price)
    return res

# Links
def Links() -> list:
    res = []
    
    for links in dataset[2:8]:
        res.append(links)
    return res


print(Title())