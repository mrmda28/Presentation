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

        self.lbl = QLabel()
        self.db_label = QLabel()
        self.stat_label = QLabel()
        self.man_label = QLabel()
        self.btn_db = QPushButton()
        self.btn_stat = QPushButton()
        self.btn_man = QPushButton()

        self.init_ui()

    def init_ui(self):
        self.lbl.setText('Description Page')
        self.lbl.setStyleSheet('font-size: 28px; color: black;')
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addStretch(1)
        self.layout.addWidget(self.lbl)

        # ----------- CARD 1 -------------
        self.db_label.setText('Database')
        self.db_label.setStyleSheet('font-size: 28px; color: black;')
        self.db_layout.addWidget(self.db_label)

        self.btn_db.setText('to Database')
        self.btn_db.setStyleSheet('''
            max-width: 88px;
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
        self.db_layout.addWidget(self.btn_db)

        # ----------- CARD 2 -------------
        self.stat_label.setText('Statistics')
        self.stat_label.setStyleSheet('font-size: 28px; color: black;')
        self.stat_layout.addWidget(self.stat_label)

        self.btn_stat.setText('to Statistics')
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
        self.stat_layout.addWidget(self.btn_stat)

        # ----------- CARD 3 -------------
        self.man_label.setText('How to use?')
        self.man_label.setStyleSheet('font-size: 28px; color: black;')
        self.man_layout.addWidget(self.man_label)

        self.btn_man.setText('to Manual')
        self.btn_man.setStyleSheet('''
                    max-width: 80px;
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
        self.man_layout.addWidget(self.btn_man)
        # ----------------------------------------
        self.cards_layout.addStretch(1)
        self.cards_layout.addLayout(self.db_layout)
        self.cards_layout.addStretch(1)
        self.cards_layout.addLayout(self.stat_layout)
        self.cards_layout.addStretch(1)
        self.cards_layout.addLayout(self.man_layout)
        self.cards_layout.addStretch(1)

        self.layout.addStretch(1)
        self.layout.addLayout(self.cards_layout)
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