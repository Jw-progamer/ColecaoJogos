# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_game.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 340)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtNome = QtWidgets.QLineEdit(Dialog)
        self.txtNome.setObjectName("txtNome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtNome)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.completeDBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.completeDBox.setObjectName("completeDBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.completeDBox)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.labelImage = QtWidgets.QLabel(Dialog)
        self.labelImage.setText("")
        self.labelImage.setObjectName("labelImage")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelImage)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Adicionar Jogo"))
        self.label.setText(_translate("Dialog", "Nome do jogo:"))
        self.label_2.setText(_translate("Dialog", "Completude do jogo:"))
        self.label_3.setText(_translate("Dialog", "Gostaria de adicionar sua capa:"))
        self.pushButton.setText(_translate("Dialog", "Adicionar uma capa"))
        self.label_4.setText(_translate("Dialog", "Capa:"))

