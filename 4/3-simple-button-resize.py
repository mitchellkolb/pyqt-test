


# https://doc.qt.io/qtforpython-6/tutorials/basictutorial/clickablebutton.html

# This is the second tutorial from the PyQT docs

import sys 
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow
from PySide6.QtCore import Slot

@Slot()
def sayHello():
    print("I was clicked")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Adjustable Window Button")
        self.setMinimumSize(300,300)

        # Create the clickable button
        self.mainButton = QPushButton("Click Plz", self)
        self.mainButton.clicked.connect(sayHello)
        self.mainButton.resize(100, 40)

        # Have the button centered
        self.centerButton()

    def resizeEvent(self, event):
        # When the window is resized by the user adjust the button to the center
        self.centerButton()
        super().resizeEvent(event)

    def centerButton(self):
        windowWidth = self.width()
        windowHeight = self.height()
        buttonWidth = self.mainButton.width()
        buttonHeight = self.mainButton.height()

        newX = (windowWidth - buttonWidth) // 2
        newY = (windowHeight - buttonHeight) // 2

        # Place the button in the center of the new window size
        self.mainButton.move(newX, newY)



# Start the Qt Application
app = QApplication(sys.argv)
window = MainWindow()
window.show()

# Start the main Qt loop
app.exec()