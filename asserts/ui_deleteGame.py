# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_game.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(587, 300)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.labelNome = QtWidgets.QLabel(Dialog)
        self.labelNome.setText("")
        self.labelNome.setObjectName("labelNome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelNome)
        self.labelCompleto = QtWidgets.QLabel(Dialog)
        self.labelCompleto.setText("")
        self.labelCompleto.setObjectName("labelCompleto")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelCompleto)
        self.labelCapa = QtWidgets.QLabel(Dialog)
        self.labelCapa.setText("")
        self.labelCapa.setObjectName("labelCapa")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelCapa)
        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Nome do Jogo:"))
        self.label_2.setText(_translate("Dialog", "Completudo do jogo:"))
        self.label_3.setText(_translate("Dialog", "Capa do jogo:"))
        self.pushButton.setText(_translate("Dialog", "Cancelar"))
        self.pushButton_2.setText(_translate("Dialog", "Deletar"))

