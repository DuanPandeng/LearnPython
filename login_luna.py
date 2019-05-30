from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from pandas import Series, DataFrame
from login_zeppelin import *


start_date = "4.10"
end_date = "4.10"
tags = []
comments = []
Veh = "MP2-626"
Lat_address = 'http://ferdinand.nioint.com/#/notebook/2EBQR8AX8'
Lon_address = 'http://ferdinand.nioint.com/#/notebook/2E92CZMRA'

Months_dict = {'January':1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}

def Login_Luna(browser):
	browser.implicitly_wait(30)
	browser.get('http://luna.nioint.com/')
	time.sleep(3)

	browser.implicitly_wait(10)
	username = browser.find_element_by_id('phone').send_keys('pandeng.duan@nio.com')
	password = browser.find_element_by_id('pwd').send_keys('Mynio20190408')
	button = browser.find_element_by_id('login-button').click()
	time.sleep(1)

	#add token
	token=browser.execute_script('return window.localStorage.getItem("vue-auth-token")')
	js='window.localStorage.setItem("vue-auth-token", "{0}")'.format(token)
	browser.execute_script(js)
	return

def Set_Conditions(browser, start_date, end_date, Veh):
	browser.implicitly_wait(30)
	browser.get('http://luna.nioint.com/#/analyze')
	time.sleep(1)

	browser.implicitly_wait(10)
	button_cal = browser.find_element_by_class_name('input-date')
	browser.execute_script("arguments[0].click();", button_cal)
	time.sleep(1)


	browser.implicitly_wait(10)
	Months_Left_P = browser.find_element_by_class_name('months-text')
	Months_Left = Months_Left_P.text.split()[0]
	Months_Left_int = Months_dict[Months_Left]
	Months_start = int(start_date.split('.')[0])
	Days_start = int(start_date.split('.')[1])
	Days_end = int(end_date.split('.')[1])
	Months_dif = Months_start - Months_Left_int

	if Months_dif == 0:
		pass

	elif Months_dif < 0:
		while Months_dif != 0:
			browser.implicitly_wait(10)
			Button_Months_Pre = browser.find_element_by_xpath('//div[@class="calendar_month_left"]/div[1]/i[1]')
			browser.execute_script("arguments[0].click();", Button_Months_Pre)
			Months_dif += 1
			time.sleep(0.5)

	elif Months_dif > 0:
		while Months_dif != 0:
			browser.implicitly_wait(10)
			Button_Months_Next = browser.find_element_by_xpath('//div[@class="calendar_month_right"]/div[1]/i[1]')
			browser.execute_script("arguments[0].click();", Button_Months_Next)
			Months_dif -= 1
			time.sleep(0.5)

	browser.implicitly_wait(10)
	button_start_date = browser.find_element_by_xpath('//div[@class="calendar_month_left"]//li[text()="%s"]' % Days_start)
	browser.execute_script("arguments[0].click();", button_start_date)
	button_end_date = browser.find_element_by_xpath('//div[@class="calendar_month_left"]//li[text()="%s"]' % Days_end)
	browser.execute_script("arguments[0].click();", button_end_date)
	time.sleep(1)

	browser.implicitly_wait(10)
	button_Date_apply = browser.find_element_by_class_name('calendar-btn-apply').click()
	time.sleep(1)

	browser.implicitly_wait(10)
	button_veh = browser.find_element_by_xpath('//li[contains(text(), "%s")]' % Veh)
	browser.execute_script("arguments[0].click();", button_veh)
	time.sleep(3)
	return

def Download_info(browser):
	browser.implicitly_wait(10)
	button_next_page = browser.find_element_by_xpath('//li[@title="下一页"]')
	while button_next_page.get_attribute('class') == 'ivu-page-next':
		browser.implicitly_wait(10)
		tag_elements = browser.find_elements_by_xpath('//tbody[1]/tr/td[3]/div')
		comment_elements = browser.find_elements_by_xpath('//tbody[1]/tr/td[9]//span')
		for i in range(len(tag_elements)):
			tags.append(tag_elements[i].text)
			comments.append(comment_elements[i].text)
		browser.execute_script("arguments[0].click();", button_next_page)
		time.sleep(5)
		browser.implicitly_wait(10)
		button_next_page = browser.find_element_by_xpath('//li[@title="下一页"]')

	tag_elements = browser.find_elements_by_xpath('//tbody[1]/tr/td[3]/div')
	comment_elements = browser.find_elements_by_xpath('//tbody[1]/tr/td[9]//span')
	for i in range(len(tag_elements)):
		tags.append(tag_elements[i].text)
		comments.append(comment_elements[i].text)
	
	return tags, comments

def DF_Zep_Result(df, address, Veh):
	login_Zeppelin()
	Tags_list = df.Tag_Number.tolist()
	Zep_Result = Get_Zeppelin_Results(Veh, Tags_list, address)
	if Zep_Result=={}:
		return df
	else:
		for key, value in Zep_Result.items():
			for i in range(len(df)):
				if df.iloc[i,0] == key[4:]:
					df.iloc[i,2] = value
		return df

def Add_Analysis_Each_Page(browser, Numb, Content):
	arr = list(range(0, 500, 20))
	browser.implicitly_wait(10)
	Button_Page = browser.find_element_by_xpath('//li[text()="上一页"]/../li[2]')
	browser.execute_script("arguments[0].click();", Button_Page)
	time.sleep(1)

    for i in range(1, len(arr)):
    	if Numb < arr[i]:
    		Page = i
    		Numb_Page = Numb - arr[i-1]
    		break        
        else:
    		Button_Page = browser.find_element_by_xpath('//li[text()="上一页"]/../li[{}]'.format(i+2)) 
    		browser.execute_script("arguments[0].click();", Button_Page)
			time.sleep(1)

	Add_Analysis(browser, Numb_Page, Content)



def Add_Analysis(browser, Numb_Page, Content):

	browser.implicitly_wait(10)
	button_analyze = browser.find_element_by_xpath('//tbody[@class="ivu-table-tbody"]/tr[%d]//span[text()="analyze"]/..' % Numb_Page)
	browser.execute_script("arguments[0].click();", button_analyze)
	time.sleep(1)

	browser.implicitly_wait(10)
	texttype_analyze = browser.find_element_by_xpath('//label[text()="分析结论"]/../div[1]/div[1]/textarea')
	texttype_analyze.send_keys(Keys.CONTROL,'a')
	texttype_analyze.send_keys(Keys.BACK_SPACE)
	texttype_analyze.send_keys("{}".format(Content))
	time.sleep(1)

	browser.implicitly_wait(10)
	button_submit = browser.find_element_by_xpath('//span[text()="Submit"]/..')
	browser.execute_script("arguments[0].click();", button_submit)


browser = webdriver.Chrome()
Login_Luna(browser)
time.sleep(2)
Set_Conditions(browser, start_date, end_date, Veh)
time.sleep(1)
Tags, Comments = Download_info(browser)

dic = {'Tag_Number':Tags, 'Comment':Comments}
Tag_Comment = pd.DataFrame(dic)
Tag_Comment['Analysis'] = "NaN"

DF_Lat_Q = Tag_Comment[Tag_Comment['Comment'].str.contains("横向退出")]
DF_Lon_Q = Tag_Comment[Tag_Comment['Comment'].str.contains("Pilot自动退出")] 


if len(DF_Lat_Q)>=1: 
	DF_Lat_Q_A = DF_Zep_Result(DF_Lat_Q, Lat_address, Veh)
	DF_Lat_Q_A_Lon = DF_Lat_Q_A[DF_Lat_Q_A['Analysis'].str.contains("Pilot-Lon Quit first")]
	if len(DF_Lat_Q_A_Lon) != 0:
		DF_Lat_Q_A.drop(list(DF_Lat_Q_A_Lon.index), inplace=True)
	print("\nPilot横向退出问题列表：\n")
	print(DF_Lat_Q_A)
	for i in list(DF_Lat_Q_A.index):
		Add_Analysis_Each_Page(browser, i+1, DF_Lat_Q_A['Analysis'][i])
else:
	print("无Pilot横向退出问题")


if  'DF_Lat_Q_A_Lon' in dir():
	DF_Lon_Q = DF_Lon_Q.add(DF_Lat_Q_A_Lon, fill_value="")
if len(DF_Lon_Q)>=1: 
	DF_Lon_Q_A = DF_Zep_Result(DF_Lon_Q, Lon_address, Veh)
	print("\nPilot纵向退出问题列表：\n")
	print(DF_Lon_Q_A)
	for i in list(DF_Lon_Q_A.index):
		Add_Analysis_Each_Page(browser, i+1, DF_Lon_Q_A['Analysis'][i])
else:
	print("无Pilot纵向退出问题")


