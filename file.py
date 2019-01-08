#!/usr/bin/python3
# -*- coding: UTF-8 -*-

fname = input("请输入要创建的文件：")
fo = open(fname, "w+")
line1 = "唐诗"
line2 = "宋诗"

fo.write('{}\n{}'.format(line1, line2))
fo.seek(0)
for line in fo:
	print(line, end='')
fo.close()