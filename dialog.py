# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter,QPixmap

class Ui_Dialog(object):
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("./images/bg2.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 358)
        #palette1 = QtGui.QPalette()
        #palette1.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap('images/bg2.jpg')))
        #Dialog.setPalette(palette1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 40, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 80, 113, 21))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 120, 113, 21))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.confirm = QtWidgets.QPushButton(Dialog)
        self.confirm.setGeometry(QtCore.QRect(70, 280, 88, 23))
        self.confirm.setObjectName("confirm")
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setGeometry(QtCore.QRect(230, 280, 88, 23))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(Dialog)
        self.cancel.clicked.connect(Dialog.close)
        self.confirm.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "注册"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "    用户名"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "     密码"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "   确认密码"))
        self.confirm.setText(_translate("Dialog", "确认"))
        self.cancel.setText(_translate("Dialog", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

