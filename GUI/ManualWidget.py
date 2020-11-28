from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QStyle, QSlider

from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
import sys

from GUI.MainWindow import *


class Manual(QWidget):
    def __init__(self, window):
        super(Manual, self).__init__(window)
        self.window = window
        self.window.background('manual')

        self.label_layout = QVBoxLayout()
        self.hboxLayout = QHBoxLayout()
        self.vboxLayout = QVBoxLayout()
        self.v = QVBoxLayout()
        self.h = QHBoxLayout()

        self.lbl = QLabel()
        self.lbl_description = QLabel()

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile('/Users/mrmda28/Desktop/Project/Presentation/Data/manual.mp4')))

        self.videowidget = QVideoWidget()

        self.btn_next = QPushButton()
        self.btn_back = QPushButton()
        self.btn_play = QPushButton()
        self.btn_mute = QPushButton()

        self.init_ui()

        self.show()

    def init_ui(self):
        self.lbl.setText('Обучающее видео')
        self.lbl.setStyleSheet('font-size: 36px; color: black;')
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.label_layout.addWidget(self.lbl)

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

        self.btn_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.btn_play.setStyleSheet('max-width: 30px; margin-top: 30px;')
        self.btn_play.clicked.connect(self.play)

        self.btn_mute.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        self.btn_mute.setStyleSheet('max-width: 30px; margin-top: 30px;')
        self.btn_mute.clicked.connect(self.mute)

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

        self.hboxLayout.addStretch(1)
        self.hboxLayout.addWidget(self.btn_back)
        self.hboxLayout.addStretch(1)
        self.hboxLayout.addWidget(self.btn_play)
        self.hboxLayout.addWidget(self.btn_mute)
        self.hboxLayout.addStretch(1)
        self.hboxLayout.addWidget(self.btn_next)
        self.hboxLayout.addStretch(1)

        self.v.addWidget(self.videowidget, 3)

        self.h.addStretch(1)
        self.h.addLayout(self.v, 5)
        self.h.addStretch(1)

        self.vboxLayout.addLayout(self.label_layout)
        self.vboxLayout.addLayout(self.h)
        self.vboxLayout.addLayout(self.hboxLayout)


        self.setLayout(self.vboxLayout)

        self.mediaPlayer.setVideoOutput(self.videowidget)


    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            self.btn_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        else:
            self.mediaPlayer.play()
            self.btn_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

    def mute(self):
        if self.mediaPlayer.isMuted() == True:
            self.mediaPlayer.setMuted(False)
            self.btn_mute.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        else:
            self.mediaPlayer.setMuted(True)
            self.btn_mute.setIcon(self.style().standardIcon(QStyle.SP_MediaVolumeMuted))

    def toGit(self):
        from GUI.GitWidget import Git
        self.window.update_widget(Git(self.window))

    def Back(self):
        from GUI.CardsWidget import Cards
        self.window.update_widget(Cards(self.window))