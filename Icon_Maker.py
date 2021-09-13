from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from Icon_Maker_window import Ui_MainWindow
from Icon_Maker_about import about_window
from Icon_Maker_LineEdit import *
from PIL import Image
import sys, os
import Icon_Maker_Icon as icon

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.icon_data = icon.Get_icon(icon.icon_str)
        self.setWindowIcon(self.icon_data)
        self.setGeometry(810, 400, 291, 149)
        self.setStyleSheet('QMainWindow {background-color: white;}')
        self.about_window = about_window()
        m = self.menuBar().addMenu("Меню")
        a = m.addAction("О программе")
        a.triggered.connect(self.aboutClicked)
        self.ui.lineEdit = MyLineEdit(self.ui.lineEdit)
        self.ui.lineEdit.setFixedHeight(40)
        self.ui.gridLayout.addWidget(self.ui.lineEdit, 1, 0, 1, 2)
        #self.ui.lineEdit.setReadOnly(True)
        self.ui.lineEdit.textChanged.connect(self.FilePathEntered)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton.clicked.connect(self.SelectButtonClicked)
        self.ui.pushButton_2.clicked.connect(self.CreateICOButtonClicked)

    def CreateICOButtonClicked(self):
        s = QMessageBox()
        s.setWindowIcon(self.icon_data)
        InputImageName = self.ui.lineEdit.text()
        TempICOName = '.'.join(InputImageName.split('.')[:-1]) + ".ico"
        try:
            OutputICOName = QFileDialog.getSaveFileName(self, "Сохранить значок (.ico)", TempICOName, "Значок ICO (*.ico)")[0]
        except:
            QMessageBox.critical(s, "Icon Maker", f"Не выбран путь для сохранения файла.\nОперация прервана", QMessageBox.Ok)
        else:
            try:
                #ICO = Image.open(r'{}'.format(InputImageName))
                ICO = Image.open(InputImageName)
            except:
                if os.path.exists(InputImageName) == True:
                    QMessageBox.critical(s, "Icon Maker", f"Файл {InputImageName} повреждён.\nОперация прервана", QMessageBox.Ok)
                else:
                    QMessageBox.critical(s, "Icon Maker", f"Файл {InputImageName} не существует.\nОперация прервана", QMessageBox.Ok)
            else:
                try:
                    ICO.save(OutputICOName, format='ICO', sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (255, 255)])
                except:
                    QMessageBox.critical(s, "Icon Maker", f"Не удалось сохранить файл {OutputICOName}.\nОперация прервана", QMessageBox.Ok)
                else:
                    QMessageBox.information(s, "Icon Maker", f"Значок {OutputICOName} успешно создан!", QMessageBox.Ok)

    def SelectButtonClicked(self):
        InputImageName = QFileDialog.getOpenFileName(self, "Выбрать изображение", "/home", "Все типы изображений (*.jpg *.jpeg *.jpe *.jfif *.png *.bmp *.gif);; Изображение JPEG (*.jpg *.jpeg *.jpe *.jfif);; Изображение PNG (*.png);; Изображение BMP (*.bmp);; Изображение GIF (*.gif)")[0]
        self.ui.lineEdit.setText(InputImageName)
        if self.ui.lineEdit.text() != "": self.ui.pushButton_2.setEnabled(True)
        else: self.ui.pushButton_2.setEnabled(False)

    def aboutClicked(self):
        self.about_window.show()
        """
        q = QMessageBox()
        q.setWindowIcon(self.icon_data)
        q.setStyleSheet('QMessageBox {background-color: white; font-family: Consolas; font-size: 13px;}')
        #q.setStyleSheet('QMessageBox {background-color: white; font-family: Consolas;}')
        QMessageBox.about(q, "О программе", '''Icon Maker 1.0\n
Автор программы:\n
   ____             _             _ _     ____  _  _
  / __ \  __ _ _ __| |_ _ __ ___ (_) |__ |___ \| || |
 / / _` |/ _` | '__| __| '_ ` _ \| | '_ \  __) | || |_
| | (_| | (_| | |  | |_| | | | | | | | | |/ __/|__   _|
 \ \__,_|\__,_|_|   \__|_| |_| |_|_|_| |_|_____|  |_|
  \____/''')"""

    def FilePathEntered(self):
        if self.ui.lineEdit.text() != "": self.ui.pushButton_2.setEnabled(True)
        else: self.ui.pushButton_2.setEnabled(False)

    def closeEvent(self, e):
        self.about_window.close()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())