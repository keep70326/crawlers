from logging import root
import requests
from bs4 import BeautifulSoup

root_url = "https://disp.cc/b/"

re = requests.get("https://disp.cc/b/PttHot")
soup = BeautifulSoup(re.text, 'html.parser')
spans = soup.find_all('span', class_='listTitle')

for span in spans:
    href = span.find('a').get('href')
    if href == "796-59l9":
        break
    url = root_url + href
    title = span.text 
    # print(title)
    # print(url)
    print(f'{title}\n{url}')

