import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint

URL = "https://leroymerlin.ru/catalogue/kuhonnye-plity/"
HOST = "https://leroymerlin.ru"
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/81.0.4044.138 YaBrowser/20.4.2.201 Yowser/2.5 Yptp/1.21 Safari/537.36",
           "accept": "*/*"}


def get_page_links(html):
    soup = BS(html, "html.parser")
    links = []
    items = soup.find_all('a', class_='black-link product-name-inner')
    for item in items:
        links.append(HOST + item.get('href'))
    return links


def get_links():
    links = []
    i = 0
    while i==0:
        i += 1
        html = requests.get(URL, headers=HEADERS)
        page_links = get_page_links(html.text)
        if len(page_links):
            links = [*links, *page_links]
        else:
            break
    return links


def get_texts():
    links = get_links()
    with open('leroymerlin.txt', 'w') as f:
        for link in links:
            soup = BS(requests.get(link, headers=HEADERS).text, "html.parser")
            items = soup.find_all('section', class_="pdp-section pdp-section--product-description")
            for item in items:
                print(item.text)
                f.write("%s\n" % ''.join([char for char in item.text if 1024 <= ord(char) <= 1279 or ord(char)==32]))


if __name__ == "__main__":
    start = datetime.now()
    print("Start:", start)
    get_texts()
    finish = datetime.now()
    print("Finish:", finish)
    print("Time:", finish-start)