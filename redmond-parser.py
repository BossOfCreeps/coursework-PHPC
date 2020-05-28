import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint

URL = "https://multivarka.pro/catalog/elektroplitki/"
HOST = "https://multivarka.pro"
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/81.0.4044.138 YaBrowser/20.4.2.201 Yowser/2.5 Yptp/1.21 Safari/537.36",
           "accept": "*/*"}


def get_page_links(html):
    soup = BS(html, "html.parser")
    links = []
    items = soup.find_all('div', class_="product-item-img")
    for item in items:
        links.append(HOST + item.find('a').get('href'))
    return links


def get_links():
    html = requests.get(URL, headers=HEADERS)
    links = get_page_links(html.text)
    return links


def get_texts():
    links = get_links()
    with open('redmond.txt', 'w') as f:
        for link in links:
            soup = BS(requests.get(link, headers=HEADERS).text, "html.parser")
            items = soup.find_all('div', class_='text')
            for item in items:
                f.write("%s\n" % ''.join([char for char in item.text if 1024 <= ord(char) <= 1279 or ord(char)==32]))


if __name__ == "__main__":
    start = datetime.now()
    print("Start:", start)
    get_texts()
    finish = datetime.now()
    print("Finish:", finish)
    print("Time:", finish-start)