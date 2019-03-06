# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\4_SW_Tool\SW_Project\Python\GUI\Display\ChangeStyle.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChangeStyleForm(object):
    def setupUi(self, ChangeStyleForm):
        ChangeStyleForm.setObjectName("ChangeStyleForm")
        ChangeStyleForm.resize(306, 92)
        self.label = QtWidgets.QLabel(ChangeStyleForm)
        self.label.setGeometry(QtCore.QRect(30, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ChangeStylecomboBox = QtWidgets.QComboBox(ChangeStyleForm)
        self.ChangeStylecomboBox.setGeometry(QtCore.QRect(120, 30, 141, 25))
        self.ChangeStylecomboBox.setObjectName("ChangeStylecomboBox")
        self.ChangeStyleAction = QtWidgets.QAction(ChangeStyleForm)
        self.ChangeStyleAction.setObjectName("ChangeStyleAction")

        self.retranslateUi(ChangeStyleForm)
        QtCore.QMetaObject.connectSlotsByName(ChangeStyleForm)

    def retranslateUi(self, ChangeStyleForm):
        _translate = QtCore.QCoreApplication.translate
        ChangeStyleForm.setWindowTitle(_translate("ChangeStyleForm", "Form"))
        self.label.setText(_translate("ChangeStyleForm", "Set Style:"))
        self.ChangeStyleAction.setText(_translate("ChangeStyleForm", "Changestyle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangeStyleForm = QtWidgets.QWidget()
    ui = Ui_ChangeStyleForm()
    ui.setupUi(ChangeStyleForm)
    ChangeStyleForm.show()
    sys.exit(app.exec_())

