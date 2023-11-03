# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from rsa import RSA

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 165, 101, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.result)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 110, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 240, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 310, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 340, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 390, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 470, 47, 13))
        self.label_8.setObjectName("label_8")
        self.message = QtWidgets.QTextEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(110, 110, 441, 50))
        self.message.setObjectName("message")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 10, 161, 51))
        self.textEdit.setObjectName("textEdit")
        self.p1 = QtWidgets.QLineEdit(self.centralwidget)
        self.p1.setGeometry(QtCore.QRect(70, 210, 481, 20))
        self.p1.setObjectName("p1")
        self.q1 = QtWidgets.QLineEdit(self.centralwidget)
        self.q1.setGeometry(QtCore.QRect(70, 240, 481, 20))
        self.q1.setObjectName("q1")
        self.e1 = QtWidgets.QLineEdit(self.centralwidget)
        self.e1.setGeometry(QtCore.QRect(70, 270, 481, 20))
        self.e1.setObjectName("e1")
        self.d1 = QtWidgets.QLineEdit(self.centralwidget)
        self.d1.setGeometry(QtCore.QRect(70, 310, 481, 20))
        self.d1.setObjectName("d1")
        self.N1 = QtWidgets.QLineEdit(self.centralwidget)
        self.N1.setGeometry(QtCore.QRect(70, 340, 481, 20))
        self.N1.setObjectName("N1")
        self.enc1 = QtWidgets.QTextEdit(self.centralwidget)
        self.enc1.setGeometry(QtCore.QRect(70, 390, 481, 60))
        self.enc1.setObjectName("enc1")
        self.enc1.setReadOnly= True
        self.dec1 = QtWidgets.QLineEdit(self.centralwidget)
        self.dec1.setGeometry(QtCore.QRect(70, 470, 481, 20))
        self.dec1.setObjectName("dec1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
         

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Connect with app
    
    def result(self):
        self.rsa = RSA(keysize=40)
        msg = self.message.toPlainText()

        enc=self.rsa.encrypt(msg)
        dec = self.rsa.decrypt(enc)
        self.enc1.setText(str(enc))
        self.dec1.setText(str(dec))
        self.p1.setText(str(self.rsa.p))
        self.q1.setText(str(self.rsa.q))
        self.d1.setText(str(self.rsa.d))
        self.e1.setText(str(self.rsa.e))
        self.N1.setText(str(self.rsa.N))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))
        self.label.setText(_translate("MainWindow", "Message"))
        self.label_2.setText(_translate("MainWindow", "p"))
        self.label_3.setText(_translate("MainWindow", "q"))
        self.label_4.setText(_translate("MainWindow", "e"))
        self.label_5.setText(_translate("MainWindow", "d"))
        self.label_6.setText(_translate("MainWindow", "N"))
        self.label_7.setText(_translate("MainWindow", "Enc"))
        self.label_8.setText(_translate("MainWindow", "Dec"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">RSA</span></p></body></html>"))
    
        
    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
