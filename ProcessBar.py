#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import time

scale = 50
t = time.clock()
n = 0.1


print("开始执行".center(scale//2, '-'))

for i in range(scale + 1):
	a, b = "*" * i, "." * (scale - i)
	c = (i/scale) * 100
	t = time.clock()
	print("\r{:>3.0f}%  [{}->{}]  {:.2f}s".format(c, a, b, t), end = '')
	n += 0.01
	time.sleep(n)

print("\n" + "结束执行".center(scale//2, '-'))