from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
import os
import time
import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint

def crawl(date):
    print('crawling', date.strftime('%Y/%m/%d'))
    r = requests.get('https://www.taifex.com.tw/cht/3/futContractsDate?queryDate={}%2F{}%2F{}'.format(date.year, date.month, date.day))
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'lxml')

    try:
        table = soup.find('table', class_='table_f')
        trs = table.find_all('tr')
    except AttributeError:
        print('今日無資料', date.strftime('%Y/%m/%d'))  # 休假日
        return
    
    rows = trs[3:]
    data = {}
    for row in rows:
        ths = row.find_all('th')
        titles = [th.text.strip() for th in ths]
        
        if titles[0] == '期貨小計':
            break

        if len(titles) == 3:
            product = titles[1]
            who = titles[2]
        else:
            who = titles[0]
        
        tds = row.find_all('td')
        cells = [td.text.strip() for td in tds]

        row_data = [product, who] + cells
        
        converted = [int(d.replace(',', '')) for d in row_data[2:]]
        row_data = row_data[:2] + converted

        headers = ['商品', '身份別', '交易多方口數', '交易多方金額', '交易空方口數', '交易空方金額', '交易淨口數', '交易淨金額',
         '未平倉多方口數', '未平倉多方金額', '未平倉空方口數', '未平倉空方金額', '未平倉淨口數', '未平倉淨金額']

        
        # product -> who -> what
        product = row_data[0]
        who = row_data[1]
        contents = {headers[i]: row_data[i] for i in range(2, len(headers))}

        if product not in data:
            data[product] = {who: contents}
        else:
            data[product][who] = contents

    # pprint(data)
    # print(data['臺股期貨']['外資']['未平倉淨口數'])

    return date, data


def save_json(date, data, path):
    filename = os.path.join(path, 'futures_' + date.strftime('%Y%m%d') + '.json')
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)  # ensure_ascii=False 讓中文字可正常存檔
    print('另存新檔', filename)


def main():
    download_dir = 'futures'
    os.makedirs(download_dir, exist_ok=True)

    start = time.time()
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        today = datetime.today()
        date = today

        while True:
            future = executor.submit(crawl, date)
            futures.append(future)

            date = date - timedelta(days=1)
            if date <= today - timedelta(days=730):
                break

        for future in as_completed(futures):
            if future.result():  # 如果有拿到表格資料
                date, data = future.result()
                save_json(date, data, download_dir)

    end = time.time()
    print(f'下載資料共花費{end - start}秒')


if __name__ == '__main__':
    main()