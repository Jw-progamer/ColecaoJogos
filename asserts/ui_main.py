# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menuarquivo = QtWidgets.QMenu(self.menubar)
        self.menuarquivo.setObjectName("menuarquivo")
        self.menuplataformas = QtWidgets.QMenu(self.menubar)
        self.menuplataformas.setObjectName("menuplataformas")
        self.menuJogos = QtWidgets.QMenu(self.menubar)
        self.menuJogos.setObjectName("menuJogos")
        self.menuajuda = QtWidgets.QMenu(self.menubar)
        self.menuajuda.setObjectName("menuajuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNovo_Arquivo = QtWidgets.QAction(MainWindow)
        self.actionNovo_Arquivo.setObjectName("actionNovo_Arquivo")
        self.actionAbrir_Arquivo = QtWidgets.QAction(MainWindow)
        self.actionAbrir_Arquivo.setObjectName("actionAbrir_Arquivo")
        self.actionBackup_Arquivo = QtWidgets.QAction(MainWindow)
        self.actionBackup_Arquivo.setObjectName("actionBackup_Arquivo")
        self.actionAdicionar_plataforma = QtWidgets.QAction(MainWindow)
        self.actionAdicionar_plataforma.setObjectName("actionAdicionar_plataforma")
        self.actionVisualizar_Plataforma = QtWidgets.QAction(MainWindow)
        self.actionVisualizar_Plataforma.setObjectName("actionVisualizar_Plataforma")
        self.actionAdicionar_Jogo = QtWidgets.QAction(MainWindow)
        self.actionAdicionar_Jogo.setObjectName("actionAdicionar_Jogo")
        self.actionVisualizar_jogos = QtWidgets.QAction(MainWindow)
        self.actionVisualizar_jogos.setObjectName("actionVisualizar_jogos")
        self.actionExcluir_jogos = QtWidgets.QAction(MainWindow)
        self.actionExcluir_jogos.setObjectName("actionExcluir_jogos")
        self.actionsobre = QtWidgets.QAction(MainWindow)
        self.actionsobre.setObjectName("actionsobre")
        self.menuarquivo.addAction(self.actionNovo_Arquivo)
        self.menuarquivo.addAction(self.actionAbrir_Arquivo)
        self.menuarquivo.addAction(self.actionBackup_Arquivo)
        self.menuplataformas.addAction(self.actionAdicionar_plataforma)
        self.menuplataformas.addAction(self.actionVisualizar_Plataforma)
        self.menuJogos.addAction(self.actionAdicionar_Jogo)
        self.menuJogos.addAction(self.actionVisualizar_jogos)
        self.menuJogos.addAction(self.actionExcluir_jogos)
        self.menuajuda.addAction(self.actionsobre)
        self.menubar.addAction(self.menuarquivo.menuAction())
        self.menubar.addAction(self.menuplataformas.menuAction())
        self.menubar.addAction(self.menuJogos.menuAction())
        self.menubar.addAction(self.menuajuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Coleção de consoles e jogos"))
        self.menuarquivo.setTitle(_translate("MainWindow", "&arquivo"))
        self.menuplataformas.setTitle(_translate("MainWindow", "p&lataformas"))
        self.menuJogos.setTitle(_translate("MainWindow", "&Jogos"))
        self.menuajuda.setTitle(_translate("MainWindow", "aj&uda"))
        self.actionNovo_Arquivo.setText(_translate("MainWindow", "&Novo Arquivo"))
        self.actionAbrir_Arquivo.setText(_translate("MainWindow", "&Abrir Arquivo"))
        self.actionBackup_Arquivo.setText(_translate("MainWindow", "&Backup Arquivo"))
        self.actionAdicionar_plataforma.setText(_translate("MainWindow", "&Adicionar Plataforma"))
        self.actionVisualizar_Plataforma.setText(_translate("MainWindow", "&Visualizar Plataforma"))
        self.actionAdicionar_Jogo.setText(_translate("MainWindow", "&Adicionar Jogo"))
        self.actionVisualizar_jogos.setText(_translate("MainWindow", "&Visualizar jogos"))
        self.actionExcluir_jogos.setText(_translate("MainWindow", "&Excluir jogos"))
        self.actionsobre.setText(_translate("MainWindow", "sobre]"))

