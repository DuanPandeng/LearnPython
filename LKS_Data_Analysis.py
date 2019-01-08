#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
from asammdf import MDF, Signal
from pandas import Series, DataFrame
from datetime import datetime
from datetime import timedelta
import pandas as pd
import numpy as np

pd.options.display.max_rows = 10


file = sys.argv[1]
tag = sys.argv[2]
signal1 = 'MeasList-LatCtrl_stLKSSts_mp'
signal2 = 'MeasList-LatCtrl_bfLksSprs_mp'

Spr = {1:'NoLineDetected', 2:'AgofVehToLaOfflim', 4:'LaWdthOfflim', 8:'LaCurvOfflim', 
		16:'LatAccOffLim', 32:'LatSpdOfflim', 64:'DispSpdOfflim', 128:'LongAccOfflim',
		256:'YawRateOfflim', 512:'ActrNotAvl', 1024:'Handsoff', 2048:'TurnIdctrOn',
		4096:'RwrdGear', 8192:'HPPLowConf', 16384:'LineIntersect'}


mdf = MDF(file+'.mf4')
sig1_raw = mdf.get(signal1)
sig1 = pd.Series(sig1_raw.samples)
sig2_raw = mdf.get(signal2)
sig2 = pd.Series(sig2_raw.samples)

starttime = datetime.strptime(file[-15:], '%Y%m%dT%H%M%S')
tagtime = datetime.strptime(tag,'%Y%m%dT%H%M%S')
diftime = tagtime - starttime
tagseconds = diftime.seconds
print("\n起始时间：{}\nTag时间：{}".format(starttime,tagtime))


t3occurtime = []
t3seconds = []
t3Spr = []
t1occurtime = []
t1seconds = []

for i in range(len(sig1)-1):
 	if int(sig1[i])==2 and int(sig1[i+1])==3:
 	    t3seconds.append(i//20)
 	    t3occurtime.append(starttime + timedelta(0, t3seconds[-1]))
 	    t3Spr.append(Spr[sig2[i+1]])

 	elif int(sig1[i])==2 and int(sig1[i+1])==1:
 		t1seconds.append(i//20)


t3Series = pd.Series(t3Spr, index=t3occurtime)
t3Issue = t3Series.truncate(after=tagtime)

if len(t3Issue)>0:
	print("{}---{}".format(t3Issue.index[-1].strftime('%H:%M:%S'),t3Issue[-1]))


t1Series = pd.Series(t1seconds)
t1Issue = t1Series[t1Series.values<tagseconds].values

if len(t1Issue)>0:
	t1occurtime.append(starttime + timedelta(0, int(t1Issue[-1])))
	point = t1occurtime[-1].strftime('%H:%M:%S')
	print("{}---QUIT without TakeOver Warning".format(point))




#m, s = divmod(seconds, 60)