# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from messageForm import MessageDialog

class Ui_Dialog(object):
    def __init__(self, message):
        self.message = message

    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.login, self.password, self.server = self.textEdit.toPlainText(), self.textEdit_2.toPlainText(), self.message
        self.ui = MessageDialog(self.login, self.password, self.server)
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 109)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 55, 31))
        self.label_2.setObjectName("label_2")
        self.next = QtWidgets.QPushButton(Dialog)
        self.next.setGeometry(QtCore.QRect(420, 70, 61, 28))
        self.next.setObjectName("next")
        self.next.clicked.connect(self.openWindow)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(190, 10, 201, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 40, 201, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Username, email, or mobile"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.next.setText(_translate("Dialog", ">"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())