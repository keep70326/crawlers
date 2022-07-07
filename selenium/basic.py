from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


chromedriver = '/Users/yunping/Desktop/crawlers/selenium/chromedriver'

driver = webdriver.Chrome(chromedriver)
driver.get('https://www.google.com')

search = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")


search.send_keys('曲面螢幕')
search.send_keys(Keys.RETURN) #Return是Enter
# driver.quit()
