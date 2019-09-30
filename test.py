import time

from PyQt5.QtCore import QObject, pyqtSignal, QThread

from PyQt5.QtWidgets import QProgressBar, QApplication, QPushButton, QDialog, QGridLayout


class TestWorker1(QThread):
    _signal = pyqtSignal(int)

    def __init__(self):
        super(TestWorker1, self).__init__()

    def run(self):
        for i in range(101):
            print(i)
            self._signal.emit(i)
            time.sleep(0.01)


class TestWorker2(QObject):
    _signal = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self):
        super(TestWorker2, self).__init__()

    def run(self):
        for i in range(101):
            print(i)
            self._signal.emit(i)
            time.sleep(0.01)
        self.finished.emit()


class ThreadDialog(QDialog):
    def __init__(self):
        super(ThreadDialog, self).__init__()

        self.grid_layout = QGridLayout(self)
        self.progress = QProgressBar(self)
        self.grid_layout.addWidget(self.progress, 0, 0, 1, 2)
        self.pushbutton1 = QPushButton('继承线程', self)
        self.grid_layout.addWidget(self.pushbutton1, 1, 0, 1, 1)
        self.pushbutton2 = QPushButton('movetothread', self)
        self.grid_layout.addWidget(self.pushbutton2, 1, 1, 1, 1)

        self.pushbutton1.clicked.connect(self.pushbutton1_clicked)
        self.pushbutton2.clicked.connect(self.pushbutton2_clicked)

    def pushbutton1_clicked(self):
        self.test_worker1 = TestWorker1()
        self.test_worker1._signal.connect(self.progress.setValue)
        self.test_worker1.start()

    def pushbutton2_clicked(self):
        self.test_worker2 = TestWorker2()
        self.test_thread2 = QThread()
        self.test_worker2.moveToThread(self.test_thread2)
        self.test_worker2._signal.connect(self.progress.setValue)
        self.test_worker2.finished.connect(self.test_worker2_finished)
        self.test_thread2.started.connect(self.test_worker2.run)
        self.test_thread2.start()

    def test_worker2_finished(self):
        self.test_thread2.quit()
        self.test_thread2.wait()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    thread_dialog = ThreadDialog()
    thread_dialog.show()
    app.exec_()
