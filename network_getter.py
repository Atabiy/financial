import requests
from bs4 import BeautifulSoup
##############################################################
url = 'https://www.vbr.ru/banki/kurs-valut/prodaja-usd/'
resp = requests.get(url).content
soup = BeautifulSoup(resp, 'html.parser')

def cleaner(text):
    ans = ''
    for i in text:
        if i in '0123456789,':
            ans += i
    return ans

def get_dollar(soup):
    doll = soup.find_all('td', class_= "rates-val")
    db = cleaner(doll[0].text)
    ds = cleaner(doll[1].text)
    return db, ds

db, ds = get_dollar(soup)
##############################################################
url = 'https://www.vbr.ru/banki/kurs-valut/prodaja-eur/'
resp = requests.get(url).content
soup = BeautifulSoup(resp, 'html.parser')

def get_euro(soup):
    eur = soup.find_all('td', class_= "rates-val")
    eb = cleaner(eur[0].text)
    es = cleaner(eur[1].text)
    return eb, es

eb, es = get_euro(soup)
