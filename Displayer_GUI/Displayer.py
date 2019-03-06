# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
import os

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from Ui_Displayer import Ui_MainWindow 
from ChangeStyle import ChangeStyleForm 

from asammdf import MDF
import pandas as pd

Origindir = os.getcwd()

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        global InputSignals
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("MDF Displayer")
        self.MatplotlibWidget_1.setVisible(False)
        self.LoadFileButton.clicked.connect(self.openMsg)
        self.InputSignalsBox.textChanged.connect(self.get_Input)
        self.listWidget.itemClicked.connect(self.set_Input)
        # Create Children Form 
        self.child_CS = ChangeStyleForm()
        self.ChangeStyleAction.triggered.connect(self.child_CSShow)
    
    def child_CSShow(self):
        self.child_CS.show()
    
    def set_Input(self, item):
        self.InputSignalsBox.setText(item.text())
        
    def get_Input(self):
        self.statusBar.showMessage("Select Signal")
        if not self.ShowDirBrowser.toPlainText():
            self.msg_file()
        else:
            self.listWidget.clear()
            select_Signals = []
            Inputvalue = self.InputSignalsBox.text()
            Signals = list(channels)
            for i in Signals:
                if Inputvalue.lower() in i.lower():
                    select_Signals.append(i)
            self.listWidget.addItems(select_Signals)
    
    def openMsg(self):
        global file, dir,  channels,  mdf
        self.statusBar.showMessage("Select target file")
        dirfile,  _ = QFileDialog.getOpenFileName(self,  "打开" , "D:/4_SW_Tool/SW_Project/Python/",  "All Files(*);; Text Filesle(*.txt)")
        if dirfile.endswith('.mdf'):
            self.ShowDirBrowser.setText(dirfile)
            file = os.path.split(dirfile)[1]
            dir = os.path.split(dirfile)[0]
            
            os.chdir(dir)
            mdf = MDF(file)
            os.chdir(Origindir)
            channels = mdf.export('pandas').columns
        else:
            self.msg_file()
    
    @pyqtSlot()
    def on_DisplayButton_clicked(self):
        showsignal = self.InputSignalsBox.text()
        self.listWidget.clear()

        if not showsignal:
            self.msg_signal()
        elif showsignal in channels:
            sig_raw = mdf.get(showsignal).samples
            self.MatplotlibWidget_1.setVisible(True)
            sig1 = pd.Series(sig_raw)
            self.MatplotlibWidget_1.mpl.start_static_plot(sig1)
            self.statusBar.showMessage("Signal Display")
        else:
            self.msg_signalwrong()
                
    def msg_file(self):
        QMessageBox.information(self,  "提示",  "Please select a .mdf file")
        self.ShowDirBrowser.setText("")
        
    def msg_signal(self):
        QMessageBox.information(self,  "提示",  "First, you need to input signal")
    
    def msg_signalwrong(self):
        QMessageBox.information(self,  "提示",  "Cannot find the signal, please input it again")
        self.InputSignalsBox.setText("")

        
if __name__=="__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
