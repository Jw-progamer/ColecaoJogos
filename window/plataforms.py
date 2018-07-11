from PyQt5.QtWidgets import QDialog
from asserts.ui_addPlataform import Ui_Dialog
from asserts.ui_viewPlataform import Ui_Dialog as Ui_View

class AddPlataformDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class ViewPlataform(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_View()
        self.ui.setupUi(self)