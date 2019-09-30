import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QRect, pyqtSignal, QThread
from PyQt5.QtGui import QCursor, QColor, QPainter, QBrush, QPainterPath, QPainter, QBrush, QColor, QPen
from login.login import *
from login.status import *
from load.loading import *
from load.other import *
import time
import math
from dateutil.parser import parse


class MyWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.mPos = None
        self.setupUi(self)
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(16)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.shadow.setOffset(-1, 3)
        self.pushButtonLogin.setGraphicsEffect(self.shadow)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        # effect = QGraphicsDropShadowEffect(self)
        # effect.setBlurRadius(12)
        # effect.setOffset(0, 0)
        # effect.setColor(Qt.gray)
        # self.setGraphicsEffect(effect)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def paintEvent(self, event):
        path = QtGui.QPainterPath()
        path.setFillRule(QtCore.Qt.WindingFill)
        path.addRect(20, 20, self.width() - 40, self.height() - 40)
        painter = QtGui.QPainter(self)
        painter.setPen(Qt.white)
        painter.setBrush(Qt.white)
        painter.setRenderHint(painter.Antialiasing, True)
        painter.drawRoundedRect(10, 10, self.width() - 20, self.height() - 20, 8, 8)
        painter.drawPath(path)
        painter.fillPath(path, QtGui.QBrush(QtCore.Qt.white))
        color = QtGui.QColor(60, 60, 60, 30)
        for i in range(0, 10):
            path = QtGui.QPainterPath()
            path.setFillRule(QtCore.Qt.WindingFill)
            painter.setRenderHint(painter.Antialiasing, True)
            painter.setBrush(Qt.transparent)
            painter.drawRoundedRect(10 - i, 10 - i, self.width() - (10 - i) * 2, self.height() - (10 - i) * 2, 8, 8)
            color.setAlpha(150 - math.sqrt(i) * 60)
            painter.setPen(color)
            painter.drawPath(path)


class Status(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Status, self).__init__(parent)
        self.setupUi(self)


class Load(QDialog, Loading_win):
    def __init__(self, parent=None):
        super(Load, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setupUi(self)


class waitExit(QThread):
    _signal = pyqtSignal(int)

    def __init__(self):
        super(waitExit, self).__init__()
        self.loading = Load()
        self.loading.show()
        self.status = True

    def __del__(self):
        self.status = False
        self.wait()

    def run(self):
        self.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        while self.status:
            Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            a = parse(Time)
            b = parse(self.time)
            print(int((a - b).total_seconds()))
            if int((a - b).total_seconds()) == 2:
                self.loading.close()
                self.status = False


class Login():
    def __init__(self):
        self.waitExit = waitExit()
        self.waitExit.start()
        self.test = QThread()
        self.style = """
                       #user{
                           border:none;border-bottom: 1px solid #aaa;font-size:14px;font-family: 微软雅黑;
                       }
                       #password{
                           border:none;border-bottom: 1px solid #aaa;font-size:14px;font-family: 微软雅黑;
                       }
                       #pushButtonLogin{
                           color:white;
                           background:#40b6ff;
                           font-size:18px;
                           box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:14px;border-radius: 4px;font-family: 微软雅黑;
                       }
                       #user:hover{
                           border-bottom: 2px solid #4d8ffd!important;
                           color:#4d8ffd
                       }
                       #password:hover{
                           border-bottom: 2px solid #4d8ffd!important;
                           color:#4d8ffd
                       }

                       #pushButtonLogin:pressed{
                           border: 1px solid #174ea9!important;
                           background: #174ea9;
                       }
                       """
        self.login = MyWindow()

        self.login.show()
        self.login.setStyleSheet(self.style)
        self.login.pushButtonLogin.clicked.connect(self.submit)
        self.test.start()

    def user_focus_in(self):
        self.login.user.setStyleSheet('border-bottom: 1px solid #4d8ffd;')

    def submit(self):
        print(self.login.user.text(), self.login.password.text())
        if self.login.user.text() == 'admin' and self.login.password.text() == 'admin':
            self.ui = Status()
            self.ui.show()
            self.ui.label.setText("状态： 登录成功")
        else:
            self.ui = Status()
            self.ui.show()
            self.ui.label.setText("状态： 登录失败")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login()
    sys.exit(app.exec_())
