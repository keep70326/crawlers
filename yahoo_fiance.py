import requests
from bs4 import BeautifulSoup

re = requests.get('https://tw.stock.yahoo.com/q/q?s=2330')
if re.status_code == requests.codes.ok:
    soup = BeautifulSoup(re.text, 'html.parser')
    table = soup.find_all('table')[2]
    print(table)

    price = table.find_all('td')[2]
    buy_price = price.find_next('td')
    sell_price = buy_price.find_next('td')

    print(price.text, buy_price.text, sell_price.text)

