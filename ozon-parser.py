import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint

URL = "https://www.ozon.ru/category/elektricheskie-plity-31820/"
HOST = "https://www.ozon.ru"
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.4.2.201 Yowser/2.5 Yptp/1.21 Safari/537.36",
           "accept": "*/*"}


def get_page_links(html):
    soup = BS(html, "html.parser")
    links = []
    items = soup.find_all('a', class_='a3a3 tile-hover-target')
    for item in items:
        links.append(HOST + item.get('href'))
    return links


def get_links():
    links = []
    i = 0
    while True:
        i += 1
        html = requests.get(URL, headers=HEADERS, params={"page": i})
        page_links = get_page_links(html.text)
        if len(page_links):
            links = [*links, *page_links]
        else:
            break
    return links


def get_texts():
    links = get_links()
    with open('ozon.txt', 'wb') as f:
        for link in links:
            pprint(link)
            p = requests.get(link, headers=HEADERS).text
            s = p.find(""","description":""")+16
            q = p.find("""\","image":\"""")
            print(p[s:q])
            print(type(p[s:q]))
            f.write("{}\n".format(p[s:q]).encode())


if __name__ == "__main__":
    start = datetime.now()
    print("Start:", start)
    get_texts()
    finish = datetime.now()
    print("Finish:", finish)
    print("Time:", finish-start)