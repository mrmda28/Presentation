from PyQt5.QtMultimediaWidgets import QVideoWidget

from GUI.MainWindow import *


class Manual(QWidget):
    def __init__(self, window):
        super(Manual, self).__init__(window)
        self.window = window
        self.window.background('manual')

        self.layout = QVBoxLayout()
        self.btn_layout = QHBoxLayout()

        self.video = QVideoWidget()

        self.lbl = QLabel()
        self.lbl_description = QLabel()

        self.btn_next = QPushButton()
        self.btn_back = QPushButton()

        self.init_ui()

    def init_ui(self):
        self.lbl.setText('Manual Page')
        self.lbl.setStyleSheet('font-size: 28px; color: black;')
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addStretch(1)
        self.layout.addWidget(self.lbl)

        self.lbl_description.setText('Description of this page')
        self.lbl_description.setStyleSheet('font-size: 24px; color: black;')
        self.lbl_description.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.lbl_description)



        self.btn_back.setText('Back')
        self.btn_back.setStyleSheet('''
                                    max-width: 40px;
                                    border-radius: 20px;
                                    border: 1px solid gray;
                                    background: gray;
                                    color: white;
                                    font-size: 15px;
                                    font-weight: bold;
                                    padding: 12px 45px;
                                    margin-top: 30px;
                                ''')
        self.btn_back.clicked.connect(self.Back)
        self.btn_layout.addWidget(self.btn_back)

        self.btn_next.setText('Next')
        self.btn_next.setStyleSheet('''
            max-width: 40px;
            border-radius: 20px;
            border: 1px solid blue;
            background: blue;
            color: white;
            font-size: 15px;
            font-weight: bold;
            padding: 12px 45px;
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