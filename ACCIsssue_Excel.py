#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime
from dateutil.parser import parse


pd.options.display.max_rows = 20


#import Excel file
xlsx = pd.ExcelFile('ACC Issues Summary.xlsx')
datawhole = pd.read_excel(xlsx,skiprows=[0,1])
datacolumn1 = pd.read_excel(xlsx, header=None, skiprows=[0], nrows=1)
datacolumn2 = pd.read_excel(xlsx, header=None, skiprows=[0,1], nrows=1)

column1_DF = datacolumn1.iloc[0,3:]
column1_DF.fillna(method='ffill', inplace=True)
column2_DF = datacolumn2.iloc[0,3:]

#取字符串
Index1_NM = datacolumn2.iloc[0,0]
Index2_NM = datacolumn2.iloc[0,1]


#设置列为行索引
datawhole[Index1_NM].fillna(method='ffill', inplace=True) 
Index1_DT = [parse(x) for x in datawhole[Index1_NM]]
index1 = list(Index1_DT)
index2 = list(datawhole[Index2_NM])

#设置二级列索引
column1 = list(column1_DF)
column2 = list(column2_DF)

#取Raw Data
data_R = datawhole.iloc[:,3:]


#数据类型转换-->float
def attempt_folat(x):
	try:
		return float(x)
	except ValueError:
		return 1

x = len(index1)
y = len(column2)
data_N = np.zeros((x,y))

for h in range(x):
	for l in range(y):
		if isinstance(data_R.iloc[h,l],(str)):
			data_R.iloc[h,l] = data_R.iloc[h,l][0]    #对字符串取第一个字母
		data_N[h][l] = attempt_folat(data_R.iloc[h,l])    #元素遍历数据类型转换


#生成新的DataFrame
data = pd.DataFrame(data_N, index=[index1,index2], columns=[column1,column2])
data.index.names =[Index1_NM, Index2_NM]
data.fillna(0, inplace=True)

#分箱
data_update = data[:datetime(2018,10,15)]
data_update1 = data[datetime(2018,10,16):]

diff = data_update.sum()-data_update1.sum()



