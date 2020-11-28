from PyQt5.QtGui import QPixmap

from GUI.MainWindow import *


class Database(QWidget):
    def __init__(self, window):
        super(Database, self).__init__(window)
        self.window = window
        self.window.background('database')

        self.layout = QVBoxLayout()
        self.btn_layout = QHBoxLayout()
        self.img_layout = QHBoxLayout()


        self.lbl = QLabel()
        self.lbl_description = QLabel()

        self.img = QLabel()
        self.pixmap = QPixmap('Data/Images/db.png')

        self.btn_next = QPushButton()
        self.btn_back = QPushButton()

        self.init_ui()

    def init_ui(self):
        self.lbl.setText('Database Page')
        self.lbl.setStyleSheet('font-size: 28px; color: black;')
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addStretch(1)
        self.layout.addWidget(self.lbl)

        self.lbl_description.setText('Description of this page')
        self.lbl_description.setStyleSheet('font-size: 24px; color: black;')
        self.lbl_description.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.lbl_description)

        self.layout.addStretch(1)

        self.img.setPixmap(self.pixmap.scaledToHeight(400))
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.img_layout.addWidget(self.img)
        self.layout.addLayout(self.img_layout)

        self.layout.addStretch(1)

        self.btn_back.setText('Назад')
        self.btn_back.setStyleSheet('''
                    max-width: 70px;
                    border-radius: 20px;
                    border: 1px solid gray;
                    background: transparent;
                    color: gray;
                    font-size: 15px;
                    font-weight: bold;
                    padding: 12px 15px;
                    margin-top: 30px;
                ''')
        self.btn_back.clicked.connect(self.Back)
        self.btn_layout.addWidget(self.btn_back)

        self.btn_next.setText('Далее')
        self.btn_next.setStyleSheet('''
            max-width: 70px;
            border-radius: 20px;
            border: 1px solid blue;
            background: blue;
            color: white;
            font-size: 15px;
            font-weight: bold;
            padding: 12px 15px;
            margin-top: 30px;
        ''')
        self.btn_next.clicked.connect(self.toGit)
        self.btn_layout.addWidget(self.btn_next)

        # self.layout.setAlignment(QtCore.Qt.AlignCenter)

        self.layout.addLayout(self.btn_layout)
        self.layout.addStretch(1)

        self.setLayout(self.layout)

    def toGit(self):
        from GUI.GitWidget import Git
        self.window.update_widget(Git(self.window))

    def Back(self):
        from GUI.CardsWidget import Cards
        self.window.update_widget(Cards(self.window))