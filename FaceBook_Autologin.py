
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass

username = input("Enter in your username: ")
password = getpass("Enter your password: ")

driver = webdriver.Chrome("C:\Python\Python38\Scripts\chromedriver")
driver.get("https://www.facebook.com/")

username_textbox = driver.find_element_by_id("email")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("pass")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("u_0_b") 
login_button.submit()
