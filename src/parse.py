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

#? The frontend for the site keeps changing, perhaps theres a way to use different urls?
BASE_URL = 'https://core-electronics.com.au/raspberry-pi/boards/compute-module-4/wireless.html?aw_shopbybrand_brand=359&cat=1396%2C1397%2C1398&price=30.00-100.00'
# BASE_URL = 'https://core-electronics.com.au/catalogsearch/result/?q=raspberry+pi+compute+module+4'

def req(url) -> requests.models.Response or str:
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return r
    else:
        print(f"The Status code is: {r.status_code}")
        exit()

res = []
soup = BeautifulSoup(req(BASE_URL).content, 'lxml')

for data in soup.find_all('a', 'product-item-link'):
    res.append(data['href'])
    pattrn = compile('compute-module-4')
    dataset = list(filter(lambda x: search(pattrn, x) != None, res))
    dataset = dataset[::-1]

# Title
def Title() -> list:
    res = []

    for links in dataset[1:]:
        soup1 = BeautifulSoup(req(links).content, 'lxml')

        for title in soup1.find_all('h1', attrs={'class': 'page-title'}):
            title = title.get_text(strip=True)
            res.append(title)
    return res

# Stock
def Stock() -> list:
    res = []

    for links in dataset[1:]:
        soup = BeautifulSoup(req(links).content, 'lxml')

        for stock in soup.find_all(
                            'div', attrs={'class': 'product alert stock'}):
            notInStock = ''.join(stock.find('p'))
            res.append(notInStock)

        for stock in soup.find_all(
                            'p', attrs={'class': 'single-product-ship-note'}):
            inStock = stock.get_text(strip=True)[:8]
            res.append(inStock)
    return list(filter(None, res))

# Price
def Price() -> list:
    res = []

    for links in dataset[1:]:
        soup = BeautifulSoup(req(links).content, 'lxml')

        for data in soup.find_all('span', attrs={'class': 'price'}):
            for price in data:
                res.append(price)
    return res

# Links
def Links() -> list:
    res = []
    
    for links in dataset[1:]:
        res.append(links)
    return res
