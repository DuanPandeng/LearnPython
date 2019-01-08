#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt 
import matplotlib




fr = open("price2016_.csv", "r")
fw = open("test.csv", "w+")

def GetData():	#将CSV文件的内容按每行一个列表，读到ls列表变量里
	ls = []
	print("读到的文件里的内容为：\n")
	for line in fr:		
		print(line, end='')
		line = line.replace("\n","")
		lsline = line.split(",")
		ls.append(lsline)
	return ls

def WriteData1():	#将一维数据写入csv
	# lsw = ['', '', '']
	fw.write(",".join(lsw) + "\n")

def WriteData2():	#将二维数据写入csv
	# lsw = [[],[]]
	for row in lsw:
		fw.write(",".join(row) + "\n")

lsw = [['1', '2', '3'], ['1', '2', '5']]
#lsw = GetData()
GetData()

if isinstance(lsw[0], list):
	 WriteData2()
else:
	 WriteData1()

fr.close()
fw.close()


# 坐标显示
for i in range(len(lsw)):
	for j in range(len(lsw[i])):
		lsw[i][j] = int(lsw[i][j])

def XY_Axis(x_start, x_end, y_start, y_end):
	plt.xlim(x_start, x_end)
	plt.ylim(y_start, y_end)


DrawDatax = lsw[0]
DrawDatay = lsw[1]
print(type(DrawDatay[0]))
print(DrawDatay)

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(DrawDatax, DrawDatay)
plt.title("坐标系标题")
plt.xlabel('时间（s）')
plt.ylabel('幅度（m）')
XY_Axis(0, 6, 0, 8)

plt.savefig('sample.PNG')
plt.show()