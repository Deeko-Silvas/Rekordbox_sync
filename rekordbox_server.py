import socket
import os
from transfer import ServerTransfer
from datetime import datetime
from Qt_popups import Popups

host = ""
port = 9999
s = None

class Server:
    def __init__(self):
        self.host = ""
        self.port = 9999
        self.s = None
        self.conn = None
        self.address = None
        self.connection_confirmed = False

    def create_socket(self):
        try:
            self.s = socket.socket()
        except socket.error as msg:
            message_box = Popups("Socket creation error", "Socket creation error: " + str(msg))
            message_box.message_box()

    def bind_socket(self):
        try:
            print("Binding the Port: " + str(self.port))
            self.s.bind((self.host, self.port))
            self.s.listen(5)
        except socket.error as msg:
            message_box = Popups("Socket binding error", "Socket binding error: " + str(msg) + "\nRetrying...")
            message_box.message_box()

    def socket_accept(self):
        self.conn, self.address = self.s.accept()
        self.connection_confirmed = True
        print("Connection has  been established! | IP " + self.address[0] + " | Port " + str(self.address[1]))
        self.confirm_connection()
        self.receive_commands()
        self.connection_confirmed = False
        self.conn.close()

    def confirm_connection(self):
        self.host = socket.gethostname()
        self.conn.send(str.encode(f"Connection established! | Name {self.host} | IP {socket.gethostbyname(self.host)}", encoding="utf-8"))

    def receive_commands(self):
        while True:
            data = self.conn.recv(1024)
            data = data.decode("utf-8")
            if data == "quit":
                self.conn.send(str.encode("quit", encoding="utf-8"))
                print(self.conn)
                self.connection_confirmed = False
                self.connect()
                break
            if data == "!list_server_audio_files":
                files = ServerTransfer("D:/Music/Unmixed Tunes")
                file_list = files.list_files()
                for file in file_list:
                    self.conn.send(str.encode(file, encoding="utf-8 "))
            if data == "!sending_file":
                self.conn.send(str.encode("!ready", encoding="utf-8"))
                receive_file()
            if data == "!sending_root":
                self.conn.send(str.encode("!ready", encoding="utf-8"))
                create_folders()

    def create_folders(self):
        details = self.conn.recv(2048)
        details = details.decode("utf-8")
        details_list = details.split(" + ")
        if not os.path.isdir(details_list[0]):
            print("new")
            os.mkdir(details_list[0])
        else:
            if self.check_date(details_list):
                self.conn.send(str.encode("!skip", encoding="utf-8"))
                return
        self.conn.sendall(str.encode("!send", encoding="utf-8"))

    def check_date(self, details):
        file = f"{details[0]}{details[1]}"
        date_server = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y, %m, %d, %H, %M, %S')
        if date_server >= details[3]:
            return True
        return False

    def receive_file(self):
        size_file = self.conn.recv(2048)
        size_file = size_file.decode("utf-8")
        total = 0
        size_file = size_file.split(" + ")
        if int(size_file[2]) > 0:
            file = f"{size_file[0]}\\{size_file[1]}"
            if os.path.isfile(file) and size_file[1] != "master.db":
                date_server = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y, %m, %d, %H, %M, %S')
                if date_server > size_file[3]:
                    self.conn.sendall(str.encode("!file_exists", encoding="utf-8"))
                    return
            self.conn.sendall(str.encode("!size_confirmed", encoding="utf-8"))
            f = open(file, "wb")
            while True:
                data = self.conn.recv(1024)
                f.write(data)
                total += len(data)
                if total == int(size_file[2]):
                    break
            f.close()
            self.conn.sendall(str.encode("!complete", encoding="utf-8"))

    def connect(self):
        self.create_socket()
        self.bind_socket()
        self.socket_accept()


