from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QMovie

from GUI.MainWindow import *


class Cards(QWidget):
    def __init__(self, window):
        super(Cards, self).__init__(window)
        self.window = window
        self.window.background('cards')

        self.layout = QVBoxLayout()
        self.cards_layout = QHBoxLayout()
        self.db_layout = QVBoxLayout()
        self.stat_layout = QVBoxLayout()
        self.man_layout = QVBoxLayout()

        self.img_db = QLabel()
        self.movie_db = QMovie('Data/Images/db.gif')
        self.movie_db.setScaledSize(QSize().scaled(120, 120, Qt.KeepAspectRatio))

        self.img_stat = QLabel()
        self.movie_stat = QMovie('Data/Images/statistics.gif')
        self.movie_stat.setScaledSize(QSize().scaled(120, 120, Qt.KeepAspectRatio))

        self.img_man = QLabel()
        self.movie_man = QMovie('Data/Images/manual.gif')
        self.movie_man.setScaledSize(QSize().scaled(120, 120, Qt.KeepAspectRatio))

        self.lbl = QLabel()
        self.db_label = QLabel()
        self.db_d_label = QLabel()

        self.stat_label = QLabel()
        self.stat_d_label = QLabel()

        self.man_label = QLabel()
        self.man_d_label = QLabel()

        self.btn_db = QPushButton()
        self.btn_db_layout = QHBoxLayout()

        self.btn_stat = QPushButton()
        self.btn_stat_layout = QHBoxLayout()

        self.btn_man = QPushButton()
        self.btn_man_layout = QHBoxLayout()

        self.init_ui()

    def init_ui(self):
        self.lbl.setText('Выбирай свой путь')
        self.lbl.setStyleSheet('font-size: 28px; color: black;')
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addStretch(1)
        self.layout.addWidget(self.lbl)

        # ----------- CARD 1 -------------
        self.img_db.setMovie(self.movie_db)
        self.img_db.setAlignment(QtCore.Qt.AlignCenter)
        self.db_layout.addStretch(2)
        self.db_layout.addWidget(self.img_db)
        self.movie_db.start()

        self.db_layout.addStretch(1)

        self.db_label.setText('База данных')
        self.db_label.setStyleSheet('font-size: 28px; color: black;')
        self.db_label.setAlignment(QtCore.Qt.AlignCenter)
        self.db_layout.addWidget(self.db_label)

        self.db_d_label.setText('Здесь можно посмотреть\nструктуру базы данных')
        self.db_d_label.setStyleSheet('font-size: 16px; color: gray;')
        self.db_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.db_layout.addWidget(self.db_d_label)

        self.btn_db.setText('Посмотреть')
        self.btn_db.setStyleSheet('''
            max-width: 110px;
                    border-radius: 20px;
                    border: 1px solid blue;
                    background: blue;
                    color: white;
                    font-size: 15px;
                    font-weight: bold;
                    padding: 12px 10px;
                    margin-top: 30px;
        ''')
        self.btn_db.clicked.connect(self.toDB)
        self.btn_db_layout.addWidget(self.btn_db)
        self.btn_db_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.db_layout.addLayout(self.btn_db_layout)
        self.db_layout.addStretch(2)

        # ----------- CARD 2 -------------
        self.img_stat.setMovie(self.movie_stat)
        self.img_stat.setAlignment(QtCore.Qt.AlignCenter)
        self.stat_layout.addStretch(2)
        self.stat_layout.addWidget(self.img_stat)
        self.movie_stat.start()

        self.stat_layout.addStretch(1)

        self.stat_label.setText('Статистика')
        self.stat_label.setStyleSheet('font-size: 28px; color: black;')
        self.stat_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stat_layout.addWidget(self.stat_label)

        self.stat_d_label.setText('Статистический график\nпокажет время FaceID')
        self.stat_d_label.setStyleSheet('font-size: 16px; color: gray;')
        self.stat_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stat_layout.addWidget(self.stat_d_label)

        self.btn_stat.setText('Посмотреть')
        self.btn_stat.setStyleSheet('''
                    max-width: 110px;
                    border-radius: 20px;
                    border: 1px solid blue;
                    background: blue;
                    color: white;
                    font-size: 15px;
                    font-weight: bold;
                    padding: 12px 10px;
                    margin-top: 30px;
                ''')
        self.btn_stat.clicked.connect(self.toStatistics)
        self.btn_stat_layout.addWidget(self.btn_stat)
        self.btn_stat_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.stat_layout.addLayout(self.btn_stat_layout)
        self.stat_layout.addStretch(2)

        # ----------- CARD 3 -------------
        self.img_man.setMovie(self.movie_man)
        self.img_man.setAlignment(QtCore.Qt.AlignCenter)
        self.man_layout.addStretch(2)
        self.man_layout.addWidget(self.img_man)
        self.movie_man.start()

        self.man_layout.addStretch(1)

        self.man_label.setText('Инструкция')
        self.man_label.setStyleSheet('font-size: 28px; color: black;')
        self.man_label.setAlignment(QtCore.Qt.AlignCenter)
        self.man_layout.addWidget(self.man_label)

        self.man_d_label.setText('Обучающее видео покажет\nкак работает программа')
        self.man_d_label.setStyleSheet('font-size: 16px; color: gray;')
        self.man_d_label.setAlignment(QtCore.Qt.AlignCenter)
        self.man_layout.addWidget(self.man_d_label)

        self.btn_man.setText('Посмотреть')
        self.btn_man.setStyleSheet('''
                    max-width: 110px;
                    border-radius: 20px;
                    border: 1px solid blue;
                    background: blue;
                    color: white;
                    font-size: 15px;
                    font-weight: bold;
                    padding: 12px 10px;
                    margin-top: 30px;
                ''')
        self.btn_man.clicked.connect(self.toManual)
        self.btn_man_layout.addWidget(self.btn_man)
        self.btn_man_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.man_layout.addLayout(self.btn_man_layout)
        self.man_layout.addStretch(2)
        # ----------------------------------------
        self.cards_layout.addStretch(1)
        self.cards_layout.addLayout(self.db_layout)
        self.cards_layout.addStretch(1)
        self.cards_layout.addLayout(self.stat_layout)
        self.cards_layout.addStretch(1)
        self.cards_layout.addLayout(self.man_layout)
        self.cards_layout.addStretch(1)

        # self.layout.addStretch(1)
        self.layout.addLayout(self.cards_layout, 3)
        self.layout.addStretch(1)

        # self.layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.layout)

    def toDB(self):
        from GUI.DatabaseWidget import Database
        self.window.update_widget(Database(self.window))

    def toStatistics(self):
        from GUI.StatisticsWidget import Statistics
        self.window.update_widget(Statistics(self.window))

    def toManual(self):
        from GUI.ManualWidget import Manual
        self.window.update_widget(Manual(self.window))