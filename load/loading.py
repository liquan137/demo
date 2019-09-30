# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import load.load

from PyQt5.QtGui import QMovie
from PyQt5 import QtCore, QtGui, QtWidgets

class Loading_win(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(103, 87)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(35, 20, 41, 51))
        self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap(":/loading/timg.gif"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gif = QMovie(":/loading/timg.gif")
        self.label.setMovie(self.gif)
        self.gif.start()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


