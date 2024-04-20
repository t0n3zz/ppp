import requests
from bs4 import BeautifulSoup
import time


DOLLAR_RUB = 'https://www.finmarket.ru/currency/rates/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}


def usd():
    full_page = requests.get(DOLLAR_RUB, headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')

    convert = (soup.findAll('div', {'class': 'value'})[0]).text
    print(convert)
    time.sleep(1)

