# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'part2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(671, 425)
        Dialog.setStyleSheet("background-color:rgb(43, 209, 255)\n"
"\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imgLabel = QtWidgets.QLabel(Dialog)
        self.imgLabel.setAutoFillBackground(False)
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.verticalLayout.addWidget(self.imgLabel)
        self.showBtn = QtWidgets.QPushButton(Dialog)
        self.showBtn.setToolTipDuration(0)
        self.showBtn.setStyleSheet("color:rgb(0, 0, 0); font: 75 10pt \"MS Shell Dlg 2\"; \n"
"font: 10pt \"Times New Roman\";")
        self.showBtn.setObjectName("showBtn")
        self.verticalLayout.addWidget(self.showBtn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gesture Recognition and Control App V1"))
        self.showBtn.setText(_translate("Dialog", "Show"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
