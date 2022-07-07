from selenium import webdriver #THSR台灣高鐵
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


chromedriver = '/Users/yunping/Desktop/crawlers/selenium/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.thsrc.com.tw/')
driver.maximize_window()

cookie = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/button[2]')
cookie.click()

start = driver.find_element(By.ID, "select_location01") #啟程站
Select(start).select_by_visible_text('新竹')
end = driver.find_element(By.ID, "select_location02") #到達站
Select(end).select_by_visible_text('板橋')

driver.find_element(By.ID, 'start-search').click()

driver.implicitly_wait(5)

time = driver.find_elements(By.CLASS_NAME, 'font-16r')

timetable = []
for t in time:
    timetable.append(t.text)

print(timetable)

