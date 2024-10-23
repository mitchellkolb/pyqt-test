

#Code from tutorial. https://youtu.be/wdEpWCFf40U?si=OodxvwZWVYtBb2OD

import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QFileDialog, QSlider, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QUrl, QTimer
from PyQt6.QtMultimedia import QMediaPlayer, QAudioFormat


class AudioApp(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()

    # Settings portion
    def settings(self):
        self.setWindowTitle("Audio-Adjuster") # Title of the window that the OS sees 
        self.setGeometry(500, 700, 600, 300) # Where on the screen does it appear
        #self.resize(600, 300) # Size of the indow when it appears

    # Desing of the UI
    def initUI(self):
        self.title = QLabel("Audio Adjuster")
        self.fileTitle = QListWidget()
        self.btnOpener = QPushButton("Choose a File Please")
        self.btnPlay = QPushButton("Play")
        self.btnPause = QPushButton("Pause")
        self.btnReset = QPushButton("Reset")
        self.btnResume = QPushButton("Resume")

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(50)
        self.slider.setMaximum(100)
        self.slider.setValue(100) #Playback speed
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)

        #Create a layout
        self.mainLayout = QVBoxLayout()
        row = QHBoxLayout()
        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        self.mainLayout.addWidget(self.title)
        self.mainLayout.addWidget(self.slider)

        col1.addWidget(self.fileTitle)
        col2.addWidget(self.btnOpener)
        col2.addWidget(self.btnPlay)
        col2.addWidget(self.btnPause)
        col2.addWidget(self.btnResume)
        col2.addWidget(self.btnReset)

        row.addLayout(col1)
        row.addLayout(col2)

        self.mainLayout.addLayout(row)
        self.setLayout(self.mainLayout)

    # Event Handler

if __name__ in "__main__":
    app = QApplication([])
    main = AudioApp()
    main.show()
    app.exec()