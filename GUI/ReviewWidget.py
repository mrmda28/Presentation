from PyQt5.QtWidgets import QTextEdit, QMessageBox
from db import add
from GUI.MainWindow import *


class Review(QWidget):
    def __init__(self, window):
        super(Review, self).__init__(window)
        self.window = window
        self.window.background('database')

        self.layout = QHBoxLayout()
        self.review_layout = QVBoxLayout()
        self.btn_layout = QVBoxLayout()

        self.input_name = QLineEdit()
        self.review = QTextEdit()

        self.lbl = QLabel()
        self.lbl_description = QLabel()

        self.btn_exit = QPushButton()

        self.message = QMessageBox()

        self.init_ui()

    def init_ui(self):
        self.review_layout.addStretch(2)
        self.lbl.setText('Отзыв')
        self.lbl.setStyleSheet('font-size: 28px; color: black;')
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.review_layout.addWidget(self.lbl)

        self.review_layout.addStretch(1)

        self.lbl_description.setText('Буду рад, если напишите отзыв о данной презентации')
        self.lbl_description.setStyleSheet('font-size: 24px; color: black;')
        self.lbl_description.setAlignment(QtCore.Qt.AlignCenter)
        self.review_layout.addWidget(self.lbl_description)

        self.review_layout.addStretch(1)

        self.input_name.setPlaceholderText('Ваше Имя')
        self.input_name.setStyleSheet('''
                    min-height: 40%;
                    background: #eee;
                    font-size: 18px;
                    border: none;
                    border-radius: 10px;
                    padding: 12px 15px;
                    margin: 8px 50px;
                ''')
        self.review_layout.addWidget(self.input_name)

        self.review_layout.addStretch(1)

        self.review.setPlaceholderText('Напишите Вашу оценку данной презентации')
        self.review.setStyleSheet('''
                            min-height: 80%;
                            background: #eee;
                            font-size: 18px;
                            border: none;
                            border-radius: 10px;
                            padding: 12px 15px;
                            margin: 8px 50px;
                        ''')
        self.review_layout.addWidget(self.review)

        self.review_layout.addStretch(1)

        self.btn_exit.setText('Отправить и выйти')
        self.btn_exit.setStyleSheet('''
            max-width: 150px;
            border-radius: 20px;
            border: 1px solid blue;
            background: blue;
            color: white;
            font-size: 15px;
            font-weight: bold;
            padding: 12px 15px;
            margin-top: 30px;
        ''')
        self.btn_exit.clicked.connect(self.Exit)
        self.btn_layout.addWidget(self.btn_exit)

        self.btn_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.review_layout.addLayout(self.btn_layout)
        self.review_layout.addStretch(2)
        self.layout.addStretch(1)
        self.layout.addLayout(self.review_layout, 4)
        self.layout.addStretch(1)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.layout)

    def Exit(self):
        try:
            name = self.input_name.text()
            text = self.review.toPlainText()

            if (name and text) != '':
                add(name, text)

                self.message.setText('Успешно :)')
                self.message.setStyleSheet('background: white;')
                self.message.exec_()

                QtCore.QCoreApplication.instance().quit()
            else:
                self.message.setText('Заполните все поля')
                self.message.setStyleSheet('background: white;')
                self.message.exec_()
        except:
            self.message.setText('В чем-то ошибка :(')
            self.message.setStyleSheet('background: white;')
            self.message.exec_()