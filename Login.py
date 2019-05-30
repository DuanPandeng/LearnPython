#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pickle
import tkinter as tk
import tkinter.messagebox as messagebox
from PIL import Image

# 主窗口
win = tk.Tk()
win.title("Welcome to Python World")
win.geometry('450x300') # 窗口尺寸
win.resizable(width=False, height=False)

# welcome image
im = Image.open('welcome.gif')
om = im.resize((450,140))
om.save('welcomeRE.gif')

canvas = tk.Canvas(win, width=450, height=140)
image_file = tk.PhotoImage(file='welcomeRe.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(win, text='User name: ').place(x=50, y=150)
tk.Label(win, text='Password: ').place(x=50, y=190)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_user_name = tk.Entry(win, textvariable=var_usr_name)
entry_user_name.place (x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_user_pwd = tk.Entry(win, textvariable=var_usr_pwd, show='*')
entry_user_pwd.place(x=160, y=190)

def user_login():
	usr_name =var_usr_name.get()
	usr_pwd = var_usr_pwd.get()
	try:
		with open('usrs_info.pickle', 'rb') as usr_file:
			users_info = pickle.load(usr_file)
			print(users_info)
	except FileNotFoundError:
		with open('usrs_info.pickle', 'wb') as usr_file:
			users_info = {'admin':'admin'}
			pickle.dump(users_info, usr_file)
	if usr_name in users_info:
		if usr_pwd == users_info[usr_name]:
			tk.messagebox.showinfo(title='Welcome', message='How are you ?' + usr_name)
		else:
			tk.messagebox.showerror(message='Error, your password is wrong, try again please')
	else:
		is_sign_up = tk.messagebox.askyesno('Welcome', 'You have not sign up yet. Sign up Now ?')

		if is_sign_up:
			user_sign_up()

def user_sign_up():
	def sign_to_python():
		np = new_pwd.get()
		npf = new_pwd_confirm.get()
		nn = new_name.get()
		with open('usrs_info.pickle', 'rb') as usr_file:
			exist_usr_info = pickle.load(usr_file)
			print(exist_usr_info)
		if np != npf:
			tk.messagebox.showerror('Error', 'Password and Confirm password must be the same!')
		elif nn in exist_usr_info:
			tk.messagebox.showerror('Error', 'The user has already signed up!')
		else:
			exist_usr_info[nn] = np
			with open('usrs_info.pickle', 'wb') as usr_file:
				pickle.dump(exist_usr_info, usr_file)
			tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
		win_sign_up.destroy()

	# sign up window
	win_sign_up = tk.Toplevel(win)
	win_sign_up.title('Sign up window')
	win_sign_up.geometry('350x200')

	new_name = tk.StringVar()
	new_name.set('example@python.com')
	tk.Label(win_sign_up, text='User name: ').place(x=10, y=10)
	entry_new_name = tk.Entry(win_sign_up, textvariable=new_name)
	entry_new_name.place(x=150, y=10)

	new_pwd = tk.StringVar()
	tk.Label(win_sign_up, text='Password: ').place(x=10, y=50)
	entry_usr_pwd = tk.Entry(win_sign_up, textvariable=new_pwd, show='*')
	entry_usr_pwd.place(x=150, y=50)

	new_pwd_confirm = tk.StringVar()
	tk.Label(win_sign_up, text='Confirm password: ').place(x=10, y=90)
	entry_usr_pwd_confirm = tk.Entry(win_sign_up, textvariable=new_pwd_confirm, show='*')
	entry_usr_pwd_confirm.place(x=150, y=90)

	btn_confirm_sign_up = tk.Button(win_sign_up, text='Sign up', command=sign_to_python)
	btn_confirm_sign_up.place(x=150, y=130)

# login and sign up button
btn_login = tk.Button(win, text='Login', width=6, height=1, font=('Arial', 8), command=user_login)
btn_login.place(x=160, y=240)
btn_sign_up = tk.Button(win, text="sign up", width=6, height=1, font=('Arial', 8), command=user_sign_up)
btn_sign_up.place(x=260, y=240)



win.mainloop()
