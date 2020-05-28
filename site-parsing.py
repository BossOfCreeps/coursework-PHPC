import requests
from bs4 import BeautifulSoup as BS

URL = "https://auto.ria.com/newauto/marka-jeep/"
HOST = "https://auto.ria.com"
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/81.0.4044.138 YaBrowser/20.4.2.201 Yowser/2.5 Yptp/1.21 Safari/537.36",
           "accept": "*/*"}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BS(html, "html.parser")

    cars = []
    items = soup.find_all('div', class_='proposition')
    for item in items:
        uah_price = item.find('span', class_='grey size13')
        if uah_price:
            uah_price = uah_price.get_text()
        else:
            uah_price = 'Цена в гривнах не указана'
        cars.append({
            'titel': item.find ('h3', class_='proposition_name').get_text(strip=True),
            'link': HOST + item.find('a').get('href'),
            'usd_price': item.find('span', class_='green').get_text(),
            'uah_price': uah_price,
            'citi': item.find('svg', class_='svg svg-i16_pin').find_next('strong').get('title'),
        })
    from pprint import pprint
    pprint(cars)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("Error")


if __name__ == "__main__":
    parse()