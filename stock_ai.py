import requests
import pprint




re = requests.get('https://chart.stock-ai.com/history?symbol=AAPL&resolution=D&from=1617590780&to=1656902840')  #如果加上verify=False則可以跳過ssl驗證
if re.status_code == 200:
    # pprint.pprint(re.json())
    data = re.json()

    zipdata = zip(data['t'], data['o'], data['h'], data['l'], data['c'], data['v'])
    pprint.pprint(list(zipdata))
