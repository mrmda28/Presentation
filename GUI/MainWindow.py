from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QMainWindow, QWidget, \
    QDesktopWidget, QMessageBox, QPushButton, QLineEdit
from GUI.StartWidget import Start


class MainWindow(QMainWindow):
    WINDOW_WIDTH = 900
    WINDOW_HEIGHT = 600

    WINDOW_TITLE = 'Presentation'

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(self.WINDOW_TITLE)
        # self.setWindowIcon(QtGui.QIcon('Data/Images/..'))
        # self.setStyleSheet('background: url(Data/Images/..);')
        # self.center_on_screen()
        self.update_widget(Start(self))
        self.show()

    def background(self, bg):
        if bg == 'start':
            self.setStyleSheet('background: url(Data/Images/bg.png) no-repeat center;')
            # self.setStyleSheet('background: white;')
        elif bg == 'description':
            # self.setStyleSheet('background: white;')
            self.setStyleSheet('background: url(Data/Images/bg2.png) no-repeat center;')
            # self.setStyleSheet('background: rgb(27,27,27);')
        elif bg == 'git':
            self.setStyleSheet('background: url(Data/Images/bg.png) no-repeat center;')
        elif bg == 'review':
            self.setStyleSheet('background: url(Data/Images/bg.png) no-repeat center;')
        else:
            self.setStyleSheet('background: white;')


    def update_widget(self, widget: QWidget, size_w: int = WINDOW_WIDTH, size_h: int = WINDOW_HEIGHT):
        self.setMinimumSize(size_w, size_h)
        # self.setFixedSize(size_w, size_h)
        self.setCentralWidget(widget)

    # def center_on_screen(self):
    #     qr = self.frameGeometry()
    #     cp = QDesktopWidget().availableGeometry().center()
    #     qr.moveCenter(cp)
    #     self.move(qr.topLeft())