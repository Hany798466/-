# 安装 pip 包
import os
from tkinter import *
from tkinter import messagebox

def getBao():
	pip = 'pip install %s -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com'%entry_bao.get()
	os.system(pip)

root = Tk()
root.title("pip包")
root.geometry("250x150+400+300")
url = StringVar()
url_lab1 = Label(text = "请输入包名:")
url_lab1.pack()
entry_bao = Entry(root,textvariable = url)
entry_bao.pack()
btn1 = Button(root,text = "提交",command = getBao,width = 8,height = 2)
btn1.pack()

root.mainloop()
