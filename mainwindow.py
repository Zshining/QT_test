# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from dialog import Ui_Dialog
from form import Ui_Form
from dialog import Ui_Dialog
from mesbox import MessageBox
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 452)
        palette1 = QtGui.QPalette()
        palette1.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap('images/bg3.jpg')))   # 设置背景图片
        MainWindow.setPalette(palette1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(440, 240, 167, 21))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit.setAccessibleName("")
        self.lineEdit.setAutoFillBackground(True)
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 280, 167, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(470, 320, 91, 31))
        self.login.setAutoDefault(False)
        self.login.setObjectName("login")
        self.register_2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_2.setGeometry(QtCore.QRect(630, 240, 75, 23))
        self.register_2.setObjectName("register_2")
        self.getpass = QtWidgets.QPushButton(self.centralwidget)
        self.getpass.setGeometry(QtCore.QRect(630, 280, 75, 23))
        self.getpass.setObjectName("getpass")
        #self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        #self.graphicsView.setGeometry(QtCore.QRect(0, 0, 431, 431))
        #self.graphicsView.setStyleSheet("border-image: url(images/bg.jpg);")
        #self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #self.register_2.clicked.connect(self.centralwidget.hide)
        #self.login2()
        self.login.clicked.connect(self.login2)
        self.dia = Ui_Dialog2()
        self.register_2.clicked.connect(self.dia.show)
        #self.form = Ui_Form2()
        #self.login.clicked.connect(self.form.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def login2(self):
        account = self.lineEdit.text()
        passwd = self.lineEdit_2.text()
        print(account, passwd)
        if passwd == '123':
            MainWindow.close()
            self.form = Ui_Form2()
            self.form.show()
        else:
            self.mes = MessageBox()
            self.mes.selectWarning()
            self.lineEdit_2.setFocus()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "测试工具"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "              用户名"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "               密码"))
        self.login.setText(_translate("MainWindow", "登录"))
        self.register_2.setText(_translate("MainWindow", "注册"))
        self.getpass.setText(_translate("MainWindow", "找回密码"))

class Ui_Form2(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Ui_Form2,self).__init__()
        self.setupUi(self)

class Ui_Dialog2(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(Ui_Dialog2,self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #Dialog = QtWidgets.QDialog()
    #ui2 = Ui_Dialog()
    #ui2.setupUi(Dialog)
    #ui.register_2.clicked.connect(Dialog.show)
    sys.exit(app.exec_())

