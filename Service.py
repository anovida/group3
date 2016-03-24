# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Service.ui'
#
# Created: Wed Mar 23 10:38:33 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BuildingServicesClient(object):
    def setupUi(self, BuildingServicesClient):
        BuildingServicesClient.setObjectName(_fromUtf8("BuildingServicesClient"))
        BuildingServicesClient.resize(423, 130)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(12)
        BuildingServicesClient.setFont(font)
        self.roomLabel = QtGui.QLabel(BuildingServicesClient)
        self.roomLabel.setGeometry(QtCore.QRect(8, 30, 36, 20))
        self.roomLabel.setObjectName(_fromUtf8("roomLabel"))
        self.roomEdit = QtGui.QLineEdit(BuildingServicesClient)
        self.roomEdit.setGeometry(QtCore.QRect(50, 30, 150, 26))
        self.roomEdit.setObjectName(_fromUtf8("roomEdit"))
        self.dateLabel = QtGui.QLabel(BuildingServicesClient)
        self.dateLabel.setGeometry(QtCore.QRect(210, 31, 27, 20))
        self.dateLabel.setObjectName(_fromUtf8("dateLabel"))
        self.dateEdit = QtGui.QDateTimeEdit(BuildingServicesClient)
        self.dateEdit.setGeometry(QtCore.QRect(240, 30, 175, 26))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.responseLabel = QtGui.QLabel(BuildingServicesClient)
        self.responseLabel.setGeometry(QtCore.QRect(7, 63, 62, 20))
        self.responseLabel.setObjectName(_fromUtf8("responseLabel"))
        self.bookButton = QtGui.QPushButton(BuildingServicesClient)
        self.bookButton.setGeometry(QtCore.QRect(58, 90, 75, 28))
        self.bookButton.setObjectName(_fromUtf8("bookButton"))
        self.unBookButton = QtGui.QPushButton(BuildingServicesClient)
        self.unBookButton.setGeometry(QtCore.QRect(139, 90, 75, 28))
        self.unBookButton.setObjectName(_fromUtf8("unBookButton"))
        self.quitButton = QtGui.QPushButton(BuildingServicesClient)
        self.quitButton.setGeometry(QtCore.QRect(220, 90, 75, 28))
        self.quitButton.setObjectName(_fromUtf8("quitButton"))

        self.retranslateUi(BuildingServicesClient)
        QtCore.QMetaObject.connectSlotsByName(BuildingServicesClient)

    def retranslateUi(self, BuildingServicesClient):
        BuildingServicesClient.setWindowTitle(_translate("BuildingServicesClient", "Form", None))
        self.roomLabel.setText(_translate("BuildingServicesClient", "Room", None))
        self.dateLabel.setText(_translate("BuildingServicesClient", "Date", None))
        self.responseLabel.setText(_translate("BuildingServicesClient", "Response", None))
        self.bookButton.setText(_translate("BuildingServicesClient", "Book", None))
        self.unBookButton.setText(_translate("BuildingServicesClient", "Unbook", None))
        self.quitButton.setText(_translate("BuildingServicesClient", "Quit", None))

