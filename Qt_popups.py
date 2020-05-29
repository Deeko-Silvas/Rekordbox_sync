from PyQt5 import QtWidgets

class Popups:
    def __init__(self, title, message):
        self.title = title
        self.message = message

    def message_box(self):
        self.app = QtWidgets.QMessageBox()
        self.app.setWindowTitle(self.title)
        self.app.setText(self.message)
        self.app.exec()