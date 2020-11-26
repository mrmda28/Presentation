from GUI.MainWindow import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


class Statistics(QWidget):
    def __init__(self, window):
        super(Statistics, self).__init__(window)
        self.window = window
        self.window.background('statistics')

        self.layout = QVBoxLayout()
        self.btn_layout = QHBoxLayout()

        self.lbl = QLabel()
        self.lbl_description = QLabel()

        self.btn_next = QPushButton()
        self.btn_back = QPushButton()

        self.init_ui()

    def init_ui(self):
        self.lbl.setText('Статистика времени входа')
        self.lbl.setStyleSheet('font-size: 28px; color: black;')
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addStretch(1)
        self.layout.addWidget(self.lbl)

        self.lbl_description.setText('График показывает сколько пользователь всреднем затрачивает времени\nна вход с помощью '
                                     'FaceID и email/password')
        self.lbl_description.setStyleSheet('font-size: 22px; color: black;')
        self.lbl_description.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.lbl_description)

        self.layout.addStretch(1)
        self.canvas = Canvas(self, width=8, height=8)
        self.layout.addWidget(self.canvas)
        self.layout.addStretch(1)

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


class Canvas(FigureCanvas):
    def __init__(self, parent, width=5, height=5, dpi=100):
        fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(fig)
        self.setParent(parent)

        self.ax.plot([0, 0.75], [0, 1], 'b-')
        self.ax.plot([0, 13], [0, 1], 'r-')

        self.ax.set(xlabel='Время', ylabel='Вход', title='(blue) - FaceID - 0.75c, (red) - email/password - 13c')
        self.ax.grid()