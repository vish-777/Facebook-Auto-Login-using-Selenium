from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = 'fb_email@email.com'
password = 'fb_password'

url = 'https://www.facebook.com/'

driver = webdriver.Chrome("C:\Python\Python38\Scripts\chromedriver")

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)

time.sleep(2)

driver.find_element_by_id('loginbutton').click()

driver.close()

