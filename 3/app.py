

#Code from tutorial. https://youtu.be/wdEpWCFf40U?si=OodxvwZWVYtBb2OD

import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QFileDialog, QSlider, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QUrl, QTimer
from PyQt6.QtMultimedia import QMediaPlayer, QAudioFormat


class AudioApp(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()

    # Settings portion
    def settings(self):
        self.setWindowTitle("Audio-Adjuster") # Title of the window that the OS sees 
        self.setGeometry(900, 600, 600, 300) # Where on the screen does it appear
        #self.resize(600, 300) # Size of the indow when it appears

    # Desing of the UI


    # Event Handler

if __name__ in "__main__":
    app = QApplication([])
    main = AudioApp()
    main.show()
    app.exec()