#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

from asammdf import MDF, signal
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np


file = 'ACC6.mdf'
signal = 'MeasList-AccMod_7C_CAN0'
gap = 3
start = 3

#read file and creat SeriersS
mdf = MDF(file)
sig_raw = mdf.get(signal)
sig1 = pd.Series(sig_raw.samples)
plt.plot(sig1)
plt.show()
