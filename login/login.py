# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(376, 463)
        Form.setWindowOpacity(1.0)
        Form.setAutoFillBackground(True)
        Form.setStyleSheet("")
        self.pushButtonLogin = QtWidgets.QPushButton(Form)
        self.pushButtonLogin.setGeometry(QtCore.QRect(50, 320, 271, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setStyleSheet("")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.user = QtWidgets.QLineEdit(Form)
        self.user.setGeometry(QtCore.QRect(60, 140, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        self.user.setFont(font)
        self.user.setStyleSheet("")
        self.user.setObjectName("user")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(60, 220, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        self.password.setFont(font)
        self.password.setStyleSheet("border:none;border-bottom: 1px solid #aaa;font-size:14px;font-family: 微软雅黑;transition: 0.3s;")
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font-size:24px;color:#4188fb;text-align:center;font-family: 微软雅黑;transition: 0.3s;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButtonLogin.setText(_translate("Form", "立即登录"))
        self.user.setPlaceholderText(_translate("Form", "请输入用户名"))
        self.password.setPlaceholderText(_translate("Form", "请输入密码"))
        self.label.setText(_translate("Form", "账号登录"))

