#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import json
import pandas as pd 
from pandas import DataFrame

data = pd.read_csv('curve.txt', sep='\s+', header=None, names=['Lon', 'Lat', 'Curvature', 'Heading', 'Slope', 'ID', 'Len', 'Lane_num', 'Min_Spd','Max_Spd', 'Tunnel', 'Bridge', 'Toll_booth', 'Tool'])

data_zoom = data[::10]

df_pd = data_zoom[['Lon', 'Lat', 'Curvature', 'Heading', 'Max_Spd']]

df_pd['Radius']=1/df_pd['Curvature']

df_pd['Direction'] = 1

for i in range(0, len(data)-10, 10):
    if df_pd['Heading'][i+10] >= df_pd['Heading'][i]:
        df_pd['Direction'][i] = "right"
    else:
        df_pd['Direction'][i] = "left"


Ra_list_20 = [0, 15, 25, 50, 75, 100]
Ra_list_30 = [0, 30, 50, 75, 100, 125, 150, 175, 200]
Ra_list_40 = [0, 60, 75, 100, 125, 150, 175, 200, 225, 250]
Ra_list_60 = [0, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400]
Ra_list_80 = [0, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
Ra_list_100 = [0, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
Ra_list_120 = [0, 650, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200]
Ra_list_130 = [0, 750, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300]


period = 2
gap = 10
index_spd = 1
index_rad = 1
index_dir = ""

dict_20_r = {}
dict_30_r = {}
dict_40_r = {}
dict_60_r = {}
dict_80_r = {}
dict_100_r = {}
dict_120_r = {}
dict_130_r = {}
dict_20_l = {}
dict_30_l = {}
dict_40_l = {}
dict_60_l = {}
dict_80_l = {}
dict_100_l = {}
dict_120_l = {}
dict_130_l = {}
dict_left= {}
dict_right= {}
dict_full = {}


def Creat_list(Ra_list, dict_spd):
    for j in range(len(Ra_list)-1):
        dict_spd['{}'.format(Ra_list[j+1])] = []


def Dict_Spd_Loc(DF, Ra_list, dict_spd_r, dict_spd_l, period, i):
    global index_spd, index_rad, index_dir
    #print(Ra_list)
    for j in range(len(Ra_list)-1):
        if all(DF['Radius'][i:i+period]>=Ra_list[j]) and all(DF['Radius'][i:i+period] < Ra_list[j+1]):
            location = [DF['Lon'][i*10],DF['Lat'][i*10]]
            if DF['Direction'][i*10] == "right":
                if Ra_list == index_spd and Ra_list[j+1]==index_rad and index_dir == "right":
                    pass
                else:
                    dict_spd_r['{}'.format(Ra_list[j+1])].append(location)
                    index_spd = Ra_list
                    index_rad = Ra_list[j+1]
                    index_dir = "right"

            else:
                if Ra_list == index_spd and Ra_list[j+1]==index_rad and index_dir == "left":
                    pass
                else:           
                    dict_spd_l['{}'.format(Ra_list[j+1])].append(location)
                    index_spd = Ra_list
                    index_rad = Ra_list[j+1]
                    index_dir = "left"


Creat_list(Ra_list_20, dict_20_r)
Creat_list(Ra_list_30, dict_30_r)
Creat_list(Ra_list_40, dict_40_r)
Creat_list(Ra_list_60, dict_60_r)
Creat_list(Ra_list_80, dict_80_r)
Creat_list(Ra_list_100, dict_100_r)
Creat_list(Ra_list_120, dict_120_r)
Creat_list(Ra_list_130, dict_130_r)
Creat_list(Ra_list_20, dict_20_l)
Creat_list(Ra_list_30, dict_30_l)
Creat_list(Ra_list_40, dict_40_l)
Creat_list(Ra_list_60, dict_60_l)
Creat_list(Ra_list_80, dict_80_l)
Creat_list(Ra_list_100, dict_100_l)
Creat_list(Ra_list_120, dict_120_l)
Creat_list(Ra_list_130, dict_130_l)


for i in range(0, len(df_pd)-10, gap):

    if all(df_pd['Max_Spd'][i:i+period] <= 20):
        Dict_Spd_Loc(df_pd, Ra_list_20, dict_20_r, dict_20_l, period, i)

    elif all(df_pd['Max_Spd'][i:i+period] <= 30) and all(20 < df_pd['Max_Spd'][i:i+period]):
        Dict_Spd_Loc(df_pd, Ra_list_30, dict_30_r, dict_30_l, period, i)   

    elif all(df_pd['Max_Spd'][i:i+period] <= 40) and all(30 < df_pd['Max_Spd'][i:i+period]):
        Dict_Spd_Loc(df_pd, Ra_list_40, dict_40_r, dict_40_l, period, i)  

    elif all(df_pd['Max_Spd'][i:i+period] <= 60) and all(40 < df_pd['Max_Spd'][i:i+period]):
        Dict_Spd_Loc(df_pd, Ra_list_60, dict_60_r, dict_60_l, period, i)  

    elif all(df_pd['Max_Spd'][i:i+period] <= 80) and all(60 < df_pd['Max_Spd'][i:i+period]):
        Dict_Spd_Loc(df_pd, Ra_list_80, dict_80_r, dict_80_l, period, i) 

    elif all(df_pd['Max_Spd'][i:i+period] <= 100) and all(80 < df_pd['Max_Spd'][i:i+period]):
        Dict_Spd_Loc(df_pd, Ra_list_100, dict_100_r, dict_100_l, period, i) 

    elif all(df_pd['Max_Spd'][i:i+period] <= 120) and all(100 < df_pd['Max_Spd'][i:i+period]):
        Dict_Spd_Loc(df_pd, Ra_list_120, dict_120_r, dict_120_l, period, i)   
                
    elif all(df_pd['Max_Spd'][i:i+period] <= 130) and all(120 < df_pd['Max_Spd'][i:i+period]):
        Dict_Spd_Loc(df_pd, Ra_list_130, dict_130_r, dict_130_l, period, i) 


dict_right["20"] = dict_20_r
dict_right["30"] = dict_30_r
dict_right["40"] = dict_40_r
dict_right["60"] = dict_60_r
dict_right["80"] = dict_80_r
dict_right["100"] = dict_100_r
dict_right["120"] = dict_120_r
dict_right["130"] = dict_130_r
dict_left["20"] = dict_20_l
dict_left["30"] = dict_30_l
dict_left["40"] = dict_40_l
dict_left["60"] = dict_60_l
dict_left["80"] = dict_80_l
dict_left["100"] = dict_100_l
dict_left["120"] = dict_120_l
dict_left["130"] = dict_130_l

dict_full["right"] = dict_right
dict_full["left"] = dict_left

#print(dict_full)

with open('HD_Map_SH.json', 'w') as f:
    json.dump(dict_full, f, indent=4)