import requests
from bs4 import BeautifulSoup
from re import compile, search
import json
import asyncio
#import aiohttp


headers = (
    {'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/103.0.5060.53 Safari/537.36',
                        'Accept-language': 'en-AU, en;q=0.5'}
                        )


BASE_URL = 'https://core-electronics.com.au/catalogsearch/result/?q=compute+module+4'

#* PARSE
def parse_content():
    for link in get_url():
        soup = BeautifulSoup(req(link).content, 'html.parser')  # scrapes data from multiple links

        # Title
        def Title():
            for title in soup.find_all('h1', attrs={'class': 'page-title'}):
                title = title.get_text(strip=True)
                return title
        
        # Stock
        def Stock():
            for stock in soup.find_all(
                                'div', attrs={'class': 'product alert stock'}):
                notInStock = ''.join(stock.find('p'))
                return notInStock

            for stock in soup.find_all(
                                'p', attrs={'class': 'single-product-ship-note'}):
                inStock = stock.get_text(strip=True)[:8]
                return inStock
        
        # Price
        def Price():
            for data in soup.find_all('span', attrs={'class': 'price'}):
                for price in data:
                    return price

        try:
            print(Title())
            print(Stock())
            print(Price())
            print(f"Link is: {link}")
            print()
        except TypeError:
            pass
        

#* REQUEST
def req(url) -> requests.models.Response or str:
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return r
    else:
        print(f"The Status code is: {r.status_code}")
        exit()


#* GET URLs
def get_url() -> list[str]:
    res = []

    soup = BeautifulSoup(req(BASE_URL).content, 
        'html.parser')

    for data in soup.find_all('a', 'product-item-link'):
        res.append(data['href'])

    pattrn = compile('compute-module-4')
    dataset = list(filter(lambda x: search(pattrn, x) != None, res))

    return dataset[2:8]


# def run():
#     print(parse_content())

# run()
