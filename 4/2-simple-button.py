


# https://doc.qt.io/qtforpython-6/tutorials/basictutorial/clickablebutton.html

# This is the second tutorial from the PyQT docs

import sys 
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow
from PySide6.QtCore import Slot

@Slot()
def sayHello():
    print("Was Clicked")

# Creates the Qt Application
app = QApplication(sys.argv)

# Creates the button
button = QPushButton("CLICK PLZ")

# Connect the button to the function hello above
button.clicked.connect(sayHello)

# Show the button
button.show()

# Start the main Qt loop
app.exec()

