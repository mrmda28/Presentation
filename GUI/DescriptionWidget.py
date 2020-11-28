from PyQt5.QtGui import QPixmap

from GUI.MainWindow import *


class Description(QWidget):
    def __init__(self, window):
        super(Description, self).__init__(window)
        self.window = window
        self.window.background('description')

        self.layout = QVBoxLayout()
        self.btn_layout = QVBoxLayout()

        self.img = QLabel()
        self.pixmap = QPixmap('Data/Images/app.png')

        self.lbl = QLabel()
        self.lbl_description = QLabel()

        self.btn_next = QPushButton()

        self.init_ui()

    def init_ui(self):
        self.layout.addStretch(1)

        self.img.setPixmap(self.pixmap.scaledToWidth(550))
        self.img.setStyleSheet('background: transparent;')
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.img)

        self.layout.addStretch(1)

        self.lbl.setText('Функционал приложения')
        self.lbl.setStyleSheet('font-size: 28px; color: white; background: transparent;')
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.lbl)

        self.lbl_description.setText('Приложение позволяет пользователям использовать более быстрый\nи безопасный '
                                     'вход в приложение с помощью FaceID')
        self.lbl_description.setStyleSheet('font-size: 18px; color: white; background: transparent;')
        self.lbl_description.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.lbl_description)

        self.layout.addStretch(1)

        self.btn_next.setText('Дальше')
        self.btn_next.setStyleSheet('''
            max-width: 100px;
            border-radius: 20px;
            border: 1px solid blue;
            background: blue;
            color: white;
            font-size: 15px;
            font-weight: bold;
            padding: 12px 25px;
            margin-top: 30px;
        ''')
        self.btn_next.clicked.connect(self.toCards)
        self.btn_layout.addWidget(self.btn_next)

        self.btn_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addLayout(self.btn_layout)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.layout)

    def toCards(self):
        from GUI.CardsWidget import Cards
        self.window.update_widget(Cards(self.window))