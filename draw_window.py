from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from screeninfo import get_monitors
from pynput import mouse
import sys


class DrawWindow(QMainWindow):
    
    mouse_clicked = pyqtSignal()
    
    def __init__(self):
        super().__init__()

        screen_size = []

        for m in get_monitors():
            screen_size.append(m.width)
            screen_size.append(m.height)

        self.fill_color = Qt.white


        self.label = QLabel()
        self.canvas = QPixmap(screen_size[0], screen_size[1])
        self.canvas.fill(self.fill_color)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)

        self.setWindowIcon(QIcon("Images//Exo_Pen_Logo_Large.png"))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
    
    def mousePressEvent(self, event):
        self.mouse_clicked.emit()