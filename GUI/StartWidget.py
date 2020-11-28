from PyQt5.QtGui import QPixmap

from GUI.DescriptionWidget import Description
from GUI.MainWindow import *


class Start(QWidget):
    def __init__(self, window):
        super(Start, self).__init__(window)
        self.window = window
        self.window.background('start')

        self.layout = QVBoxLayout()
        self.btn_layout = QVBoxLayout()

        self.img = QLabel()
        self.pixmap = QPixmap('Data/Images/faceid_white_icon.png')

        self.lbl = QLabel()
        self.lbl_description = QLabel()

        self.btn_next = QPushButton()

        self.init_ui()

    def init_ui(self):
        self.layout.addStretch(2)
        self.lbl.setText('Презентация FaceID')
        self.lbl.setStyleSheet('font-size: 42px; color: white; background: transparent;')
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.lbl)

        self.lbl_description.setText('Выполнил студент Масленников Дмитрий')
        self.lbl_description.setStyleSheet('font-size: 26px; color: white; background: transparent;')
        self.lbl_description.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.lbl_description)

        self.layout.addStretch(1)

        self.img.setPixmap(self.pixmap.scaledToHeight(100))
        self.img.setStyleSheet('background: transparent;')
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.img)

        self.layout.addStretch(1)

        self.btn_next.setText('Начинаем')
        self.btn_next.setStyleSheet('''
            max-width: 110px;
            border-radius: 20px;
            border: 1px solid blue;
            background: blue;
            color: white;
            font-size: 15px;
            font-weight: bold;
            padding: 12px 25px;
            margin-top: 30px;
        ''')
        self.btn_next.clicked.connect(self.toDescription)
        self.btn_layout.addWidget(self.btn_next)

        self.btn_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addLayout(self.btn_layout)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.layout)

    def toDescription(self):
        self.window.update_widget(Description(self.window))