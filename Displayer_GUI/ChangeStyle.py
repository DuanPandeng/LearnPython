# -*- coding: utf-8 -*-

"""
Module implementing ChangeStyleForm.
"""
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Ui_ChangeStyle import Ui_ChangeStyleForm


class ChangeStyleForm(QWidget, Ui_ChangeStyleForm):

    def __init__(self, parent=None):
        super(ChangeStyleForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Sytle Change Window")
        self.ChangeStylecomboBox.addItems(QStyleFactory.keys())
        index = self.ChangeStylecomboBox.findText(QApplication.style().objectName(), QtCore.Qt.MatchFixedString)
        self.ChangeStylecomboBox.setCurrentIndex(index)
        self.ChangeStylecomboBox.activated[str].connect(self.handlesStyleChanged)
        
    def handlesStyleChanged(self,  style):
        QApplication.setStyle(style)

