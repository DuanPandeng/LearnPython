# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
import os
import json
import base64
import ctypes
import win32con
from win32process import SuspendThread, ResumeThread
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import pyqtSlot,  QObject,  pyqtSignal,  QThread
from PyQt5.QtWidgets import QMainWindow,  QApplication
from Ui_Auto_LZ_Main import Ui_MainWindow
from Auto_LZ_Qt import *
from Veh_Edit import *
from Address_Setting import *


class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        global Skip, load_dict,  Theadalive, Process_Info, Issue_Info
        Skip = "Yes"
        Theadalive = 0
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Auto_LZ')
        self.setFixedSize(self.width(), self.height())
        self.pushButton_end.setEnabled(False)
        self.checkBox_Skip.toggled.connect(lambda:self.btnstate_S(self.checkBox_Skip))
        
        Process_Info = EmittingStream(textWritten=self.normalOutputWritten)
        Issue_Info = EmittingStream(textWritten=self.errorOutputWritten)
        sys.stdout = Process_Info
        sys.stderr = Issue_Info
        
        if os.path.exists('Auto_LZ.json'):
            with open('Auto_LZ.json', 'r') as load_f:
                load_dict = json.load(load_f)
            if len(load_dict)>16:
                password_d = base64.b64decode('{}'.format(load_dict['password']).encode('utf-8'))
                password_r = str(password_d,'utf-8')
                self.lineEdit_password.setText('{}'.format(password_r))
                self.lineEdit_username.setText('{}'.format(load_dict['username']))
                self.lineEdit_start_date.setText('{}'.format(load_dict['start_date']))
                self.lineEdit_end_date.setText('{}'.format(load_dict['end_date']))
                self.lineEdit_key_words1.setText('{}'.format(load_dict['key_words1']))          
                self.lineEdit_Zep_Address1.setText('{}'.format(load_dict['Zep_Address1']))
                self.lineEdit_key_words2.setText('{}'.format(load_dict['key_words2']))          
                self.lineEdit_Zep_Address2.setText('{}'.format(load_dict['Zep_Address2']))
                self.lineEdit_key_words3.setText('{}'.format(load_dict['key_words3']))          
                self.lineEdit_Zep_Address3.setText('{}'.format(load_dict['Zep_Address3']))
                self.lineEdit_key_words4.setText('{}'.format(load_dict['key_words4']))          
                self.lineEdit_Zep_Address4.setText('{}'.format(load_dict['Zep_Address4']))
                self.lineEdit_key_words5.setText('{}'.format(load_dict['key_words5']))          
                self.lineEdit_Zep_Address5.setText('{}'.format(load_dict['Zep_Address5']))
                self.lineEdit_key_words6.setText('{}'.format(load_dict['key_words6']))          
                self.lineEdit_Zep_Address6.setText('{}'.format(load_dict['Zep_Address6']))                 
                
                self.comboBox_Veh.addItems(list(load_dict['vin'].keys()))
                self.comboBox_Veh.setCurrentText('{}'.format(load_dict['Veh']))
                self.comboBox_Fun1.addItems(load_dict['Fun_list'])
                self.comboBox_Fun1.setCurrentText('{}'.format(load_dict['Function1']))
                self.comboBox_Fun2.addItems(load_dict['Fun_list'])
                self.comboBox_Fun2.setCurrentText('{}'.format(load_dict['Function2']))
                self.comboBox_Fun3.addItems(load_dict['Fun_list'])
                self.comboBox_Fun3.setCurrentText('{}'.format(load_dict['Function3']))
                self.comboBox_Fun4.addItems(load_dict['Fun_list'])
                self.comboBox_Fun4.setCurrentText('{}'.format(load_dict['Function4']))
                self.comboBox_Fun5.addItems(load_dict['Fun_list'])
                self.comboBox_Fun5.setCurrentText('{}'.format(load_dict['Function5']))
                self.comboBox_Fun6.addItems(load_dict['Fun_list'])
                self.comboBox_Fun6.setCurrentText('{}'.format(load_dict['Function6']))
                
                if load_dict['G_File']=="True":
                    self.checkBox_file.setChecked(True)
                else:
                    self.checkBox_file.setChecked(False)
                if load_dict['Browser_V']=="True":
                    self.checkBox_browser.setChecked(True)
                else:
                    self.checkBox_browser.setChecked(False)

                self.checkBox_address_link.setChecked(True)

                print("Hi,{}  欢迎使用 Auto_LZ !". format(load_dict['username'].split('.')[0]))
            
            else:
                print("配置文件 Auto_LZ.json 需要更新")
        
        else:
            print("配置文件 Auto_LZ.json 不存在！")
        
        
    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        cursor = self.textEdit_p_info.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.textEdit_p_info.setTextCursor(cursor)
        self.textEdit_p_info.ensureCursorVisible()
    
    def errorOutputWritten(self, text):
        """Append text to the QTextEdit."""
        cursor = self.textEdit_e_info.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.textEdit_e_info.setTextCursor(cursor)
        self.textEdit_e_info.ensureCursorVisible()
    
    def btnstate_S(self, btn):
        global Skip
        if btn.isChecked() == True:
            Skip = "No"
        else:
            Skip ="Yes"

    @pyqtSlot()
    def on_lineEdit_username_editingFinished(self):
        global Theadalive, load_dict
        if Theadalive == 1:
            pass
        else:
            if self.lineEdit_username.text() != load_dict['username']:
                self.textEdit_p_info.clear()
                print("Hi,{}  欢迎使用 Auto_LZ !". format(self.lineEdit_username.text().split('.')[0])) 
 
    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        global Skip, Info_list,  load_dict, Theadalive, button_end_st
        button_end_st = 0
        self.pushButton_start.setText("正在分析")
        self.pushButton_start.setEnabled(False)
        self.pushButton_end.setEnabled(True)
        self.pushButton_end.setText("暂停分析")

        self.Save_Auto_LZ_Info()

        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = EmittingStream(textWritten=self.errorOutputWritten)

        self.workThread=WorkThread()
        self.workThread.start()
        Theadalive = 1
        self.workThread.trigger_end.connect(self.Auto_LZ_Stop)

    @pyqtSlot()
    def on_pushButton_end_clicked(self):
        global button_end_st
        if button_end_st==0:
            button_end_st = 1
            self.pushButton_end.setText("继续分析")
            self.pushButton_start.setEnabled(True)
            self.pushButton_start.setText("开始分析")
            if self.workThread.handle == -1:
                return print('handle is wrong')
            ret = SuspendThread(self.workThread.handle)
            print('\n分析已中断，继续分析请点击－继续分析，重新开始请点击－开始分析',  ret)
        elif button_end_st==1:
            button_end_st = 0
            self.pushButton_start.setText("正在分析")
            self.pushButton_start.setEnabled(False)
            self.pushButton_end.setText("暂停分析")
            if self.workThread.handle == -1:
                return print('handle is wrong')
            ret = ResumeThread(self.workThread.handle)
            print('分析继续……',  ret)
            
    @pyqtSlot()
    def on_pushButton_edit_clicked(self):
        dialog = Dialog(self)
        dialog.show()
        dialog.dialogSignal.connect(self.subwindow)
        
    def subwindow(self, flag,  dict):
        global load_dict
        if flag==1:
            print("\n车辆编辑成功")
            self.comboBox_Veh.clear()
            self.comboBox_Veh.addItems(list(dict.keys()))
            load_dict['vin'] =  dict
        else:
            print("\n车辆编辑取消")
            
    @pyqtSlot()
    def on_pushButton_address_setting_clicked(self):
        dialog = Dialog_Address_Setting(self)
        dialog.show()
        dialog.dialog_AS_Signal.connect(self.subwindow_as)

    def subwindow_as(self, flag):
        global load_dict
        if flag==1:
            print("\n地址配置成功")
            with open('Auto_LZ.json', 'r') as load_f:
                load_dict = json.load(load_f)
        else:
            print("\n取消配置地址")
    
    @pyqtSlot()
    def on_lineEdit_key_words1_editingFinished(self):
        global load_dict
        if self.checkBox_address_link.isChecked():
            key_list = list(load_dict['Match'].keys())
            address_list = list(load_dict['Match'].values())
            key = self.lineEdit_key_words1.text()
            for i in range(8):
                if len(key_list[i])>0:
                    if key_list[i] in key:
                        self.lineEdit_Zep_Address1.setText(address_list[i])

    @pyqtSlot()
    def on_lineEdit_key_words2_editingFinished(self):
        global load_dict
        if self.checkBox_address_link.isChecked():
            key_list = list(load_dict['Match'].keys())
            address_list = list(load_dict['Match'].values())
            key = self.lineEdit_key_words2.text()
            for i in range(8):
                if len(key_list[i])>0:
                    if key_list[i] in key:
                        self.lineEdit_Zep_Address2.setText(address_list[i])
        
    @pyqtSlot()
    def on_lineEdit_key_words3_editingFinished(self):
        global load_dict
        if self.checkBox_address_link.isChecked():
            key_list = list(load_dict['Match'].keys())
            address_list = list(load_dict['Match'].values())
            key = self.lineEdit_key_words3.text()
            for i in range(8):
                if len(key_list[i])>0:
                    if key_list[i] in key:
                        self.lineEdit_Zep_Address3.setText(address_list[i])
                    
    @pyqtSlot()
    def on_lineEdit_key_words4_editingFinished(self):
        global load_dict
        if self.checkBox_address_link.isChecked():
            key_list = list(load_dict['Match'].keys())
            address_list = list(load_dict['Match'].values())
            key = self.lineEdit_key_words4.text()
            for i in range(8):
                if len(key_list[i])>0:
                    if key_list[i] in key:
                        self.lineEdit_Zep_Address4.setText(address_list[i])

    @pyqtSlot()
    def on_lineEdit_key_words5_editingFinished(self):
        global load_dict
        if self.checkBox_address_link.isChecked():
            key_list = list(load_dict['Match'].keys())
            address_list = list(load_dict['Match'].values())
            key = self.lineEdit_key_words5.text()
            for i in range(8):
                if len(key_list[i])>0:
                    if key_list[i] in key:
                        self.lineEdit_Zep_Address5.setText(address_list[i])
        
    @pyqtSlot()
    def on_lineEdit_key_words6_editingFinished(self):
        global load_dict
        if self.checkBox_address_link.isChecked():
            key_list = list(load_dict['Match'].keys())
            address_list = list(load_dict['Match'].values())
            key = self.lineEdit_key_words6.text()
            for i in range(8):
                if len(key_list[i])>0:
                    if key_list[i] in key:
                        self.lineEdit_Zep_Address6.setText(address_list[i])



    def Save_Auto_LZ_Info(self):
        global load_dict, Info_list
        password_r = self.lineEdit_password.text()
        password_en = base64.b64encode('{}'.format(password_r).encode('utf-8'))
        password_str = str(password_en, 'utf-8')
        load_dict['username']=self.lineEdit_username.text()
        load_dict['password'] = password_str
        load_dict['Veh']=self.comboBox_Veh.currentText()
        load_dict['start_date']=self.lineEdit_start_date.text()
        load_dict['end_date']=self.lineEdit_end_date.text()
        load_dict['key_words1']=self.lineEdit_key_words1.text()
        load_dict['Zep_Address1']=self.lineEdit_Zep_Address1.text()
        load_dict['Function1']=self.comboBox_Fun1.currentText()
        load_dict['key_words2']=self.lineEdit_key_words2.text()
        load_dict['Zep_Address2']=self.lineEdit_Zep_Address2.text()
        load_dict['Function2']=self.comboBox_Fun2.currentText()
        load_dict['key_words3']=self.lineEdit_key_words3.text()
        load_dict['Zep_Address3']=self.lineEdit_Zep_Address3.text()
        load_dict['Function3']=self.comboBox_Fun3.currentText()
        load_dict['key_words4']=self.lineEdit_key_words4.text()
        load_dict['Zep_Address4']=self.lineEdit_Zep_Address4.text()
        load_dict['Function4']=self.comboBox_Fun4.currentText()
        load_dict['key_words5']=self.lineEdit_key_words5.text()
        load_dict['Zep_Address5']=self.lineEdit_Zep_Address5.text()
        load_dict['Function5']=self.comboBox_Fun5.currentText()
        load_dict['key_words6']=self.lineEdit_key_words6.text()
        load_dict['Zep_Address6']=self.lineEdit_Zep_Address6.text()
        load_dict['Function6']=self.comboBox_Fun6.currentText()   
        load_dict['Skip']=Skip
        load_dict['G_File']=str(self.checkBox_file.isChecked())
        load_dict['Browser_V']=str(self.checkBox_browser.isChecked())
        Info_list = list(load_dict.values())[:26]
        Info_list[1]=password_r
        Info_list.append(str(load_dict['vin']))

        with open('Auto_LZ.json', 'w') as f:
            json.dump(load_dict, f, indent=4)


    def Auto_LZ_Stop(self):
        global Theadalive
        Theadalive = 0
        print("\nAuto_LZ 本次分析结束!")
        print("----------------------------------------\n")
        self.pushButton_start.setEnabled(True)
        self.pushButton_start.setText("开始分析")
        self.pushButton_end.setEnabled(False)

    def closeEvent(self, event):
        global _console_        
        sys.stdout=_console_
        Browser_Close()
        self.Save_Auto_LZ_Info()
        

class EmittingStream(QObject):
    textWritten = pyqtSignal(str)
    def write(self, text):
        self.textWritten.emit(str(text)) 


class WorkThread(QThread):
    trigger_end = pyqtSignal()
    handle = -1

    def __init__(self):
        super(WorkThread,  self).__init__()
    
    def run(self):
        global Info_list, Process_Info, Issue_Info

        try:
            self.handle = ctypes.windll.kernel32.OpenThread(win32con.PROCESS_ALL_ACCESS, False, int(QThread.currentThreadId()))
        except Exception as e:
            print('get thread handle failed', e)

        try:
            Auto_LZ_Main(Info_list)
        except Exception as e:
            print("\n出错啦，快去报错信息里看看什么原因, 有问题请联系pandeng.duan@nio.com")
            sys.stdout = Issue_Info
            time.sleep(1)
            print(e)
            sys.stdout = Process_Info
        self.trigger_end.emit()






if __name__=="__main__":
    app = QApplication(sys.argv)
    _console_=sys.stdout
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
