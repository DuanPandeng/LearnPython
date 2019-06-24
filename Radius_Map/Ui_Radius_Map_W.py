# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\4_SW_Tool\SW_Project\Python\GUI\Radius_Map\Radius_Map_W.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(625, 550)
        Dialog.setSizeGripEnabled(True)
        self.pushButton_display = QtWidgets.QPushButton(Dialog)
        self.pushButton_display.setGeometry(QtCore.QRect(500, 210, 93, 28))
        self.pushButton_display.setObjectName("pushButton_display")
        self.textEdit_display = QtWidgets.QTextEdit(Dialog)
        self.textEdit_display.setGeometry(QtCore.QRect(30, 380, 441, 151))
        self.textEdit_display.setObjectName("textEdit_display")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 441, 191))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.comboBox_dir = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_dir.setGeometry(QtCore.QRect(330, 110, 91, 22))
        self.comboBox_dir.setCurrentText("")
        self.comboBox_dir.setObjectName("comboBox_dir")
        self.comboBox_speed = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_speed.setGeometry(QtCore.QRect(30, 110, 101, 21))
        self.comboBox_speed.setObjectName("comboBox_speed")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(190, 90, 72, 15))
        self.label_2.setObjectName("label_2")
        self.comboBox_radius = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_radius.setGeometry(QtCore.QRect(180, 110, 101, 22))
        self.comboBox_radius.setObjectName("comboBox_radius")
        self.checkBox_all = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_all.setGeometry(QtCore.QRect(40, 150, 141, 19))
        self.checkBox_all.setObjectName("checkBox_all")
        self.label_dir = QtWidgets.QLabel(self.groupBox)
        self.label_dir.setGeometry(QtCore.QRect(330, 90, 81, 16))
        self.label_dir.setObjectName("label_dir")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 90, 72, 15))
        self.label.setObjectName("label")
        self.pushButton_add_file = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_add_file.setGeometry(QtCore.QRect(30, 40, 81, 25))
        self.pushButton_add_file.setObjectName("pushButton_add_file")
        self.lineEdit_add_file = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_add_file.setGeometry(QtCore.QRect(120, 40, 301, 25))
        self.lineEdit_add_file.setObjectName("lineEdit_add_file")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 240, 441, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_lon = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_lon.setGeometry(QtCore.QRect(160, 30, 201, 25))
        self.lineEdit_lon.setObjectName("lineEdit_lon")
        self.lineEdit_lat = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_lat.setGeometry(QtCore.QRect(160, 70, 201, 25))
        self.lineEdit_lat.setObjectName("lineEdit_lat")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(70, 30, 72, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(70, 70, 72, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_display.setText(_translate("Dialog", "Display"))
        self.groupBox.setTitle(_translate("Dialog", "多点显示:"))
        self.label_2.setText(_translate("Dialog", "Radius:"))
        self.checkBox_all.setText(_translate("Dialog", "显示所有的点"))
        self.label_dir.setText(_translate("Dialog", "Direction:"))
        self.label.setText(_translate("Dialog", "Speed:"))
        self.pushButton_add_file.setText(_translate("Dialog", "加载数据"))
        self.groupBox_2.setTitle(_translate("Dialog", "单点显示:"))
        self.label_3.setText(_translate("Dialog", "经度："))
        self.label_4.setText(_translate("Dialog", "纬度："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

