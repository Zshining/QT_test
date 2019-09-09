#-*- coding:utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QMessageBox, QGridLayout, QLabel, QPushButton, QFrame

class MessageBox(QWidget):
    def __init__(self):       
        super(MessageBox,self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("MessageBox")
        self.setGeometry(1100,400,300,290)

        self.questionLabel = QLabel("Question:")
        self.questionLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.infoLabel = QLabel("Information:")
        self.infoLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.warningLabel = QLabel("Warning:")
        self.warningLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)



    def selectQuestion(self):
        button = QMessageBox.question(self,"Question","检测到程序有更新，是否安装最新版本？",
                                      QMessageBox.Ok|QMessageBox.Cancel,QMessageBox.Ok)

        if button == QMessageBox.Ok:
            self.resultLabel.setText("<h2>Question:<font color=red>  OK</font></h2>")
        elif button == QMessageBox.Cancel:
            self.resultLabel.setText("<h2>Question:<font color=red>  Cancel</font></h2>")
        else:
            return

    def selectInfo(self):
        QMessageBox.information(self,"Information","程序当前版本为V3.11")
        self.resultLabel.setText("Information")
        4
    def selectWarning(self):
        #button = QMessageBox.warning(self,"Warning","账号或密码错误!!!",
        #                              QMessageBox.Reset|QMessageBox.Help|QMessageBox.Cancel,QMessageBox.Reset)
        QMessageBox.warning(self,"Warning","账号或密码错误!!!")

        #if button == QMessageBox.Reset:
        #    self.resultLabel.setText("<h2>Warning:<font color=red>  Reset</font></h2>")
        #elif button == QMessageBox.Help:
        #    self.resultLabel.setText("<h2>Warning:<font color=red>  Help</font></h2>")
        #elif button == QMessageBox.Cancel:
        #    self.resultLabel.setText("<h2>Warning:<font color=red>  Cancel</font></h2>")
        #else:
        #    return

    def selectCritical(self):
        QMessageBox.critical(self,"Critical","服务器宕机！")
        self.resultLabel.setText("<h2><font color=red>Critical</font></h2>")