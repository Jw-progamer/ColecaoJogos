# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_platform.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(469, 352)
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
        self.btnImage = QtWidgets.QPushButton(Dialog)
        self.btnImage.setObjectName("btnImage")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btnImage)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.labelImg = QtWidgets.QLabel(Dialog)
        self.labelImg.setText("")
        self.labelImg.setObjectName("labelImg")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelImg)
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
        Dialog.setWindowTitle(_translate("Dialog", "Adicionar Plataforma"))
        self.label.setText(_translate("Dialog", "Nome da Plataforma:"))
        self.label_2.setText(_translate("Dialog", "Image para representa-lá:"))
        self.btnImage.setText(_translate("Dialog", "Adicionar Imagem"))
        self.label_3.setText(_translate("Dialog", "Imagem:"))

