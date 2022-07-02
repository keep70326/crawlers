from logging import root
import requests
from bs4 import BeautifulSoup


root_url = 'https://movies.yahoo.com.tw/chart.html'
re = requests.get(root_url)
re.encoding = 'utf-8'
soup = BeautifulSoup(re.text, 'lxml')
# print(soup)
rows = soup.find_all('div', class_='tr')
# print(rows)
colname = list(rows.pop(0).stripped_strings) #欄位名稱
print(colname)


