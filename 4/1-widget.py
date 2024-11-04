

# https://doc.qt.io/qtforpython-6/tutorials/basictutorial/widgets.html#tutorial-widgets

# I will be following this tutorial from the PyQT website above

import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("Michael")
label.show()
app.exec()