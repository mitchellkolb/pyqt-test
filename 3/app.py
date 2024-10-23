

#Code from tutorial. https://youtu.be/wdEpWCFf40U?si=OodxvwZWVYtBb2OD

import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QFileDialog, QSlider, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QUrl, QTimer
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


class AudioApp(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()
        self.eventHandler()

    # Settings portion
    def settings(self):
        self.setWindowTitle("Audio-Adjuster") # Title of the window that the OS sees 
        self.setGeometry(500, 700, 600, 300) # Where on the screen does it appear
        #self.resize(600, 300) # Size of the indow when it appears

    # Desing of the UI
    def initUI(self):
        self.title = QLabel("Audio Adjuster")
        self.fileTitle = QListWidget()
        self.btnOpener = QPushButton("Choose a File")
        self.btnPlay = QPushButton("Play")
        self.btnPause = QPushButton("Pause")
        self.btnReset = QPushButton("Reset")
        self.btnResume = QPushButton("Resume")

        #Deactivate button for now
        self.btnPause.setDisabled(True)
        self.btnReset.setDisabled(True)
        self.btnResume.setDisabled(True)


        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(50)
        self.slider.setMaximum(100)
        self.slider.setValue(100) #Playback speed
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)

        self.sliderText = QLabel("Speed: 100x")
        self.sliderText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        sliderLayout = QHBoxLayout()
        sliderLayout.addWidget(self.sliderText)
        sliderLayout.addWidget(self.slider)

        #Create a layout
        self.mainLayout = QVBoxLayout()
        row = QHBoxLayout()
        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        self.mainLayout.addWidget(self.title)
        self.mainLayout.addLayout(sliderLayout)

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

        # Audio classes from pyqt
        self.audioOutput = QAudioOutput()
        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setAudioOutput(self.audioOutput)



    # Event Handler
    def eventHandler(self):
        self.slider.valueChanged.connect(self.updateSlider)
        self.btnOpener.clicked.connect(self.openFile)
        self.btnPlay.clicked.connect(self.playAudio)

    # Change slider number
    def updateSlider(self):
        speed = self.slider.value() / 100
        self.sliderText.setText(f"Speed: {speed:.2f}x")

    # Open files
    def openFile(self):
        path = QFileDialog.getExistingDirectory(self, "Pick Folder")

        if path:
            self.fileTitle.clear()
            for fileName in os.listdir(path):
                if fileName.endswith(".mp3"):
                    self.fileTitle.addItem(fileName)
        
        else:
            file, _ = QFileDialog.getOpenFileName(self, "Select File", filter="Audio Files (*.mp3)")
            if file:
                self.fileTitle.clear()
                self.fileTitle.addItem(os.path.basename(file))

    # Play Audio Files
    def playAudio(self):
        if self.fileTitle.selectedItems():
            fileName = self.fileTitle.selectedItems()[0].text()
            folderPath = QFileDialog.getExistingDirectory(self, "Select Folder")
            filePath = os.path.join(folderPath, fileName)
            fileUrl = QUrl.fromLocalFile(filePath)

            self.mediaPlayer.setSource(fileUrl)
            self.mediaPlayer.setPlaybackRate(self.slider.value() // 100.0)
            self.mediaPlayer.play()

            #Deactivate button for now
            self.btnPause.setEnabled(True)
            self.btnResume.setDisabled(True)
            self.btnReset.setEnabled(True)
            self.btnPlay.setDisabled(True)



if __name__ in "__main__":
    app = QApplication([])
    main = AudioApp()
    main.show()
    app.exec()