
import os, sys, glob
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *

from utils.multiview import View

class Rocket(View):
    def __init__(self, mvp):
        super().__init__(mvp)

        self.loadMenu('config/rocket-menu.json')

        # init
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.datalayout = QVBoxLayout()
        self.setViewLayout(self.layout)

        self.widgets = {}
        self.widgets['datacase'] = QGroupBox('Data')
        self.widgets['data'] = QListWidget()
        self.widgets['connect'] = QPushButton('Connect to rocket')
        self.widgets['record'] = QPushButton('Start recording')

        # set signals
        self.widgets['connect'].clicked.connect(self.buttsig)
        self.widgets['record'].clicked.connect(self.recsig)

        self.datalayout.addWidget(self.widgets['data'])
        self.widgets['datacase'].setLayout(self.datalayout)

        # add
        self.layout.addWidget(self.widgets['connect'])
        self.layout.addWidget(self.widgets['record'])
        self.layout.addWidget(self.widgets['datacase'])

    def buttsig(self):
        self.widgets['connect'].setText('Connected')
        self.widgets['connect'].setDisabled(True)

    def recsig(self):
        if self.recording:
            self.recording = False
            # stop recording and do whatever
            self.widgets['record'].setText('Data recorded')
            self.widgets['record'].setDisabled(True)
            self.setStatus('Stopped')
        else:
            self.recording = True
            self.widgets['record'].setText('Stop recording')
            self.setStatus('Recording')

    def newsig(self):
        print('New signal goes here')

    def portsig(self):
        print('Port signal goes here')
