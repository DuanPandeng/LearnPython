# !/usr/bin/python3
# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_Zeppelin(username, password, Browser_V):
	global browser_zep
	cookies = []
	chrome_options = webdriver.ChromeOptions()
	if Browser_V=="False":
		chrome_options.add_argument('--headless')
	chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])
	browser_zep = webdriver.Chrome(chrome_options=chrome_options)
	
	browser_zep.implicitly_wait(30)
	browser_zep.get('http://ferdinand.nioint.com/#/')
	time.sleep(1)
	#print("\n正在登录 Zeppelin")

	browser_zep.implicitly_wait(10)
	cookies_default = browser_zep.get_cookies()

	wait = WebDriverWait(browser_zep, 10)
	button_Date_apply = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'nav-login-btn'))).click()
	time.sleep(1)

	browser_zep.implicitly_wait(10)
	username = browser_zep.find_element_by_id('userName').send_keys('{}'.format(username))
	password = browser_zep.find_element_by_id('password').send_keys('{}'.format(password))
	button_login_2 = browser_zep.find_element_by_xpath('//button[@ng-click="login()"]')
	browser_zep.execute_script("arguments[0].click();", button_login_2)
	time.sleep(1)

	# get cookies
	browser_zep.implicitly_wait(10)
	cookies = browser_zep.get_cookies()
	while cookies==cookies_default:
		time.sleep(1)
		cookies = browser_zep.get_cookies()
	#add cookie
	browser_zep.add_cookie(cookies[0])

def Get_Zeppelin_Results(vin, Veh, Tags, Address):
	global browser_zep
	browser_zep.implicitly_wait(30)
	browser_zep.get(Address)
	time.sleep(1)

	browser_zep.implicitly_wait(30)
	texttype = browser_zep.find_element_by_xpath('//textarea[@class="ace_text-input"][1]')

	texttype.send_keys(Keys.CONTROL,'a')
	texttype.send_keys(Keys.BACK_SPACE)
	texttype.send_keys(r"""%pyspark
	vin={0} # dictionary
	vehicle="{1}" # vehicle number 
	tags={2}# tag array
	""".format(vin, Veh, Tags).replace('\t',''))
	time.sleep(1)

	button_run = browser_zep.find_element_by_xpath('//button[@uib-tooltip="Run all paragraphs"][1]')
	browser_zep.execute_script("arguments[0].click();", button_run)
	time.sleep(1)
	browser_zep.implicitly_wait(10)
	button_run_ok = browser_zep.find_element_by_xpath('//button[text()="OK"]')
	browser_zep.execute_script("arguments[0].click();", button_run_ok)
	print("数据分析中... 可能要持续几分钟的时间.\n")
	time.sleep(1)

	status = browser_zep.find_element_by_xpath('//div[@id="main"]/div/div[2]/div[3]//div[@class="control ng-scope"]/span[2]')
	while status.text != "RUNNING":
		time.sleep(1)
	#print(status.text)
	while status.text != "FINISHED":
		time.sleep(1)
	browser_zep.implicitly_wait(10)
	Zep_Result_P = browser_zep.find_element_by_xpath('//div[contains(@class, "plainTextContent")]')
	#print(Zep_Result_P.text)
	Zep_Result = Zep_Result_P.text.split('\n\n')
	return Zep_Result

def Browser_zep_flag():
	global browser_zep
	if 'browser_zep' in dir():
		return True
	else:
		return False

def Browser_zep_Close():
	global browser_zep
	browser_zep.quit()


if __name__ == '__main__':
	username = "pandeng.duan"
	password = "Mynio20190408"
	vin = '{"MP2-592":"LJ1EEAUU1J7700592","MP2-009":"LJ1EEAUU6J7701009","MP2-215":"LJ1EEAUU9J7701215","MP2-625":"LJ1EEAUU1J7700625","MP2-626":"LJ1EEAUU3J7700626","MP2-627":"LJ1EEAUU5J7700627","MP2-629":"LJ1EEAUU9J7700629","MP2-583":"LJ1EEAUU0J7700583","6TT-016":"LJ1E6A2U7K7700016", "abc":"1"}'

	login_Zeppelin(username,password)
	Get_Zeppelin_Results(vin, "MP2-592", ["20190527T130913","20190526T213333"], 'http://ferdinand.nioint.com/#/notebook/2E9SCEHU4')

