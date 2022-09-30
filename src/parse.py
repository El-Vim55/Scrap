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

class Urls():
    CORE_ELEC_CM4_URL = 'https://core-electronics.com.au/raspberry-pi/boards/compute-module-4/wireless.html?aw_shopbybrand_brand=359&cat=1397%2C1398&price=30.00-100.00'
    CORE_ELEC_RPI4_URL = 'https://core-electronics.com.au/catalogsearch/result/?q=RPi+4+model+B'

def req(url) -> requests.models.Response or str:
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print(f"The Status code is: {r.status_code}")
        exit()
    else:
        return r

def many_soup(url, pattern) -> list:
    res = []
    soup = BeautifulSoup(req(url).content, 'lxml')

    for data in soup.find_all('a', 'product-item-link'):
        res.append(data['href'])
        pattrn = compile(f'{pattern}')
        dataset = list(filter(lambda x: search(pattrn, x) != None, res))
    return dataset

# Title
def Title(args) -> list:
    res = []

    for links in args:
        soup = BeautifulSoup(req(links).content, 'lxml')

        for title in soup.find_all('h1', attrs={'class': 'page-title'}):
            title = title.get_text(strip=True)
            res.append(title)
    return res

# Stock
def Stock(args) -> list:
    res = []

    for links in args:
        soup = BeautifulSoup(req(links).content, 'lxml')

        for stock in soup.find_all(
                            'div', attrs={'class': 'product alert stock'}):
            notInStock = ''.join(stock.find('p')).replace('Out of Stock', 'No')
            res.append(notInStock)

        for stock in soup.find_all(
                            'p', attrs={'class': 'single-product-ship-note'}):
            inStock = stock.get_text(strip=True)[:8].replace('In stock', 'Yes')
            res.append(inStock)
    return list(filter(None, res))

# Price
def Price(args) -> list:
    res = []

    for links in args:
        soup = BeautifulSoup(req(links).content, 'lxml')

        for data in soup.find_all('span', attrs={'class': 'price'}):
            for price in data:
                res.append(price)
    return res

# Links
def Links(args) -> list:
    res = []
    
    for links in args:
        res.append(links)
    return res
