import requests
from bs4 import BeautifulSoup


headers = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64)\
                    AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/103.0.5060.53 Safari/537.36',
                            'Accept-language': 'en-AU, en;q=0.5'})


# url = 'https://core-electronics.com.au/raspberry-pi-compute-module-4-lite-1gb-ram.html'
url = 'https://core-electronics.com.au/raspberry-pi-compute-module-4-lite-2gb-ram-wireless.html' 
# url = 'https://core-electronics.com.au/raspberry-pi-compute-module-4-32gb-emmc-4gb-ram-wireless.html'

r = requests.get(url, headers=headers)
print('[Response Code]', r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')


#* TITLE
try:
    for title in soup.find_all(
                        'h1', attrs={'class': 'page-title'}):

        title_ = title.get_text(strip=True)
        print(f"[Title] {title_}")

except AttributeError:
    print('NA')


#* IN_STOCK
def stock() -> str:

    for stock in soup.find_all(
                        'div', attrs={'class': 'product alert stock'}):
        stock_1 = ''.join(stock.find('p'))
        return f"[Stock] {stock_1}"


    for stock in soup.find_all(
                        'p', attrs={'class': 'single-product-ship-note'}):
        stock_2 = stock.get_text(strip=True)[:8]
        return f"[Stock] {stock_2}"


#* Price
try:
    for data in soup.find_all('span', attrs=
                                        {'class': 'price'}):
        for price in data:
            print(f"[Price] {price}")

except AttributeError:
    print('NA')


#TODO make it so that it is able to take other links as well
#TODO make it run indefinitely 

from time import sleep

if __name__ == '__main__':
    while True:
        print(stock())
        sleep(3)