# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import pyqtSlot,  QObject,  pyqtSignal
from PyQt5.QtWidgets import QDialog,  QApplication
from Ui_Radius_Map_W import Ui_Dialog
from Radius_Map import *


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        global whole,  Spd_list
        whole = False
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('MPP')
        
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        
        Spd_list = ["20", "30", "40", "60", "80", "100", "120", "130"]
        Ra_list_20 = ["15", "25", "50", "75", "100"]
        self.comboBox_speed.addItems(Spd_list)
        self.comboBox_speed.currentIndexChanged.connect(self.selectionchange)
        self.comboBox_radius.addItems(Ra_list_20)
        self.comboBox_dir.addItem("right")
        self.comboBox_dir.addItem("left")
        self.comboBox_dir.addItem("both")
        self.comboBox_dir.setCurrentText('both')
        self.checkBox_all.toggled.connect(lambda:self.btnstate(self.checkBox_all))

    def selectionchange(self):
        Ra_list_20 = [0,  15, 25, 50, 75, 100]
        Ra_list_30 = [0, 30, 50, 75, 100, 125, 150, 175, 200]
        Ra_list_40 = [0, 60, 75, 100, 125, 150, 175, 200, 225, 250]
        Ra_list_60 = [0, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400]
        Ra_list_80 = [0, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
        Ra_list_100 = [0, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
        Ra_list_120 = [0, 650, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200]
        Ra_list_130 = [0, 750, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300]
        Spd_Ra_dict = {"20": Ra_list_20, "30": Ra_list_30, "40":Ra_list_40, "60":Ra_list_60, "80":Ra_list_80, "100":Ra_list_100, "120":Ra_list_120, "130":Ra_list_130}
        
        spd = self.comboBox_speed.currentText()
        if spd in Spd_Ra_dict.keys():
            Ra_list = Spd_Ra_dict[spd][1:]
            Ra_list_Str = [str(x) for x in Ra_list]
            self.comboBox_radius.clear()
            self.comboBox_radius.addItems(Ra_list_Str)

    def btnstate(self, btn):
        global whole, Spd_list
        if btn.isChecked() == True:
            self.comboBox_speed.clear()
            self.comboBox_radius.clear()
            whole = True
        else:
            self.comboBox_speed.addItems(Spd_list)
            whole = False

    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        cursor = self.textEdit_display.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.textEdit_display.setTextCursor(cursor)
        self.textEdit_display.ensureCursorVisible()

    @pyqtSlot()
    def on_pushButton_display_clicked(self):
        global whole
        spd = self.comboBox_speed.currentText()
        rad = self.comboBox_radius.currentText()
        Dir = self.comboBox_dir.currentText()
        dirfile = self.lineEdit_add_file.text()
        if len(dirfile)>0:
            file = os.path.split(dirfile)[1]
        else:
            file = ""
        Radius_Map_Main( file, whole,  spd, rad, Dir)
    
    def closeEvent(self, event):
    	global _console_
    	sys.stdout=_console_
    
    @pyqtSlot()
    def on_pushButton_add_file_clicked(self):
        dirfile,  _ = QFileDialog.getOpenFileName(self,  "打开" , "/",  "All Files(*);;JSON Files(*.json)")
        if dirfile.endswith('.json'):
            self.lineEdit_add_file.setText(dirfile)
        else:
            self.msg_file()
    
    def msg_file(self):
        QMessageBox.information(self,  "提示",  "Please select a .json file")
        self.lineEdit_add_file.setText("")

class EmittingStream(QObject):
    textWritten = pyqtSignal(str)
    def write(self, text):
        self.textWritten.emit(str(text)) 

if __name__=="__main__":
    app = QApplication(sys.argv)
    _console_=sys.stdout
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
