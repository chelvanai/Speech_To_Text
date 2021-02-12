import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    button1 = QPushButton(widget)
    button1.setText("Voice2Text")
    button1.setGeometry(100,100,100,50)
    button1.setIcon(QIcon("voice-to-text.png"))
    button1.move(200, 400)
    button1.clicked.connect(clicked)

    widget.setGeometry(50, 50, 500, 500)
    widget.setWindowTitle("voice to text")
    widget.show()
    sys.exit(app.exec_())


def clicked():
    print("Button 1 clicked")


if __name__ == '__main__':
    window()
