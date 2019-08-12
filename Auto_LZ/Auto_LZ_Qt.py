#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pandas import DataFrame
from pandas import ExcelWriter
from Login_Zeppelin_Qt import *
import xlrd
import xlwt
from xlutils.copy import copy


Months_dict = {'January':1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
Fun_dict = {'AEB':1, 'BSD':2, 'LDW':3, 'LCA':4, 'SDO':5, 'AHBC':6, 'FCTA':7, 'RCTA':8, 'FCTAB':9, 'APA':10, 'SAPA':11, 'ACC':12, 'TSR':13, 'ISA':14, 'LKS':15, 'ALC':16, 'Pilot-Lat':17, 'Pilot-Lon':18}


def CreatAuto_LZ_file(f):
	if not os.path.exists(f):
		Auto_LZ_ip = []
		username = input("输入用户名：例如 ************\n")
		Auto_LZ_ip.append(username)
		password= input("输入密码：\n")
		Auto_LZ_ip.append(password)
		Veh = input("输入车辆的编码：例如 MP2-592\n")
		Auto_LZ_ip.append(Veh)
		start_date = input("输入分析的起始日期：例如 5.1\n")
		Auto_LZ_ip.append(start_date)
		end_date = input("输入分析的终止日期：例如 5.3（注意：暂时不支持跨月份分析噢）\n")
		Auto_LZ_ip.append(end_date)
		key_words = input("输入数据的检索条件：例如 ACC自动退出|Pilot退出\n")
		Auto_LZ_ip.append(key_words)
		Zep_Address = input("输入用于分析的Zeppelin地址：\n")
		Auto_LZ_ip.append(Zep_Address)
		Fun = input("输入分析数据的功能分类：例如 Pilot-Lat\n")
		Auto_LZ_ip.append(Fun)
		Skip = input("是否要跳过其它人已经分析过的Tag： Yes/No\n")
		Auto_LZ_ip.append(Skip)
		vin = '{"MP2-xxx":"LJ1EEAUU1J7700xxx"}'
		Auto_LZ_ip.append(vin)
		with open(os.getcwd() + '/Auto_LZ.txt', 'w') as f:
			f.writelines(x + '\n' for x in Auto_LZ_ip)
	else:
		with open(os.getcwd() + '/Auto_LZ.txt', 'r') as f:
			Auto_LZ_f = f.readlines()		
			Auto_LZ_info = [x.strip() for x in Auto_LZ_f]
			vin = '{"MP2-xxx":"LJ1EEAUU1J7700xxx"}'
			Auto_LZ_info.append(vin)
	return Auto_LZ_info

def Login_Luna(browser, username, password):
	browser.implicitly_wait(30)
	browser.get('http://########.com')
	time.sleep(3)

	browser.implicitly_wait(30)
	username = browser.find_element_by_id('phone').send_keys('{}'.format(username))
	password = browser.find_element_by_id('pwd').send_keys('{}'.format(password))
	wait = WebDriverWait(browser, 10)
	button_Login = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
	browser.execute_script("arguments[0].click();", button_Login)
	time.sleep(3)

	#add token
	token=browser.execute_script('return window.localStorage.getItem("vue-auth-token")')
	js='window.localStorage.setItem("vue-auth-token", "{0}")'.format(token)
	browser.execute_script(js)
	time.sleep(1)

def Set_Conditions(browser, start_date, end_date, Veh):
	browser.implicitly_wait(30)
	browser.get('http://luna.nioint.com/#/analyze')
	time.sleep(3)

	browser.implicitly_wait(30)
	button_veh = browser.find_element_by_xpath('//li[contains(text(), "%s")]' % Veh)
	browser.execute_script("arguments[0].click();", button_veh)
	time.sleep(3)

	browser.implicitly_wait(30)
	button_cal = browser.find_element_by_xpath('//i[contains(@class,"ivu-icon-ios-calendar-outline")]/../input')
	browser.execute_script("arguments[0].click();", button_cal)
	time.sleep(1)

	browser.implicitly_wait(10)
	Months_Left_P = browser.find_element_by_xpath('//div[contains(@class,"ivu-picker-panel-content-left")]/div[@class="ivu-date-picker-header"]/span[3]/span[2]')
	Months_Left = Months_Left_P.text[0]
	Months_Left_int = int(Months_Left)
	Months_start = int(start_date.split('.')[0])
	Days_start = int(start_date.split('.')[1])
	Months_end = int(end_date.split('.')[0])
	Days_end = int(end_date.split('.')[1])
	Months_dif = Months_start - Months_Left_int
	Months_date_dif = Months_end-Months_start

	if Months_dif == 0:
		pass

	elif Months_dif < 0:
		while Months_dif != 0:
			browser.implicitly_wait(10)
			Button_Months_Pre = browser.find_element_by_xpath('//div[contains(@class,"ivu-picker-panel-content-left")]/div[@class="ivu-date-picker-header"]/span[2]/i')
			browser.execute_script("arguments[0].click();", Button_Months_Pre)
			Months_dif += 1
			time.sleep(0.5)

	elif Months_dif > 0:
		while Months_dif != 0:
			browser.implicitly_wait(10)
			Button_Months_Next = browser.find_element_by_xpath('//div[contains(@class,"ivu-picker-panel-content-right")]/div[@class="ivu-date-picker-header"]/span[3]/i')
			browser.execute_script("arguments[0].click();", Button_Months_Next)
			Months_dif -= 1
			time.sleep(0.5)

	if Months_date_dif == 0:
		Months_calendar = 'ivu-picker-panel-content-left'
	elif Months_date_dif == 1:
		Months_calendar = 'ivu-picker-panel-content-right'
	else:
		print("查询月份跨度太大，请缩小查询范围(两个月之内)")

	browser.implicitly_wait(10)
	button_start_date = browser.find_element_by_xpath('//div[contains(@class,"ivu-picker-panel-content-left")]//em[text()="%s"]' % Days_start)
	browser.execute_script("arguments[0].click();", button_start_date)
	button_end_date = browser.find_element_by_xpath('//div[contains(@class,"%s")]//em[text()="%s"]' % (Months_calendar, Days_end))
	browser.execute_script("arguments[0].click();", button_end_date)
	time.sleep(3)
	return

def Download_info(browser):
	tags = []
	comments = []
	try:
		browser.implicitly_wait(10)
		Tag_P = browser.find_element_by_xpath('//tbody[@class="ivu-table-tbody"]/tr' )

	except:
		return tags, comments

	else:
		browser.implicitly_wait(30)
		button_next_page = browser.find_element_by_xpath('//li[@title="下一页"]')
		while button_next_page.get_attribute('class') == 'ivu-page-next':
			browser.implicitly_wait(30)
			tag_elements = browser.find_elements_by_xpath('//tbody[1]/tr/td[3]/div')
			comment_elements = browser.find_elements_by_xpath('//tbody[1]/tr/td[9]//span')
			for i in range(len(tag_elements)):
				tags.append(tag_elements[i].text)
				comments.append(comment_elements[i].text)
			browser.execute_script("arguments[0].click();", button_next_page)
			time.sleep(3)
			browser.implicitly_wait(30)
			button_next_page = browser.find_element_by_xpath('//li[@title="下一页"]')

		tag_elements = browser.find_elements_by_xpath('//tbody[1]/tr/td[3]/div')
		comment_elements = browser.find_elements_by_xpath('//tbody[1]/tr/td[9]//span')
		for i in range(len(tag_elements)):
			tags.append(tag_elements[i].text)
			comments.append(comment_elements[i].text)
		return tags, comments

def DF_Zep_Result_list(df, address, vin, Veh):
	Tags_list = df.Tag_Number.tolist()
	Tags_list_f = [x[-15:] for x in Tags_list]
	Zep_Result = Get_Zeppelin_Results(vin, Veh, Tags_list_f, address)
	for i in range(len(Zep_Result)):
		df.iloc[i,2] = Zep_Result[i]
	return df

def Add_Analysis_Each_Page(browser, Numb, Content, Type, Skip):
	arr = list(range(0, 500, 20))
	browser.implicitly_wait(10)
	Button_Page = browser.find_element_by_xpath('//li[@title="上一页"]/../li[2]')
	browser.execute_script("arguments[0].click();", Button_Page)
	time.sleep(1)

	for i in range(1, len(arr)):
		if Numb <= arr[i]:
			Page = i
			Numb_Page = Numb - arr[i-1]
			break
		else:
			Button_Page = browser.find_element_by_xpath('//li[@title="上一页"]/../li[{}]'.format(i+2)) 
			browser.execute_script("arguments[0].click();", Button_Page)
			time.sleep(1)

	Add_Analysis(browser, Numb_Page, Content, Type, Skip)

def Add_Analysis(browser, Numb_Page, Content, Type, Skip):

	try:
		flag = True
		browser.implicitly_wait(10)
		Tag_P = browser.find_element_by_xpath('//tbody[1]/tr[%d]/td[3]/div' % Numb_Page)
		Tag_Num = Tag_P.text
		Text_analyze_P = browser.find_element_by_xpath('//tbody[@class="ivu-table-tbody"]/tr[%d]/td[12]//p' % Numb_Page)
	except:
		flag=False

	if flag==True and Skip=="Yes":
		print("Tag:{} 已经被其它小伙伴分析过了噢~".format(Tag_Num[:15]))
	else:
		browser.implicitly_wait(10)
		button_analyze = browser.find_element_by_xpath('//tbody[@class="ivu-table-tbody"]/tr[%d]//span[text()="analyze"]/..' % Numb_Page)
		browser.execute_script("arguments[0].click();", button_analyze)
		time.sleep(1)

		browser.implicitly_wait(10)
		button_fun = browser.find_element_by_xpath('//div[@class="ivu-form-item-content"]/div[1]/label[{}]'.format(Type))
		browser.execute_script("arguments[0].click();", button_fun)
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
		time.sleep(1)
		print("Tag:{} 分析结果已上传到Luna".format(Tag_Num))

def Auto_LZ_Main(info_list):
	global browser_luna, Zep_Sts, username, password, Veh, vin, Skip, G_File, Browser_V, Tag_Comment
	username = info_list[0]
	password = info_list[1]
	Veh = info_list[2]
	start_date = info_list[3]
	end_date = info_list[4]
	key_words1 = info_list[5]
	Zep_Address1 = info_list[6]
	Fun1 = info_list[7]
	key_words2 = info_list[8]
	Zep_Address2 = info_list[9]
	Fun2 = info_list[10]
	key_words3 = info_list[11]
	Zep_Address3 = info_list[12]
	Fun3 = info_list[13]

	key_words4 = info_list[14]
	Zep_Address4 = info_list[15]
	Fun4 = info_list[16]
	key_words5 = info_list[17]
	Zep_Address5 = info_list[18]
	Fun5 = info_list[19]
	key_words6 = info_list[20]
	Zep_Address6 = info_list[21]
	Fun6 = info_list[22]
	Skip = info_list[23]
	G_File = info_list[24]
	Browser_V = info_list[25]
	vin = info_list[-1]
	Zep_Sts = 0
	
	chrome_options = webdriver.ChromeOptions()
	if Browser_V=="False":
		chrome_options.add_argument('--headless')
	chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])
	browser_luna = webdriver.Chrome(chrome_options=chrome_options)
	
	print("\n正在登录 Luna")
	Login_Luna(browser_luna,username,password)
	Set_Conditions(browser_luna, start_date, end_date, Veh)
	print("努力检索中...")
	time.sleep(1)

	Tags, Comments = Download_info(browser_luna)
	if len(Tags)!=0:
		dic = {'Tag_Number':Tags, 'Comment':Comments}
		Tag_Comment = DataFrame(dic)
		Tag_Comment['Analysis'] = "NaN"

		Run_Script(key_words1, Fun1, Zep_Address1)
		Run_Script(key_words2, Fun2, Zep_Address2)
		Run_Script(key_words3, Fun3, Zep_Address3)
		Run_Script(key_words4, Fun4, Zep_Address4)
		Run_Script(key_words5, Fun5, Zep_Address5)
		Run_Script(key_words6, Fun6, Zep_Address6)

		# if len(key_words1)!=0:
		# 	DF_Filte1 = Tag_Comment[Tag_Comment['Comment'].str.contains("{}".format(key_words1), case=False)].copy()
		# 	if len(DF_Filte1)>=1: 
		# 		print("\n关于{0}功能，Auto_LZ帮您从Luna上查找到{1}个Tag".format(Fun1, len(DF_Filte1)))
		# 		if Zep_Sts == 0:
		# 			login_Zeppelin(username[:-8], password, Browser_V)
		# 			Zep_Sts = 1

		# 		DF_Filte_A = DF_Zep_Result_list(DF_Filte1, Zep_Address1, vin, Veh)
		# 		for i in list(DF_Filte_A.index):
		# 			Add_Analysis_Each_Page(browser_luna, i+1, DF_Filte_A['Analysis'][i], Fun_dict[Fun1], Skip)
		# 		if G_File == "True":
		# 			try:
		# 				Write_Excel("Tags_list.xls", DF_Filte_A)
		# 			except:
		# 				print("文件保存失败，请检查下文件Tags_list.xls当前是否处于打开状态")
		# 	else:
		# 		print("\nAuto_LZ没有找到关于{}功能的信息，换个检索条件试试呢，如果您检索了多个字符条件，在拼写“｜”时，注意要切换成英文输入法".format(Fun1))		


		# if len(key_words2)!=0:
		# 	DF_Filte2 = Tag_Comment[Tag_Comment['Comment'].str.contains("{}".format(key_words2), case=False)].copy()
		# 	if len(DF_Filte2)>=1: 
		# 		print("\n关于{0}功能，Auto_LZ帮您从Luna上查找到{1}个Tag".format(Fun2, len(DF_Filte2)))
		# 		if Zep_Sts == 0:
		# 			login_Zeppelin(username[:-8], password, Browser_V)
		# 			Zep_Sts = 1
		# 		DF_Filte_A = DF_Zep_Result_list(DF_Filte2, Zep_Address2, vin, Veh)
		# 		for i in list(DF_Filte_A.index):
		# 			Add_Analysis_Each_Page(browser_luna, i+1, DF_Filte_A['Analysis'][i], Fun_dict[Fun2], Skip)
		# 		if G_File == "True":
		# 			try:
		# 				Write_Excel("Tags_list.xls", DF_Filte_A)
		# 			except:
		# 				print("文件保存失败，请检查下文件Tags_list.xls当前是否处于打开状态")
		# 	else:
		# 		print("\nAuto_LZ没有找到关于{}功能的信息，换个检索条件试试呢，如果您检索了多个字符条件，在拼写“｜”时，注意要切换成英文输入法".format(Fun2))


		# if len(key_words3)!=0:
		# 	DF_Filte3 = Tag_Comment[Tag_Comment['Comment'].str.contains("{}".format(key_words3), case=False)].copy()
		# 	if len(DF_Filte3)>=1: 
		# 		print("\n关于{0}功能，Auto_LZ帮您从Luna上查找到{1}个Tag".format(Fun3, len(DF_Filte3)))
		# 		if Zep_Sts == 0:
		# 			login_Zeppelin(username[:-8], password, Browser_V)
		# 			Zep_Sts = 1
		# 		DF_Filte_A = DF_Zep_Result_list(DF_Filte3, Zep_Address3, vin, Veh)
		# 		for i in list(DF_Filte_A.index):
		# 			Add_Analysis_Each_Page(browser_luna, i+1, DF_Filte_A['Analysis'][i], Fun_dict[Fun3], Skip)
		# 		if G_File == "True":
		# 			try:
		# 				Write_Excel("Tags_list.xls", DF_Filte_A)
		# 			except:
		# 				print("文件保存失败，请检查下文件Tags_list.xls当前是否处于打开状态")
		# 	else:
		# 		print("\nAuto_LZ没有找到关于{}功能的信息，换个检索条件试试呢，如果您检索了多个字符条件，在拼写“｜”时，注意要切换成英文输入法".format(Fun3))

	else:
		print("\nLuna上暂时无数据！当天可能没有进行路测噢~")

	Browser_Close()


def Run_Script(key_words, Fun, Zep_Address):
	global browser_luna, Zep_Sts, username, password, Veh, vin, Skip, G_File, Browser_V, Tag_Comment
	if len(key_words)!=0:
		DF_Filte = Tag_Comment[Tag_Comment['Comment'].str.contains("{}".format(key_words), case=False)].copy()
		if len(DF_Filte)>=1: 
			print("\n关于{0}功能，Auto_LZ帮您从Luna上查找到{1}个Tag".format(Fun, len(DF_Filte)))
			if Zep_Sts == 0:
				login_Zeppelin(username[:-8], password, Browser_V)
				Zep_Sts = 1

			DF_Filte_A = DF_Zep_Result_list(DF_Filte, Zep_Address, vin, Veh)
			for i in list(DF_Filte_A.index):
				Add_Analysis_Each_Page(browser_luna, i+1, DF_Filte_A['Analysis'][i], Fun_dict[Fun], Skip)
			if G_File == "True":
				try:
					Write_Excel("Tags_list.xls", DF_Filte_A)
				except:
					print("文件保存失败，请检查下文件Tags_list.xls当前是否处于打开状态")
		else:
			print("\nAuto_LZ没有找到关于{}功能的信息，换个检索条件试试呢，如果您检索了多个字符条件，在拼写“｜”时，注意切换成英文输入法".format(Fun))	


def Write_Excel(f, DF):
	if os.path.exists(f):
		value = DF.values.tolist()
		index = len(value) #获取需要写入数据的行数
		workbook = xlrd.open_workbook(f) #打开工作簿
		sheets = workbook.sheet_names() #获取工作簿中的所有表格
		worksheet = workbook.sheet_by_name(sheets[0]) #获取工作簿中所有表格的第一个表格
		rows_old = worksheet.nrows #获取表格中已存在的数据的行数
		new_workbook = copy(workbook) #将xlrd对象拷贝转化为xlwt对象
		new_worksheet = new_workbook.get_sheet(0) #获取转化后工作簿第一个表格
		for i in range(0, index):
			for j in range(0, len(value[i])):
				new_worksheet.write(i+rows_old+1, j, value[i][j])
		new_workbook.save(f)
	else:
		writer = ExcelWriter(f)
		DF.to_excel(writer, index=False)
		writer.save()	
	print("分析结果已保存到 Tags_list.xls")


def Browser_Close():
	global browser_luna
	browser_luna.quit()
	Browser_zep_Close()


if __name__ == '__main__':

	Auto_LZ_info = CreatAuto_LZ_file("Auto_LZ.txt")
	Auto_LZ_Main(Auto_LZ_info)
