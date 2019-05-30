from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from pandas import Series, DataFrame


def login_Zeppelin():	
	cookies = []
	global browser
	browser = webdriver.Chrome()
	browser.implicitly_wait(30)
	browser.get('http://ferdinand.nioint.com/#/')
	time.sleep(1)

	browser.implicitly_wait(10)
	cookies_default = browser.get_cookies()

	browser.implicitly_wait(10)
	button_login_1 = browser.find_element_by_class_name('nav-login-btn')
	browser.execute_script("arguments[0].click();", button_login_1)
	time.sleep(1)

	browser.implicitly_wait(10)
	username = browser.find_element_by_id('userName').send_keys('pandeng.duan')
	password = browser.find_element_by_id('password').send_keys('Mynio20190408')
	button_login_2 = browser.find_element_by_xpath('//button[@ng-click="login()"]')
	browser.execute_script("arguments[0].click();", button_login_2)
	time.sleep(1)

	# get cookies
	browser.implicitly_wait(10)
	cookies = browser.get_cookies()
	while cookies==cookies_default:
		time.sleep(1)
		cookies = browser.get_cookies()
	# #add cookie
	browser.add_cookie(cookies[0])



def Get_Zeppelin_Results(Veh, Tags, Address):
	global browser
	browser.implicitly_wait(30)
	browser.get(Address)
	time.sleep(1)

	browser.implicitly_wait(30)
	texttype = browser.find_element_by_xpath('//textarea[@class="ace_text-input"][1]')

	texttype.send_keys(Keys.CONTROL,'a')
	texttype.send_keys(Keys.BACK_SPACE)
	texttype.send_keys(r"""%pyspark
	vin={{"MP2-592":"LJ1EEAUU1J7700592","MP2-009":"LJ1EEAUU6J7701009","MP2-215":"LJ1EEAUU9J7701215","MP2-625":"LJ1EEAUU1J7700625","MP2-626":"LJ1EEAUU3J7700626","MP2-627":"LJ1EEAUU5J7700627","MP2-629":"LJ1EEAUU9J7700629","MP2-583":"LJ1EEAUU0J7700583","6TT-016":"LJ1E6A2U7K7700016"}} # dictionary
	vehicle="{0}" # vehicle number 
	tags={1}# tag array
	""".format(Veh, Tags).replace('\t',''))

	button_run = browser.find_element_by_xpath('//button[@uib-tooltip="Run all paragraphs"][1]')
	browser.execute_script("arguments[0].click();", button_run)
	time.sleep(1)
	browser.implicitly_wait(10)
	button_run_ok = browser.find_element_by_xpath('//button[text()="OK"]')
	browser.execute_script("arguments[0].click();", button_run_ok)
	print("\nData Analysing... This may take a few minutes, go get a cup of coffee!")
	time.sleep(5)

	status = browser.find_element_by_xpath('//div[@id="main"]/div/div[2]/div[3]//div[@class="control ng-scope"]/span[2]')
	print(status.text)

	while status.text != "FINISHED":
		time.sleep(1)
	browser.implicitly_wait(10)
	Zep_Result_P = browser.find_element_by_xpath('//div[contains(@class, "plainTextContent")]')
	Zep_Result = Zep_Result_P.text.split('\n\n')
	Zep_Result_split=[]
	Zep_Result_Dict={}
	for i in Zep_Result:
		if len(i.split('\n'))==2:
			Zep_Result_split.append(i.split('\n'))
	if len(Zep_Result_split) != 0:
		Zep_Result_Dict = dict(Zep_Result_split)
	return Zep_Result_Dict


if __name__ == '__main__':
	login_Zeppelin()
	Get_Zeppelin_Results("MP2-592", ["20190527T130913","20190526T213333"], 'http://ferdinand.nioint.com/#/notebook/2E9SCEHU4')


#ActionChains(browser).move_to_element(texttype).perform()
# span_vehicle = browser.find_element_by_xpath('//span[@class="ace_identifier" and text()="vehicle"]/../span[@class="ace_string"]')
# print(span_vehicle.text)
# time.sleep(1)


