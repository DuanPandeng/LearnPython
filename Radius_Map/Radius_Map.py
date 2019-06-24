#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import json
import folium
import webbrowser


def Create_GeoJson_file_whole(Dict, spd_list, Dir):
	global flag_data

	Ra_list_20 = [0, 15, 25, 50, 75, 100]
	Ra_list_30 = [0, 30, 50, 75, 100, 125, 150, 175, 200]
	Ra_list_40 = [0, 60, 75, 100, 125, 150, 175, 200, 225, 250]
	Ra_list_60 = [0, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400]
	Ra_list_80 = [0, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
	Ra_list_100 = [0, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
	Ra_list_120 = [0, 650, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200]
	Ra_list_130 = [0, 750, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300]
	Spd_Ra_dict = {"20": Ra_list_20, "30": Ra_list_30, "40":Ra_list_40, "60":Ra_list_60, "80":Ra_list_80, "100":Ra_list_100, "120":Ra_list_120, "130":Ra_list_130}
	
	list_multpoint=[]
	for i in range(len(spd_list)):
		spd = spd_list[i]
		rad_list = Spd_Ra_dict[spd]
		for j in range(len(rad_list)-1):
			rad = rad_list[j+1]
			point_list_w=[]
			if Dir == "right":
				point_list_w=Dict['right'][spd][str(rad)]
			elif Dir == "left":
				point_list_w=Dict['left'][spd][str(rad)]
			elif Dir == "both":
				point_list_w_r=Dict['right'][spd][str(rad)]
				point_list_w_l=Dict['left'][spd][str(rad)]
				point_list_w = point_list_w_r + point_list_w_l
			else:
				print("abnormal")
			if len(point_list_w) >= 1:
				for h in point_list_w:
					lat = h[1]
					lon = h[0]
					dict_properties = dict(speed=spd, raduis=rad)
					dict_geometry = dict(type= "Point", coordinates= [lon,lat])
					dict_point = dict(type= "Feature", properties=dict_properties, geometry=dict_geometry)   
					list_multpoint.append(dict_point)	
	flag_data = len(list_multpoint)
	dict_object = dict(type= "FeatureCollection", features=list_multpoint)
	with open('Map_info.json', 'w') as f:
		json.dump(dict_object, f)


def Create_GeoJson_file_unit(Dict, spd, rad, Dir):
	global flag_data

	list_multpoint=[]
	point_list=[]
	if Dir == "right":
		point_list=Dict['right'][spd][str(rad)]
	elif Dir == "left":
		point_list=Dict['left'][spd][str(rad)]
	elif Dir == "both":
		point_list_r=Dict['right'][spd][str(rad)]
		point_list_l=Dict['left'][spd][str(rad)]
		point_list = point_list_r + point_list_l
	if len(point_list) > 0:
		for i in point_list:
			lat = i[1]
			lon = i[0]
			dict_properties = dict(speed=spd, raduis=rad)
			dict_geometry = dict(type= "Point", coordinates= [lon,lat])
			dict_point = dict(type= "Feature", properties=dict_properties, geometry=dict_geometry)   
			list_multpoint.append(dict_point)
		flag_data = len(list_multpoint)	
	else:
		flag_data = 0

	dict_object = dict(type= "FeatureCollection", features=list_multpoint)
	file_object = open('Map_info.json', 'w')
	json.dump(dict_object, file_object)
	

def Radius_Map_Main(file, whole, spd, rad, Dir):
	global flag_data

	Spd_list = ["20", "30", "40", "60", "80", "100", "120", "130"]

	if len(file) > 0: 
		#多点显示
		with open('{}'.format(file), 'r') as load_f:
			Map_dict = json.load(load_f)

		if whole:
			Create_GeoJson_file_whole(Map_dict, Spd_list, Dir)
		else:
			Create_GeoJson_file_unit(Map_dict, spd, rad, Dir)

		if flag_data != 0:
			print("{} Map Points Was Found".format(flag_data))		
			m = folium.Map(location=[31.284285, 121.47075], zoom_start=8, control_scale=True)
			Style_color = lambda x:{'fillColor':'#ff0080' if x['properties']["speed"]=="30" else '#8000ff'}
			ShangdaTooltip = folium.GeoJsonTooltip(fields=['speed','raduis'],style=('background-color:grey; color:white'))
			gj = folium.GeoJson('Map_info.json', style_function=Style_color, tooltip=ShangdaTooltip)
			gj.add_to(m)
			
			m.save('Radius_map.html')
			webbrowser.open('Radius_map.html')
		else:
			print("No Map Point Found")
	else:
		#单点显示
		print("单点显示，待开发")
		pass
	
if __name__ == '__main__':
	Radius_Map_Main(False, "30", "75")

