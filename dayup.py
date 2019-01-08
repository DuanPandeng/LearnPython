#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import math

days = 1+(365//7*4+365%7)*0.001
print(days)

def dayUP(Ni):
	dayup = 1.0
	for i in range (365):
		if i % 7 in [3, 1, 6]:
			dayup = dayup
		else:
			dayup = math.fsum([dayup,Ni])
	return dayup

Ni = 0.001

print("N 值为{:.3f}时，一周工作4天，一年后的年终值为：{:.4f}".format(Ni, dayUP(Ni)))