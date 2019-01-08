#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from asammdf import MDF, Signal
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

pd.options.display.max_rows = 10


file = 'ACC6.mdf'
signal = 'MeasList-AccMod_7C_CAN0'
gap = 3
start = 3

#read file and creat Seriers
mdf = MDF(file)
sig1_raw = mdf.get(signal)
sig1 = pd.Series(sig1_raw.samples)

#filte by change point
sig1_point_A=pd.Series(np.arange(len(sig1)))
for i in range(len(sig1)-1):
	sig1_point_A[i] = sig1[i+1]-sig1[i]

#filte by change point's step size 'gap'
sig1_point_G = sig1_point_A[(sig1_point_A == gap)].index.tolist()
sig1_point_G_counts = len(sig1_point_G)

#filte by previous value 'start'
sig1_point_1=[]
for i in range(len(sig1_point_G)):
	if sig1[sig1_point_G[i]]==start:
		sig1_point_1.append(sig1_point_G[i]) 

sig1_point_1_counts = len(sig1_point_1)


#write to file
writer = pd.ExcelWriter('mdf1.xlsx')
sig1_point = Series(sig1_point_1)
sig1_point.to_excel(writer, startcol=1, startrow=1, header=False, index=False)
writer.save()
