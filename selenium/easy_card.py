from selenium import webdriver #悠遊卡
from selenium.webdriver.common.by import By

CARD_NUMBER = ''
BIRTHDAY = ''
CHROMEDRIVER = '/Users/yunping/Desktop/crawlers/selenium/chromedriver'

class Card:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROMEDRIVER)

    def run(self):
        self.go_to_website()
        self.enter_data()
        self.select_radio_button()
        self.wait_robot_ckeck()
        self.click_search()
        self.get_data()

    def go_to_website(self):
        self.driver.get('https://ezweb.easycard.com.tw/search/CardSearch.php')

    def enter_data(self):
        card_number_input = self.driver.find_element(By.NAME, 'card_id')
        card_number_input.send_keys(CARD_NUMBER)
        birthday_input = self.driver.find_element(By.NAME, 'birthday')
        birthday_input.send_keys(BIRTHDAY)

    def select_radio_button(self):
        button = self.driver.find_element(By.ID, 'date3m')
        button.click()

    def wait_robot_ckeck(self):
        input('press enter when done with robot check')

    def click_search(self):
        search_button = self.driver.find_element(By.ID, 'btnSearch')
        search_button.click()

    def get_data(self):
        self.driver.implicitly_wait(3)
        rows = self.driver.find_element(By.CLASS_NAME, 'r1')
        for row in rowa:
            print(row.text)


if __name__ == '__main__':
    c = Card()
    c.run()



