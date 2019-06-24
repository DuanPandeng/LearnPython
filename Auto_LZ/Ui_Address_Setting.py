# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\4_SW_Tool\SW_Project\Python\GUI\Auto_LZ\Address_Setting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(662, 475)
        Dialog.setSizeGripEnabled(True)
        self.lineEdit_AS_keys_1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_keys_1.setGeometry(QtCore.QRect(50, 70, 111, 25))
        self.lineEdit_AS_keys_1.setObjectName("lineEdit_AS_keys_1")
        self.lineEdit_AS_keys_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_keys_2.setGeometry(QtCore.QRect(50, 110, 111, 25))
        self.lineEdit_AS_keys_2.setObjectName("lineEdit_AS_keys_2")
        self.lineEdit_AS_keys_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_keys_3.setGeometry(QtCore.QRect(50, 150, 111, 25))
        self.lineEdit_AS_keys_3.setObjectName("lineEdit_AS_keys_3")
        self.lineEdit_AS_keys_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_keys_4.setGeometry(QtCore.QRect(50, 190, 111, 25))
        self.lineEdit_AS_keys_4.setObjectName("lineEdit_AS_keys_4")
        self.lineEdit_AS_keys_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_keys_5.setGeometry(QtCore.QRect(50, 230, 111, 25))
        self.lineEdit_AS_keys_5.setObjectName("lineEdit_AS_keys_5")
        self.lineEdit_AS_keys_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_keys_6.setGeometry(QtCore.QRect(50, 270, 111, 25))
        self.lineEdit_AS_keys_6.setObjectName("lineEdit_AS_keys_6")
        self.lineEdit_AS_address1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_address1.setGeometry(QtCore.QRect(220, 70, 401, 25))
        self.lineEdit_AS_address1.setObjectName("lineEdit_AS_address1")
        self.lineEdit_AS_address2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_address2.setGeometry(QtCore.QRect(220, 110, 401, 25))
        self.lineEdit_AS_address2.setObjectName("lineEdit_AS_address2")
        self.lineEdit_AS_address3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_address3.setGeometry(QtCore.QRect(220, 150, 401, 25))
        self.lineEdit_AS_address3.setObjectName("lineEdit_AS_address3")
        self.lineEdit_AS_address4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_address4.setGeometry(QtCore.QRect(220, 190, 401, 25))
        self.lineEdit_AS_address4.setObjectName("lineEdit_AS_address4")
        self.lineEdit_AS_address5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_address5.setGeometry(QtCore.QRect(220, 230, 401, 25))
        self.lineEdit_AS_address5.setObjectName("lineEdit_AS_address5")
        self.lineEdit_AS_address6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_address6.setGeometry(QtCore.QRect(220, 270, 401, 25))
        self.lineEdit_AS_address6.setObjectName("lineEdit_AS_address6")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 121, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 181, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_AS_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_AS_save.setGeometry(QtCore.QRect(120, 410, 93, 28))
        self.pushButton_AS_save.setObjectName("pushButton_AS_save")
        self.pushButton_AS_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_AS_cancel.setGeometry(QtCore.QRect(320, 410, 93, 28))
        self.pushButton_AS_cancel.setObjectName("pushButton_AS_cancel")
        self.lineEdit_AS_keys_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_keys_7.setGeometry(QtCore.QRect(50, 310, 111, 25))
        self.lineEdit_AS_keys_7.setObjectName("lineEdit_AS_keys_7")
        self.lineEdit_AS_address7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_address7.setGeometry(QtCore.QRect(220, 310, 401, 25))
        self.lineEdit_AS_address7.setObjectName("lineEdit_AS_address7")
        self.lineEdit_AS_keys_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_keys_8.setGeometry(QtCore.QRect(50, 350, 111, 25))
        self.lineEdit_AS_keys_8.setObjectName("lineEdit_AS_keys_8")
        self.lineEdit_AS_address8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_AS_address8.setGeometry(QtCore.QRect(220, 350, 401, 25))
        self.lineEdit_AS_address8.setObjectName("lineEdit_AS_address8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "关键字字符设置："))
        self.label_2.setText(_translate("Dialog", "自动匹配的Zep地址设置："))
        self.pushButton_AS_save.setText(_translate("Dialog", "保存"))
        self.pushButton_AS_cancel.setText(_translate("Dialog", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

