# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_plataform.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(543, 385)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
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
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.btnAdd = QtWidgets.QPushButton(Dialog)
        self.btnAdd.setObjectName("btnAdd")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btnAdd)
        self.gridLayout.addLayout(self.formLayout, 0, 2, 1, 1)
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)
        self.btnSair = QtWidgets.QPushButton(Dialog)
        self.btnSair.setObjectName("btnSair")
        self.gridLayout.addWidget(self.btnSair, 1, 0, 1, 1)
        self.btnEditar = QtWidgets.QPushButton(Dialog)
        self.btnEditar.setObjectName("btnEditar")
        self.gridLayout.addWidget(self.btnEditar, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Visualizar Plataforma"))
        self.label.setText(_translate("Dialog", "Nome da Plataforma:"))
        self.label_2.setText(_translate("Dialog", "Imagem da plataforma:"))
        self.label_4.setText(_translate("Dialog", "lAdicionar imagem:"))
        self.btnAdd.setText(_translate("Dialog", "adicionar imagem"))
        self.btnSair.setText(_translate("Dialog", "Sair"))
        self.btnEditar.setText(_translate("Dialog", "Editar informações"))

