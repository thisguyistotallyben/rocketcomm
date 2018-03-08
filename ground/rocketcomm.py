# test.py
# Author:  Ben Johnson
# Purpose: Provide a temporary wrapper for townwizard and also test
#          View/MultiView function

import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *

from utils.multiview import MultiView
from views.rocket import Rocket

class RocketView(MultiView):
    def __init__(self):
        # variables
        super().__init__()
        self.title = 'Rocket Comms (Alpha)'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 600

        self.createMenuBar()
        self.createStatusBar()

        # init
        self.initUI()

        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # wrapper widget (holds everything)
        self.wrap = QWidget()

        # layout
        self.layout = QVBoxLayout()
        self.wrap.setLayout(self.layout)

        # rocket view
        self.rocket = Rocket(self)
        self.addView(self.rocket)

        # add the viewer and set
        self.layout.addWidget(self.getViewer())
        self.setCurrentView(self.rocket)

        # set central widget
        self.setCentralWidget(self.wrap)

if __name__ == '__main__':
    # QT IT UP
    app = QApplication(sys.argv)

    # initalize classes
    win = RocketView()

    # execute, clean up, and exit
    sys.exit(app.exec_())
