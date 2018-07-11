from PyQt5.QtWidgets import QDialog
from asserts.ui_abort import Ui_Dialog

class About(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btnSair.clicked.connect(self.close)