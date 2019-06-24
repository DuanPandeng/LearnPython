#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import shutil
import subprocess
import readline
import time


Currentdir = os.getcwd()
readline.parse_and_bind("control-v: paste")

flag = 1
Counter = 36000

def scan_file():
	Download_files = []
	files = os.listdir()
	for f in files:
		if f.endswith('.gz'):
			Download_files.append(f)
	return Download_files

def unzip_it(f):
	folder_name = f.split('.')[0]
	target_path = './' + folder_name
	os.makedirs(target_path)
	shutil.unpack_archive(f, target_path)

def delete_file(f):
	os.remove(f)

def creatdir_file(f):
	if not os.path.exists(f):
		Dir_ip = []
		Dir_downloads_ip = input("输入压缩文件所在地址：例如（C:\\Users\\dpd\\Downloads）\n")
		Dir_ip.append(Dir_downloads_ip)
		Dir_Mapping_ip = input("输入Mapping文件地址：例如（D:\\NIO_Project\\pilot.txt）\n")
		Dir_ip.append(Dir_Mapping_ip)
		Dir_DataConverter_ip = input("输入DataConverter.exe地址：例如（D:\\NIO_Project\\DataConverter.exe）\n")
		Dir_ip.append(Dir_DataConverter_ip)
		Dir_package_ip = input("输入解压缩数据存放地址：例如（D:\\NIO_Project\\Data）\n")
		Dir_ip.append(Dir_package_ip)
		with open(Currentdir + '/dirs.txt', 'w') as f:
			f.writelines(x + '\n' for x in Dir_ip)
	with open(Currentdir + '/dirs.txt', 'r') as f:
		dir_f = f.readlines()
	return dir_f


dir_f = creatdir_file("dirs.txt")
os.chdir(r"{}".format(dir_f[0][:-1]))
Mapping = r"{}".format(dir_f[1][:-1])
print("\n压缩文件所在地址：\n{}".format(dir_f[0][:-1]))
print("\nMapping文件地址：\n{}".format(dir_f[1][:-1]))
print("\nDataConverter.exe地址：\n{}".format(dir_f[2][:-1]))
print("\n解压缩数据存放地址：\n{}\n".format(dir_f[3][:-1]))

while Counter != 0:
	os.chdir(r"{}".format(dir_f[0][:-1]))
	Counter -= 1		
	zip_files = scan_file()
	if zip_files:
		flag = 1
		for zip_file in zip_files:
			os.chdir(r"{}".format(dir_f[0][:-1]))
			shutil.move('./' + zip_file, "{}".format(dir_f[3][:-1]))
			os.chdir(r"{}".format(dir_f[3][:-1]))
			print("数据解压中……")
			try:
				unzip_it(zip_file)
			except:
				print("{}数据解压报错，数据包可能不完整\n".format(zip_file[14:33]))
			finally:
				Eth_Path = './' + zip_file.split('.')[0]+ '/' + zip_file[18:33]
				Eth_file = Eth_Path + './eth_' + zip_file[18:33] + '.dat' 
				#print(Eth_Path)		
				try:
					subprocess.call('"%s" %s %s %s' % (dir_f[2][:-1],"Pandora_ETH=>MDF",Eth_file,Mapping))
				except:
					print("{}数据转化出错，检查下DataConverter地址正确； 若地址更新，请删除目录下dirs.txt文件\n".format(zip_file[14:33]))
					shutil.rmtree('./' + zip_file.split('.')[0])
					time.sleep(1)
				else:
					try:
						fexist = 0
						os.chdir(Eth_Path)
						files = os.listdir()
						os.chdir(r"{}".format(dir_f[3][:-1]))
						if not os.path.exists("./MDF"):
							os.makedirs("./MDF")
						for f in files:
							if f.endswith('.mdf'):
								fexist = 1
								shutil.copy(Eth_Path + '/' + f, './MDF')
							elif f.endswith('.mf4'):
								fexist = 1
								print('mf4')
								shutil.copy(Eth_Path + '/' + f, './MDF')
						if fexist==1:
							print("\n数据 {} generate mdf file sucessfully\n".format(zip_file[14:33]))
							shutil.copytree('./' + zip_file.split('.')[0] + '/' + zip_file[18:33], './' + zip_file[14:33])
							shutil.rmtree('./' + zip_file.split('.')[0])
							print("Good job, 数据 {} Convert Done!\n".format(zip_file[14:33]))
							delete_file(zip_file)
						else:
							print("{}mdf数据未生成，再看看DataConverter的设置？\n".format(zip_file[14:33]))
							shutil.rmtree('./' + zip_file.split('.')[0])					
							time.sleep(1)
					except:
						print("{}数据Copy出错，是不是文件已经存在？\n".format(zip_file[14:33]))
						shutil.rmtree('./' + zip_file.split('.')[0])
						time.sleep(1)
	else:
		if flag == 0:
			pass
			time.sleep(3)
		else:
			print("正在搜索解压文件……\n")
			flag = 0

os.chdir(Currentdir)