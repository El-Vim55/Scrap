import requests
from bs4 import BeautifulSoup
import re
import json
from random import randint
#import aiohttp
#import asyncio


headers = (
    {'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/103.0.5060.53 Safari/537.36',
                        'Accept-language': 'en-AU, en;q=0.5'}
                        )

BASE_URL = 'https://core-electronics.com.au/catalogsearch/result/?q=compute+module+4'


def save_content():
    pass


#* PARSE
def parse_content():
    for i in get_url():
        soup = BeautifulSoup(req(i).content, 'lxml')
        print(soup)


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

    pattrn = re.compile('compute-module-4')
    dataset = list(filter(lambda x: re.search(pattrn, x) != None, res))

    return dataset


def main():
    pass

if __name__ == '__main__':
    # print(get_url())
    parse_content()
