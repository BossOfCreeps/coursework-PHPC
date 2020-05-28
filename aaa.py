"""
Выполнить парсинг 10 сайтов по определенной тематике. Итогом парсинга одного сайта является текст, содержащий взятые из
сайта описания. Получить список 200 наиболее используемых слов из полученного текста для каждого сайта (исключить
стоп-слова: предлоги и союзы). Найти слова, которые попадают в список для одних сайтов и отсутствуют на других.
Найти слова, которые присутствуют в списках для всех сайтов.
"""
import csv
import operator
import re

text_string = open('wildberries.txt', 'r').read().lower()
match_pattern = re.findall(r'\b[а-я]{3,15}\b', text_string)

frequency = {}
for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

bad_words = ["для", "это", "при", "что", "без", "вам", "этого", "всех", "или", "и"]
for w in bad_words:
    frequency[w] = 0


with open("aaa-wildberries.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)[:200])