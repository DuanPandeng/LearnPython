#!/usr/bin/python3
# -*- coding: UTF-8 -*-

fo = open("price2016_.csv", "r")
ls = []
for line in fo:
	line = line.replace("\n","")
	print(line)
	ls = line.split(",")
	print(ls)
fo.close()