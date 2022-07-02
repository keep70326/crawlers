from email import message
import requests
from bs4 import BeautifulSoup


root_url = input("請輸Dcard文章網址：")

def article_exist(article):
    resp = requests.get(article)

    if resp.status_code == 200:
        return resp.text 

    else:
        print('此篇文章不存在、或被移除了')
        return None


def get_comments(post_exist):
        soup = BeautifulSoup(post_exist, 'html.parser')
        title = soup.find('h1', class_="sc-ae7e8d73-0 llageZ").text
        print('找到該文章：', title)

        floor = soup.find_all('div', class_="sc-7ea8de7c-1 ekmZNL")
        all_floor = ([n.text for n in floor][3].split( ))
        all_floor = all_floor[1]#留言有幾樓
        return all_floor


def get_data():
    data = {}
    post_exist = article_exist(root_url)
    all_floor = int(get_comments(post_exist))
    print(all_floor)

    for floor in range(all_floor):
        floor = floor + 1 
        url = f'{root_url}/b/{floor}'
        # print(url)
        re = requests.get(url)
        soup = BeautifulSoup(re.text, 'html.parser')
        user = soup.find('span', class_="sc-5fc81f2a-2 caxKwD")
        # print(user)
        # all_user = [u.text for u in user][3:] #扣除愛心數最高的3個熱門留言
        message = soup.find('div', class_="sc-8ec6ca7a-0 eqOEKX")
        # all_message = [me.text for me in message][4:] #扣除愛心數最高的3個熱門留言
        data[user] = message



if __name__ == "__main__":
    data = get_data()
        

        

    


    

