# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PDF_Toolchain_about_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.resize(402, 293)
        self.centralwidget = QtWidgets.QWidget(AboutWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 391, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 41, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 210, 41, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(140, 210, 41, 41))
        self.label_7.setObjectName("label_7")
        AboutWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AboutWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 21))
        self.menubar.setObjectName("menubar")
        AboutWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AboutWindow)
        self.statusbar.setObjectName("statusbar")
        AboutWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "PDF Toolchain"))
        self.label.setText(_translate("AboutWindow", " ___                  __  __       _\n"
"|_ _|___ ___  _ __   |  \\/  | __ _| | _____ _ __\n"
" | |/ __/ _ \\| '_ \\  | |\\/| |/ _` | |/ / _ \\ '__|\n"
" | | (_| (_) | | | | | |  | | (_| |   <  __/ |\n"
"|___\\___\\___/|_| |_| |_|  |_|\\__,_|_|\\_\\___|_|\n"
" "))
        self.label_2.setText(_translate("AboutWindow", "V 1.2"))
        self.label_3.setText(_translate("AboutWindow", "Автор программы:"))
        self.label_4.setText(_translate("AboutWindow", "   ____             _             _ _     ____  _  _\n"
"  / __ \\  __ _ _ __| |_ _ __ ___ (_) |__ |___ \\| || |\n"
" / / _` |/ _` | \'__| __| \'_ ` _ \\| | \'_ \\  __) | || |_\n"
"| | (_| | (_| | |  | |_| | | | | | | | | |/ __/|__   _|\n"
" \\ \\__,_|\\__,_|_|   \\__|_| |_| |_|_|_| |_|_____|  |_|\n"
"  \\____/"))
        self.label_5.setText(_translate("AboutWindow", "TextLabel"))
        self.label_6.setText(_translate("AboutWindow", "TextLabel"))
        self.label_7.setText(_translate("AboutWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutWindow = QtWidgets.QMainWindow()
    ui = Ui_AboutWindow()
    ui.setupUi(AboutWindow)
    AboutWindow.show()
    sys.exit(app.exec_())
