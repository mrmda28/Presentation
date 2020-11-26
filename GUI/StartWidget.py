from GUI.DescriptionWidget import Description
from GUI.MainWindow import *


class Start(QWidget):
    def __init__(self, window):
        super(Start, self).__init__(window)
        self.window = window
        self.window.background('start')

        self.layout = QVBoxLayout()
        self.btn_layout = QVBoxLayout()

        self.lbl = QLabel()
        self.lbl_description = QLabel()

        self.btn_next = QPushButton()

        self.init_ui()

    def init_ui(self):
        self.lbl.setText('Start Page')
        self.lbl.setStyleSheet('font-size: 28px; color: black;')
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.lbl)

        self.lbl_description.setText('Description of this page')
        self.lbl_description.setStyleSheet('font-size: 24px; color: black;')
        self.lbl_description.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.lbl_description)

        self.btn_next.setText('Start')
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
        self.btn_next.clicked.connect(self.toDescription)
        self.btn_layout.addWidget(self.btn_next)

        self.btn_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addLayout(self.btn_layout)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.layout)

    def toDescription(self):
        self.window.update_widget(Description(self.window))