from PyQt5.QtWidgets import QApplication
from window.main import Main
import data.dataBinding as data
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    data.createDatabaseIfNotExists()
    main = Main()
    main.show()
    sys.exit(app.exec_())