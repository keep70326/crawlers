import requests 
from bs4 import BeautifulSoup
import pandas as pd


data = []
re = requests.get('http://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx')
if re.status_code == requests.codes.ok:
    soup = BeautifulSoup(re.text, 'lxml')
    # print(soup.prettify())

    tables = soup.find_all('table', attrs={'cellpadding':'2'})#找到屬性是2的兩個小表格
    print(tables[0])

    for table in tables:
        trs = table.find_all('tr')
        for tr in trs:
            date, value, price = [td.text for td in tr.find_all('td')]
            print(date, value, price)
            if date == '日期':
                continue
            data.append([date, value, price])

df = pd.DataFrame(data, columns=['日期', '買賣超金額', '台指期'])
df.to_csv('eight_bank.csv')
# print(data)
