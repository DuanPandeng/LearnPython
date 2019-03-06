# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\4_SW_Tool\SW_Project\Python\GUI\Display\Displayer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1167, 533)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.LoadFileButton = QtWidgets.QPushButton(self.centralWidget)
        self.LoadFileButton.setGeometry(QtCore.QRect(20, 30, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadFileButton.sizePolicy().hasHeightForWidth())
        self.LoadFileButton.setSizePolicy(sizePolicy)
        self.LoadFileButton.setObjectName("LoadFileButton")
        self.ShowDirBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.ShowDirBrowser.setGeometry(QtCore.QRect(20, 70, 361, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShowDirBrowser.sizePolicy().hasHeightForWidth())
        self.ShowDirBrowser.setSizePolicy(sizePolicy)
        self.ShowDirBrowser.setObjectName("ShowDirBrowser")
        self.DisplayButton = QtWidgets.QPushButton(self.centralWidget)
        self.DisplayButton.setGeometry(QtCore.QRect(420, 30, 93, 28))
        self.DisplayButton.setObjectName("DisplayButton")
        self.MatplotlibWidget_1 = MatplotlibWidget(self.centralWidget)
        self.MatplotlibWidget_1.setGeometry(QtCore.QRect(410, 60, 741, 431))
        self.MatplotlibWidget_1.setObjectName("MatplotlibWidget_1")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 130, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.InputSignalsBox = QtWidgets.QLineEdit(self.centralWidget)
        self.InputSignalsBox.setGeometry(QtCore.QRect(20, 170, 361, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputSignalsBox.sizePolicy().hasHeightForWidth())
        self.InputSignalsBox.setSizePolicy(sizePolicy)
        self.InputSignalsBox.setObjectName("InputSignalsBox")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 210, 361, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1167, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.ChangeStyleAction = QtWidgets.QAction(MainWindow)
        self.ChangeStyleAction.setObjectName("ChangeStyleAction")
        self.menuView.addAction(self.ChangeStyleAction)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.LoadFileButton, self.ShowDirBrowser)
        MainWindow.setTabOrder(self.ShowDirBrowser, self.InputSignalsBox)
        MainWindow.setTabOrder(self.InputSignalsBox, self.listWidget)
        MainWindow.setTabOrder(self.listWidget, self.DisplayButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LoadFileButton.setText(_translate("MainWindow", "File Load"))
        self.DisplayButton.setText(_translate("MainWindow", "Display"))
        self.label.setText(_translate("MainWindow", "Input signals"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.ChangeStyleAction.setText(_translate("MainWindow", "ChangeStyle"))

from MatplotlibWidget import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

