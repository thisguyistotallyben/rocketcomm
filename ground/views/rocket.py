import os, sys, glob
from serial.tools import list_ports
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *

from utils.multiview import View

class Rocket(View):
    def __init__(self, mvp):
        super().__init__(mvp)

        self.loadMenu('config/rocket-menu.json')

        self.recording = False

        # init
        self.initUI()

        self.portsig()

    def initUI(self):
        self.layout = QGridLayout()
        self.connlayout = QGridLayout()
        self.statuslayout = QVBoxLayout()
        self.datalayout = QVBoxLayout()
        self.setViewLayout(self.layout)

        self.widgets = {}
        self.widgets['datacase'] = QGroupBox('Data')
        self.widgets['data'] = QListWidget()
        self.widgets['start'] = QPushButton('Start')
        self.widgets['stop'] = QPushButton('Stop')
        self.widgets['save'] = QPushButton('Save')

        self.widgets['conn wrapper'] = QGroupBox('Connection Information')
        self.widgets['conn portlabel'] = QLabel('Port')
        self.widgets['conn refresh'] = QPushButton('Refresh')
        self.widgets['conn combo'] = QComboBox(self)
        self.widgets['conn connect'] = QPushButton('Connect')

        self.widgets['status wrapper'] = QGroupBox('Status')
        self.widgets['status send'] = QLabel('Sending')
        self.widgets['status receive'] = QLabel('Receiving')


        # setup connections section
        self.widgets['conn wrapper'].setLayout(self.connlayout)
        self.connlayout.addWidget(self.widgets['conn portlabel'], 0,0)
        self.connlayout.addWidget(self.widgets['conn refresh'], 0,1)
        self.connlayout.addWidget(self.widgets['conn combo'], 1,0, 1,2)
        self.connlayout.addWidget(self.widgets['conn connect'], 2,0, 1,2)
        self.connlayout.addWidget(self.widgets['status wrapper'], 4,0, 1,2)
        self.connlayout.setRowStretch(3,4)

        self.widgets['status wrapper'].setLayout(self.statuslayout)
        self.widgets['status send'].setDisabled(True)
        self.widgets['status receive'].setDisabled(True)
        self.statuslayout.addWidget(self.widgets['status send'])
        self.statuslayout.addWidget(self.widgets['status receive'])

        # set signals
        self.widgets['conn connect'].clicked.connect(self.buttsig)
        self.widgets['start'].clicked.connect(self.recsig)
        self.widgets['conn refresh'].clicked.connect(self.portsig)


        self.datalayout.addWidget(self.widgets['data'])
        self.widgets['datacase'].setLayout(self.datalayout)

        # add
        self.layout.addWidget(self.widgets['conn wrapper'], 0,0, 2,1)
        self.layout.addWidget(self.widgets['datacase'], 0,1, 1,3)
        self.layout.addWidget(self.widgets['start'], 1,1)
        self.layout.addWidget(self.widgets['stop'], 1,2)
        self.layout.addWidget(self.widgets['save'], 1,3)

        self.layout.setColumnStretch(0,1)
        self.layout.setColumnStretch(1,3)
        self.layout.setColumnStretch(2,3)
        self.layout.setColumnStretch(3,3)

    def buttsig(self):
        self.widgets['conn connect'].setText('Connected')
        self.widgets['conn connect'].setDisabled(True)

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
        # setup
        ports = list_ports.comports()
        self.widgets['conn combo'].clear()
        print('getting ports')
        for i in ports:
            self.widgets['conn combo'].addItem(i.name)
