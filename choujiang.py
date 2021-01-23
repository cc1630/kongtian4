# -*- coding: UTF-8 -*-
import random
import ctypes
import time
import sys
import os
from xml.dom.minidom import parse
import datetime
import shutil
from cv2 import cv2
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
 
picture_list = []
path = ''
end_pic = 'end_pic'
pictures = 'pictures'
luck_num = 1 #抽出几张图片 最好数量远小于抽奖池
 
 
def build_path(args) :
	end_path = os.getcwd()
	for arg in args :
		end_path = end_path + '\\' + arg
	return end_path
 
def init_pic() :
	end_path = build_path([path])
	g = os.walk(end_path)
	for _,_,filelist in g :
		for filename in filelist:
			if filename.endswith('jpg'):
				picture_list.append(filename)
	if picture_list :
		return True, end_path
	return False, None
 
#随机图片
def random_pic_index() :
	return picture_list[random.randint(0, len(picture_list)-1)]
 
#读XML配置
def read_xml() :
	doc = parse('./config.xml')
	root = doc.documentElement
	global path, random_time
	path = root.getElementsByTagName('path')[0].firstChild.data
	end_pic = root.getElementsByTagName('end_pic')[0].firstChild.data
 
#清空目标文件夹
def clear_end_pic() :
	path = os.getcwd() + '\\' + end_pic
	#print ('======%s' %str(path))
	for file in os.listdir(path) :
		file_data = path + '\\' + file
		if os.path.isfile(file_data) :
			#print(file_data)
			os.remove(file_data)
 
def run() :
	read_xml()
	flag, end_path = init_pic()
	if not flag or not end_path :
		print('Init error, not have pictures(filename with .jpg)')
		exit (1)
	clear_end_pic()
	#给随机数一个种子
	random.seed(int(time.time()))
	luck_filenames = []
	#可能会有重复的 多跑十次，还有重复就算了
	for i in range(0, luck_num+10) :
		for j in range(50):
			filename = random_pic_index()
			img = cv2.imread(os.getcwd()+'\\'+pictures+'\\'+filename)
			cv2.namedWindow("process", cv2.WINDOW_NORMAL)
			cv2.moveWindow("process", 600,200)
			cv2.imshow("process", img)
			cv2.waitKey(50)
		if filename in luck_filenames :
			continue
		luck_filenames.append(filename)
		print('%s  picture: %s' %(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), filename))
		#拷贝文件
		shutil.copyfile(end_path+'\\'+filename, os.getcwd()+'\\'+end_pic+'\\'+filename)
		img = cv2.imread(os.getcwd()+'\\'+end_pic+'\\'+filename)
		img = cv2.resize(img, (150, 100))
		cv2.namedWindow("result", cv2.WINDOW_NORMAL)
		cv2.moveWindow("result", 500,150)
		cv2.imshow("result", img)
		cv2.waitKey()
		cv2.destroyAllWindows()
		if len(luck_filenames) >= luck_num :
			break
	input('Please enter and then exit!!!')

class Example(QMainWindow) :
    
	def __init__(self) :
		super().__init__()
	
		self.initUI()
	def initUI(self):      
		#1 systools 安装环境
		btn1 = QPushButton("开始", self)
		btn1.move(80, 50)
		btn1.resize(150, 50)
		btn1.clicked.connect(self.button1Clicked)  
		#2 build 安装SDK
		# btn2 = QPushButton("2暂停", self)
		# btn2.move(50, 150)
		# btn2.resize(200, 30)
		# btn2.clicked.connect(self.button2Clicked)

		self.statusBar()
		self.setGeometry(200, 300, 300, 300)
		self.setWindowTitle('抽奖APP-V1.01')
		self.show()

	#按钮1事件
	def button1Clicked(self):
		run()
		# os.system('ls')#命令行
		# #os.system('cd /home')
		# os.system('./systools')
		# sender = self.sender()
		# self.statusBar().showMessage(sender.text() + ' was pressed')
	#按钮2事件
	def button2Clicked(self):
		# os.system('ls')#命令行
		# #os.system('cd /home')
		# os.system('./build')
		# sender = self.sender()
		# self.statusBar().showMessage(sender.text() + ' was pressed')
		print() 

if __name__ == '__main__':
    
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())