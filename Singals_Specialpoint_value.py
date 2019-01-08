#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from asammdf import MDF, Signal
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

pd.options.display.max_rows = 10



file = 'ACC6.mdf'
signal1 = 'MeasList-AccMod_7C_CAN0'
signal2 = 'MeasList-VehSpd_5B_CAN0'
gap = 3



mdf = MDF(file)
sig1_raw = mdf.get(signal1)
sig1 = pd.Series(sig1_raw.samples)
sig2_raw = mdf.get(signal2)
sig2 = pd.Series(sig2_raw.samples)


sig1_point=pd.Series(np.arange(len(sig1)))
for i in range(len(sig1)-1):
	sig1_point[i] = sig1[i+1]-sig1[i]


sig1_point_1 = sig1_point[(sig1_point == gap)].index.tolist()
sig1_point_1_counts = len(sig1_point_1)

#sig1_point_1_index = sig1_point_1[0]
#sig2_value = sig2[sig1_point_1_index]

sig2_filter = sig2.iloc[sig1_point_1]
sig2_filter_values = list(sig2_filter.values)

for i in range(len(sig1_point_1))