import webbrowser

from GUI.MainWindow import *


class Git(QWidget):
    def __init__(self, window):
        super(Git, self).__init__(window)
        self.window = window
        self.window.background('database')

        self.layout = QVBoxLayout()
        self.btn_layout = QVBoxLayout()

        self.lbl = QLabel()
        self.lbl_description = QLabel()

        self.btn_git = QPushButton()
        self.btn_next = QPushButton()

        self.init_ui()

    def init_ui(self):
        self.lbl.setText('GitHub Page')
        self.lbl.setStyleSheet('font-size: 28px; color: black;')
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.lbl)

        self.btn_git.setText('Open GitHub page')
        self.btn_git.setStyleSheet('font-size: 24px; color: black; border: none; border-bottom: 3px solid yellow;')
        self.btn_git.clicked.connect(lambda: webbrowser.open('https://github.com/mrmda28/FaceID'))
        self.layout.addWidget(self.btn_git)

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
        self.btn_next.clicked.connect(self.toReview)
        self.btn_layout.addWidget(self.btn_next)

        self.btn_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addLayout(self.btn_layout)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.layout)

    def toReview(self):
        from GUI.ReviewWidget import Review
        self.window.update_widget(Review(self.window))