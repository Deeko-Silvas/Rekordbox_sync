from MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle
import sys
import win32api
from textwrap import wrap
import socket
from rekordbox_server import Server
from rekordbox_client import Client
import threading


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.send_btn.clicked.connect(self.show_receive)
        self.receive_btn.clicked.connect(self.show_send)

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

        self.disconnectBtn_2.clicked.connect(self.disconnet_server)
        self.audioBtn_2.clicked.connect(client_connection.audio)
        self.rbBtn_2.clicked.connect(lambda: client_connection.rekordbox_sync(str(self.drivesComboBox_2.currentText())))
        self.allBtn_2.clicked.connect(lambda: client_connection.all(str(self.drivesComboBox_2.currentText())))

        self.disconnectBtn_2.setDisabled(True)

    def show_send(self):
        self.send.show()
        self.start.hide()

    def show_receive(self):
        self.receive.show()
        self.start.hide()

    def radio(self):
        # Checks status of radio buttons and changes search options accordingly
        if self.networkRadio_2.isChecked() or self.previousRadio_2.isChecked():
            self.searchInput_2.setDisabled(True)
        else:
            pass
            self.searchInput_2.setDisabled(False)

    def search(self):
        if self.ipRadio_2.isChecked():
            new_connection.ip = self.searchInput_2.text()
        elif self.nameRadio_2.isChecked():
            new_connection.search_name = self.searchInput_2.text()
            self.find_network("name")
        elif self.networkRadio_2:
            self.find_network("scan")

    def find_network(self, radio):
        self.optionsCombo_2.clear()
        if radio == "ip":
            new_connection.computer_name = socket.gethostbyaddr(new_connection.ip)[0]
            self.optionsCombo_2.addItem(new_connection.computer_name)
        elif radio == "scan":
            scan = threading.Thread(target=self.scan_netwok, args=())
            scan.start()
        elif radio == "name":
            new_connection.ip = socket.gethostname(new_connection.search_name)
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
        client_connection.host = new_connection.ip
        connect_thread = threading.Thread(target=client_connection.connect, args=())
        connect_thread.start()
        while not client_connection.current_connection:
            continue
        self.connectionLbl_2.setText(client_connection.current_connection)
        self.disconnectBtn_2.setDisabled(False)

    def disconnet_server(self):
        # Close socket, set connection text and disable button on GUI.
        client_connection.disconnect()
        self.connectionLbl_2.setText("No Connection")
        self.disconnectBtn_2.setDisabled(True)

    def drives(self):
        return wrap(win32api.GetLogicalDriveStrings(), 4)


class Connection:
    def __init__(self):
        self.ip = ""
        self.port = 9999
        self.search_name = ""
        self.computer_name = ""
        self.this_computer_name = socket.gethostname()


new_connection = Connection()
client_connection = Client()

app = QtWidgets.QApplication([])
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
window = MainWindow()
window.show()

sys.exit(app.exec_())
