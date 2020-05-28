"""
Выполнить парсинг 10 сайтов по определенной тематике. Итогом парсинга одного сайта является текст, содержащий взятые из
сайта описания. Получить список 200 наиболее используемых слов из полученного текста для каждого сайта (исключить
стоп-слова: предлоги и союзы). Найти слова, которые попадают в список для одних сайтов и отсутствуют на других.
Найти слова, которые присутствуют в списках для всех сайтов.
"""
import csv
from pprint import pprint

shops = ["auchan", "dns", "eldorado", "goods", "kcenter", "leroymerlin", "ozon", "redmond", "stroysya", "wildberries"]

d = {}
for shop in shops:
    FILENAME = "aaa-{}.csv".format(shop)
    l = []
    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            l.append(row[0])
    d[shop] = l

for shop in shops:
    l = []
    for shop1 in shops:
        if shop1 != shop:
            for word in d[shop1]:
                l.append(word)
    print(shop, set(d[shop]) - set(l))

# Найти слова, которые присутствуют в списках для всех сайтов
print(set(d["auchan"]) & set(d["dns"]) & set(d["eldorado"]) & set(d["goods"]) & set(d["kcenter"]) &
      set(d["leroymerlin"]) & set(d["ozon"]) & set(d["redmond"]) & set(d["stroysya"]) & set(d["wildberries"]))
