from MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle
from rekordbox_client import Client
from rekordbox_server import Server
import sys
import win32api
from textwrap import wrap
import socket
import threading
import os


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.app = None
        self.await_connection_thread = None

        self.client_connection = Client()
        self.server_connection = Server()

        self.send_btn.clicked.connect(self.show_send)
        self.receive_btn.clicked.connect(self.show_receive)

        # disable previous connection radio until implemented
        self.previousRadio_2.setDisabled(True)

        self.actionExit.triggered.connect(self.close)

        # Get list of drives on current machine

        self.drivesComboBox_2.addItems(self.drives())

        self.networkRadio_2.toggled.connect(self.radio)
        self.ipRadio_2.toggled.connect(self.radio)
        self.nameRadio_2.toggled.connect(self.radio)
        self.previousRadio_2.toggled.connect(self.radio)

        self.connectionLbl_2.setText("No Connection")

        # buttons
        self.searchBtn_2.clicked.connect(self.search)
        self.connectBtn_2.clicked.connect(self.connect_server)

        self.disconnectBtn_2.clicked.connect(self.disconnect)
        self.audioBtn_2.clicked.connect(self.client_connection.audio)
        self.rbBtn_2.clicked.connect(lambda: self.client_connection.rekordbox_sync(str(self.drivesComboBox_2.currentText())))
        self.allBtn_2.clicked.connect(lambda: self.client_connection.all(str(self.drivesComboBox_2.currentText())))

        self.musicFolderBtn_2.clicked.connect(self.add_folder)

        # Set button statuses for program load (Disconnected state)
        self.button_state(True)

    def show_receive(self):
        self.start.hide()
        self.send.show()
        QtWidgets.qApp.processEvents()
        server_connect_thread = threading.Thread(target=self.server_connection.connect, args=())
        server_connect_thread.start()
        self.connectionLbl.setText("Waiting for connection")
        QtWidgets.qApp.processEvents()
        self.await_connection_thread = threading.Thread(target=self.await_connection, args=())
        self.await_connection_thread.start()

    def await_connection(self):
        while not self.server_connection.connection_confirmed:
            continue
        self.connectionLbl.setText(f"Connection has  been established! | IP {self.server_connection.address[0]} | "
                                   f"Port {str(self.server_connection.address[1])}")
        self.await_termination()

    def await_termination(self):
        while self.server_connection.connection_confirmed:
            continue
        self.connectionLbl.setText(f"Awaiting connection")

    def show_send(self):
        self.receive.show()
        self.start.hide()

    def radio(self):
        # Checks status of radio buttons and changes search options accordingly
        if self.networkRadio_2.isChecked() or self.previousRadio_2.isChecked():
            self.searchInput_2.setDisabled(True)
            self.searchBtn_2.setDisabled(True)
            if not self.previousRadio_2.isChecked():
                self.searchBtn_2.setDisabled(False)
        else:
            pass
            self.searchInput_2.setDisabled(False)
            self.searchBtn_2.setDisabled(False)

    def search(self):
        if self.networkRadio_2.isChecked():
            self.find_network("scan")
        elif self.previousRadio_2.isChecked():
            pass
        elif len(self.searchInput_2.text()) > 0:
            if self.ipRadio_2.isChecked():
                new_connection.ip = self.searchInput_2.text()
                self.find_network("ip")
            elif self.nameRadio_2.isChecked():
                new_connection.search_name = self.searchInput_2.text()
                self.find_network("name")
        else:
            # To add popup stating search cannot be empty
            pass

    def find_network(self, radio):
        self.optionsCombo_2.clear()
        if radio == "ip":
            try:
                new_connection.computer_name = socket.gethostbyaddr(new_connection.ip)[0]
            except socket.herror:
                self.message_box("Error", "Error: IP address not found")
                return
            self.optionsCombo_2.addItem(new_connection.computer_name)
        elif radio == "scan":
            scan = threading.Thread(target=self.scan_netwok, args=())
            scan.start()
        elif radio == "name":
            try:
                new_connection.ip = socket.gethostbyname(new_connection.search_name)
            except socket.gaierror:
                self.message_box("Error", "Error: Computer not found")
                return
            new_connection.computer_name = new_connection.search_name
            self.optionsCombo_2.addItem(new_connection.computer_name)

    def scan_netwok(self):
        # Scan local network for all devices using port 135 for Windows machines

        for i in range(1, 20):
            res = self.connect("192.168.0." + str(i), 135)
            if res:
                address = "192.168.0." + str(i)
                temp_computer_name = socket.gethostbyaddr(address)[0]
                # if this computer then do not include in options to select
                if new_connection.this_computer_name not in temp_computer_name:
                    self.optionsCombo_2.addItem(temp_computer_name)

    def connect(self, hostname, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((hostname, port))
        sock.close()
        return result == 0

    def connect_server(self):
        chosen_network = str(self.optionsCombo_2.currentText())
        new_connection.ip = socket.gethostbyname(chosen_network)
        self.client_connection.host = new_connection.ip
        connect_thread = threading.Thread(target=self.client_connection.connect, args=())
        connect_thread.start()
        while not self.client_connection.current_connection:
            continue
        self.connectionLbl_2.setText(self.client_connection.current_connection)
        self.button_state(False)
        QtWidgets.qApp.processEvents()

    def disconnect(self):
        # Close socket, set connection text and disable button on GUI.
        self.client_connection.disconnect()
        self.connectionLbl_2.setText("No Connection")
        self.button_state(True)

    def button_state(self, state):
        self.disconnectBtn_2.setDisabled(state)
        self.connectBtn_2.setDisabled((not state))
        self.rbBtn_2.setDisabled(state)
        self.audioBtn_2.setDisabled(state)
        self.allBtn_2.setDisabled(state)

    def drives(self):
        return wrap(win32api.GetLogicalDriveStrings(), 4)

    def add_folder(self):
        self.client_connection.audio_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        self.folderInput_2.setText(self.client_connection.audio_folder)

    def sync_audio(self):
        check_audio_file = self.client_connection.audio()

    def message_box(self, title, message):
        self.app = QtWidgets.QMessageBox()
        self.app.setWindowTitle(title)
        self.app.setText(message)
        self.app.exec()

    def closeEvent(self, event):
        """confirm exit when clicking file->exit or title bar cross"""
        result = QtWidgets.QMessageBox.question(self,
                                                "Confirm Exit...",
                                                "Are you sure you want to exit ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            event.accept()
            os._exit(1)
        else:
            event.ignore()


class Connection:
    def __init__(self):
        self.ip = ""
        self.port = 9999
        self.search_name = ""
        self.computer_name = ""
        self.this_computer_name = socket.gethostname()


new_connection = Connection()

app = QtWidgets.QApplication([])
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
window = MainWindow()
window.show()

sys.exit(app.exec_())
