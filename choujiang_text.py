# -*- coding: UTF-8 -*-
import random
import asyncio
#import ctypes
import time
import sys
import os
import threading
from xml.dom.minidom import parse
import datetime
import shutil
from cv2 import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

end = False
data = ['张三', '李四', '王五', '李雷', '韩梅梅']


def start(self):
    '''
    开始抽奖
    '''
    random.seed(int(time.time()))
    global end
    end = False
    self.widget_Win = WidgetWindow()
    self.widget_Win.show()
    while (not end):
        self.widget_Win.setText(data[random.randint(0, len(data) - 1)])
        QApplication.processEvents()


class WidgetWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        #self.label.setFont(QFont("Roman times", 70, QFont.AnyStyle))
        self.label.setFont(QFont("Microsoft YaHei", 70, QFont.AnyStyle))
        self.label.setGeometry(480, 230, 480, 230)
        self.label.move(0, 0)
        self.setWindowTitle('抽奖中...')
        self.resize(480, 230)

    def setText(self, text):
        self.label.setText(text)
        self.label.repaint()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        '''
        界面初始化
        '''
        #1 开始按钮
        btn1 = QPushButton("开始", self)
        btn1.move(80, 50)
        btn1.resize(150, 50)
        btn1.clicked.connect(self.startButtonClicked)
        #2 暂停按钮
        btn2 = QPushButton("暂停", self)
        btn2.move(80, 150)
        btn2.resize(150, 50)
        btn2.clicked.connect(self.endButtonClicked)

        self.statusBar()
        self.setGeometry(200, 300, 300, 300)
        self.setWindowTitle('抽奖APP-V0.01')
        self.show()

    #按钮1事件
    def startButtonClicked(self):
        start(self)

    #按钮2事件
    def endButtonClicked(self):
        global end
        end = True


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
