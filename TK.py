#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter as tk
import tkinter.messagebox as messagebox

# 主窗口
win = tk.Tk()
win.title("My Window")
win.geometry('600x300') # 窗口尺寸
win.resizable(width=False, height=True)

# 标签
var = tk.StringVar()
l1 = tk.Label(win, textvariable=var, anchor=tk.NE, fg="red", bg='green', font=('Arial',12), width=10, height=1)
l1.pack(side = 'left')
l2 = tk.Label(win, anchor=tk.NW, fg="black", bg='blue', font=('Arial',12), text="hellopython", width=10, height=1)
l2.pack(side = 'top')
l3 = tk.Label(win, bg = 'yellow', width=20, text='empty')
l3.pack()

# 按键的响应事件
def clickout():
	print("OK")

on_hit = False
def hit_me():
	global on_hit
	if on_hit == False:
		on_hit = True
		var.set('you hit me')
	else:
		on_hit = False
		var.set('')

def insert_point():
	var = e.get()
	t.insert('insert', var)

def insert_end():
	var = e.get()
	t.insert('end', var)

def print_selection(v):
	l3.config(text = 'You have selected' + v)

def print_selection_1():
	if(var1.get()==1) & (var2.get()==0):
		l3.config(text='I only love python3')
	elif(var1.get()==0) & (var2.get()==1):
		l3.config(text='I only love C++')
	elif(var1.get()==1) & (var2.get()==1):
		l3.config(text='I love both')
	else:
		l3.config(text='I do not love either')


def moveit():
	canvas.move(rect, 0, 2)

def do_job():
	global counter
	l3.config(text='do'+str(conter))
	conter+=1

def mb():
	#tk.messagebox.showinfo(title='Hi', message='hahaha')
	#tk.messagebox.showwarning(title='Hi', message='nonono')
	#tk.messagebox.showerror(title='Hi', message='NO! Never')
	print(tk.messagebox.askokcancel(title='Hi', message='hahaha'))
	
# 按键
b1 = tk.Button(win, anchor=tk.N, text="hit me", command=hit_me,width=10,height=1)
b1.pack(side = 'bottom')

b2 = tk.Button(win, text='inset point', width=10, height=1, command=insert_point)
b2.pack()

b3 = tk.Button(win, text='insert end', width=10, height=1, command=insert_end)
b3.pack()

b4 = tk.Button(win, text='move', command=moveit).pack()

b5 = tk.Button(win, text='Mb', command=mb).pack()


# 文本框
t = tk.Text(win, height=2)
t.pack()

# 单行输入框
e = tk.Entry(win, show = None)
e.pack()

# Listbox
var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
lb = tk.Listbox(win, listvariable = var2)
list_item = [1, 2, 3, 4]
for item in list_item:
	lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.pack()

# 单选按钮
r1 = tk.Radiobutton(win, text = 'Option A', variable = var, value = 'A', command = print_selection)
r1.pack()
r2 = tk.Radiobutton(win, text = 'Option B', variable = var, value = 'B', command = print_selection)
r2.pack( )

# scale
s = tk.Scale(win, label = 'try me', from_ = 5, to = 11, orient = tk.HORIZONTAL, length =200, showvalue=1, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

# 多选框
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(win, text='python', variable=var1, onvalue=1, offvalue=0, command=print_selection_1)
c2 = tk.Checkbutton(win, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection_1)
c1.pack()
c2.pack()

# 插入图片
canvas = tk.Canvas(win, bg='blue', height=150, width=200)
image_file=tk.PhotoImage(file="birdnest.png")
image = canvas.create_image(10,10,anchor='nw',image=image_file)
x0, y0, x1, y1 = 90, 90, 120, 120
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='yellow')
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)
canvas.pack()

#Menu
menubar = tk.Menu(win)
filemenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='file', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Save', command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label = 'import', menu=submenu, underline=0)
submenu.add_command(label='submenu1', command=do_job)

win.config(menu=menubar)

# Messagebox


# 主事件循环
win.mainloop()