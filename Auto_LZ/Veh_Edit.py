# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
#import os
import json
from PyQt5.QtCore import pyqtSlot,  pyqtSignal
from PyQt5.QtWidgets import QDialog

from Ui_Veh_Edit import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    
    dialogSignal = pyqtSignal(int,  dict)
    
    def __init__(self, parent=None):
        global load_dict
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('添加或删除车辆')
        self.setFixedSize(self.width(), self.height())
        with open('Auto_LZ.json', 'r') as load_f:
            load_dict = json.load(load_f)
            VIN = load_dict['vin']
            self.textEdit.setPlainText(str(VIN)[1:-1].replace(',', '\n'))
    
    @pyqtSlot()
    def on_pushButton_save_clicked(self):
        global load_dict
        VIN_Set = self.textEdit.toPlainText()
        VIN_Str = '{' + VIN_Set.replace('\n',  ',') + '}'
        VIN_New = eval(VIN_Str)
        load_dict['vin'] =  VIN_New
        with open('Auto_LZ.json', 'w') as f:
            json.dump(load_dict, f, indent=4)
        self.dialogSignal.emit(1,  VIN_New)
        self.destroy()
    
    @pyqtSlot()
    def on_pushButton_cancel_clicked(self):
        self.dialogSignal.emit(0,  {})
        self.destroy()
