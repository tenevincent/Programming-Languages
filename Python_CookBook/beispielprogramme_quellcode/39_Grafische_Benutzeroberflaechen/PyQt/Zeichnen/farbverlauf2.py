#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class MeinWidget(QtWidgets.QWidget):
    def __init__(self, parent=None): 
        super().__init__(parent)
        self.grafik = QtGui.QImage("lena.png")
        self.ziel = QtCore.QRect(10, 10, 130, 130) 
        self.quelle = QtCore.QRect(0, 0, self.grafik.width(), self.grafik.height())

        self.pen = QtGui.QPen(QtGui.QColor(0,0,0)) 
        self.pen.setWidth(3)

        gradient = QtGui.QLinearGradient(10, 10, 130, 130)
        gradient.setColorAt(0.0, QtGui.QColor(0,0,0,255))
        gradient.setColorAt(1.0, QtGui.QColor(255,255,255,0))
        self.brush = QtGui.QBrush(gradient)
        
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(self.ziel, self.grafik, self.quelle)
        
        painter.setPen(self.pen) 
        painter.setBrush(self.brush) 
        painter.drawRect(10, 10, 130, 130)
        
app = QtWidgets.QApplication(sys.argv) 
widget = MeinWidget()
widget.resize(150, 150) 
widget.show()
sys.exit(app.exec_())
 
