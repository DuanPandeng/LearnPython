from selenium import webdriver
import time
import requests
import json

browser = webdriver.Chrome()
browser.get('http://luna.nioint.com/')
browser.implicitly_wait(60)

username = browser.find_element_by_id('phone').send_keys('XXX@XXX.com')
password = browser.find_element_by_id('pwd').send_keys('XXXXXXXX')
button = browser.find_element_by_id('login-button').click()
time.sleep(1)

# get cookies
browser.implicitly_wait(5)
cookies = browser.get_cookies()
print(cookies)
print(type(cookies[0]))

#get token
token=browser.execute_script('return window.localStorage.getItem("vue-auth-token")')
print(token)

# f1 = open('cookie.txt', 'w')
# f1.write(json.dumps(cookies))
# f1.close
