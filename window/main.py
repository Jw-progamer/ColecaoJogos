from PyQt5.QtWidgets import QMainWindow
from asserts.ui_main import Ui_MainWindow
from window.plataforms import AddPlataformDialog, ViewPlataform
from window.games import AddGameDialog, ViewGameDialog, DeleteGame
from window.About import About

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionAdicionar_plataforma.triggered.connect(self.actionAddPlataform)
        self.ui.actionVisualizar_Plataforma.triggered.connect(self.actionViewPlataform)

        self.ui.actionAdicionar_Jogo.triggered.connect(self.actonAddGame)
        self.ui.actionVisualizar_jogos.triggered.connect(self.actionViewGame)
        self.ui.actionExcluir_jogos.triggered.connect(self.actionDeleteGame)

        self.ui.actionsobre.triggered.connect(self.actionAbout)

    def actionAddPlataform(self):
        dialog = AddPlataformDialog()
        dialog.show()
        dialog.exec_()

    def actionViewPlataform(self):
        dialog= ViewPlataform()
        dialog.show()
        dialog.exec_()

    def actonAddGame(self):
        dialog = AddGameDialog()
        dialog.show()
        dialog.exec_()

    def actionViewGame(self):
        dialog = ViewGameDialog()
        dialog.show()
        dialog.exec_()

    def actionDeleteGame(self):
        dialog = DeleteGame()
        dialog.show()
        dialog.exec_()

    def actionAbout(self):
        dialog = About()
        dialog.show()
        dialog.exec_()