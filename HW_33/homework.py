import requests
import csv
from bs4 import BeautifulSoup


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):  # ссылка на сайт/файл
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        products = self.html.find_all('div', class_='img_block32')

        for item in products:
            title = item.find('div', class_='title').text
            author = item.find('div', class_='pretitle').text
            journal = item.find('div', class_='sublink').find('a').text
            science = item.find('div', class_='sublink').find_all('a')[1].text
            self.res.append({
                'title': title,
                'author': author,
                'journal': journal,
                'science': science
            })

# Текстовый файл
    # def save_doc(self):
    #     with open(self.path, 'w') as f:
    #         for item in self.res:
    #             f.write(f'Название статьи: {item["title"]}\nАвтор: {item["author"]}\n'
    #                     f'Журнал: {item["journal"]}\nОбласть: {item["science"]}\n\n')

    def save_exel(self):
        with open(self.path, 'a') as f:
            writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=list(self.res[0].keys()))
            writer.writeheader()
            for d in self.res:
                writer.writerow(d)

    def run(self):
        self.get_html()
        self.parsing()
        # self.save_doc()
        self.save_exel()
