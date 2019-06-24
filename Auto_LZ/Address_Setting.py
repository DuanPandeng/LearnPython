# -*- coding: utf-8 -*-

"""
Module implementing Dialog_Address_Setting.
"""
import os
import json
from PyQt5.QtCore import pyqtSlot,  pyqtSignal
from PyQt5.QtWidgets import QDialog

from Ui_Address_Setting import Ui_Dialog


class Dialog_Address_Setting(QDialog, Ui_Dialog):
    
    dialog_AS_Signal = pyqtSignal(int)
    
    def __init__(self, parent=None):
        global load_dict
        super(Dialog_Address_Setting, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Zep地址自动配置')
        self.setFixedSize(self.width(), self.height())
        
        if os.path.exists('Auto_LZ.json'):
            with open('Auto_LZ.json', 'r') as load_f:
                load_dict = json.load(load_f)
            if len(load_dict)>16:
                key_list = list(load_dict['Match'].keys())
                value_list = list(load_dict['Match'].values())
                self.lineEdit_AS_keys_1.setText('{}'.format(key_list[0]))
                self.lineEdit_AS_keys_2.setText('{}'.format(key_list[1]))
                self.lineEdit_AS_keys_3.setText('{}'.format(key_list[2]))
                self.lineEdit_AS_keys_4.setText('{}'.format(key_list[3]))          
                self.lineEdit_AS_keys_5.setText('{}'.format(key_list[4]))
                self.lineEdit_AS_keys_6.setText('{}'.format(key_list[5]))          
                self.lineEdit_AS_keys_7.setText('{}'.format(key_list[6]))
                self.lineEdit_AS_keys_8.setText('{}'.format(key_list[7])) 
                self.lineEdit_AS_address1.setText('{}'.format(value_list[0]))
                self.lineEdit_AS_address2.setText('{}'.format(value_list[1]))
                self.lineEdit_AS_address3.setText('{}'.format(value_list[2]))
                self.lineEdit_AS_address4.setText('{}'.format(value_list[3]))
                self.lineEdit_AS_address5.setText('{}'.format(value_list[4]))
                self.lineEdit_AS_address6.setText('{}'.format(value_list[5]))
                self.lineEdit_AS_address7.setText('{}'.format(value_list[6]))
                self.lineEdit_AS_address8.setText('{}'.format(value_list[7]))

    @pyqtSlot()
    def on_pushButton_AS_save_clicked(self):
        global load_dict
        load_dict['Match'].clear()
        load_dict['Match'][self.lineEdit_AS_keys_1.text()]=self.lineEdit_AS_address1.text()
        load_dict['Match'][self.lineEdit_AS_keys_2.text()]=self.lineEdit_AS_address2.text()
        load_dict['Match'][self.lineEdit_AS_keys_3.text()]=self.lineEdit_AS_address3.text()
        load_dict['Match'][self.lineEdit_AS_keys_4.text()]=self.lineEdit_AS_address4.text()
        load_dict['Match'][self.lineEdit_AS_keys_5.text()]=self.lineEdit_AS_address5.text()
        load_dict['Match'][self.lineEdit_AS_keys_6.text()]=self.lineEdit_AS_address6.text()
        load_dict['Match'][self.lineEdit_AS_keys_7.text()]=self.lineEdit_AS_address7.text()
        load_dict['Match'][self.lineEdit_AS_keys_8.text()]=self.lineEdit_AS_address8.text()

        with open('Auto_LZ.json', 'w') as f:
            json.dump(load_dict, f, indent=4)
        self.dialog_AS_Signal.emit(1)
        self.destroy()
    
    @pyqtSlot()
    def on_pushButton_AS_cancel_clicked(self):
        self.dialog_AS_Signal.emit(0)
        self.destroy()
