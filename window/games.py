from PyQt5.QtWidgets import QDialog
from asserts.ui_addGame import Ui_Dialog as Ui_add_game
from asserts.ui_viewGame import Ui_Dialog as Ui_view_game
from asserts.ui_deleteGame import Ui_Dialog as Ui_delete_game

class AddGameDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_add_game()
        self.ui.setupUi(self)

class ViewGameDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_view_game()
        self.ui.setupUi(self)

class DeleteGame(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_delete_game()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close)
