import requests
from bs4 import BeautifulSoup


def get_html(url):
    res = requests.get(url)
    return res.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find('main', class_='js-main').find_all('div', class_='product-price-amount')[1].\
        find('div', class_='price').text
    print(p1)
    p2 = soup.find('div', class_='front').find('a', class_='image-wrapper')['href']
    print(p2)


def main():
    url = 'https://www.toledo24.pro/?utm_source=yandex&utm_medium=cpc&utm_campaign=ep-smb-toledo_yandex_shopping&utm_' \
          'content=5164590395_13818065255_desktop_%7Cpid%7C7_7%7Ccid%7C85684202%7Cgid%7C5164590395%7Caid%7C1' \
          '3818065255%7Cadp%7Cno%7Cpos%7Cpremium1%7Csrc%7Csearch_none%7Cdvc%7Cdesktop_47_Нижний%20Новгород_premium_' \
          '1_0&utm_term=&_openstat=ZGlyZWN0LnlhbmRleC5ydTs4NTY4NDIwMjsxMzgxODA2NTI1NTt5YW5kZXgucnU6cHJlbWl1bQ&yclid=' \
          '11768928951299997695'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
