import socket
import os
import subprocess
from transfer import Transfer
from PyQt5 import QtCore, QtGui, QtWidgets



class Client:
    def __init__(self):
        self.host = ""
        self.port = 9999
        self.data = None
        self.s = None
        self.current_connection = None
        self.audio_folder = ""

    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(200)
        self.s.connect((self.host, self.port))

        # Listen for confirmation from server
        self.current_connection = self.s.recv(1024)
        self.current_connection = self.current_connection.decode("utf-8")

    def listen(self):
        # listen for messages when called
        while True:
            # infinite loop waiting for messages from server
            self.data = self.s.recv(1024)
            self.data = self.data.decode("utf-8")

            # If reply from server is quite then shutdown, close socket and exit infinite loop
            if self.data == "quit":
                self.terminate_connection()
                break

            elif len(self.data) > 0:
                print(self.data)
                # data_list = self.data.split("\n")
                # print(data_list)
        return

    def listen_list(self, files):
        full_packet = ""
        while True:
            packet = self.s.recv(1024)
            packet = packet.decode("utf-8")

            full_packet += packet
            if "!finished" in packet:
                break

        files.list_audio_files("client", "", "")
        received_data = full_packet.split("!new_track")
        received_data.pop()
        files.server_files_list = received_data
        files.list_server_files()
        # files.send_missing_files(self.s)

    def send(self):
        self.s.send(str.encode("Send Data"))

    def audio(self):
        if len(self.audio_folder) != 0:
            print("not 0")
            files = Transfer(self.audio_folder)
            self.s.send(str.encode("!list_server_audio_files"))
            self.listen_list(files)
        print("False")
        return "False"


    def rekordbox_sync(self, drive):
        username = os.getlogin()
        files = Transfer(f"{drive[:3]}Users\\{username}\\AppData\\Roaming\\Pioneer\\rekordbox\\")
        rb_files = ["master.db", "networkAnalyze6.db", "masterPlaylists6.xml", "automixPlaylist6.xml"]

        #self.progress_bar()
        for rb_file in rb_files:
            files.prepare_to_send_file(self.s, files.path, rb_file)
        for root, dir, file in os.walk(f"{files.path}\\share\\PIONEER"):
            #print(len(file))
            files.send_root(self.s, root)
            for f in file:
                files.prepare_to_send_file(self.s, root, f)
        print("finished sending")

    def progress_bar(self):
        progress = QtWidgets.QProgressDialog()
        progress.show()


        #files.list_rb_track_info(self.s)

    def all(self, drive):
        self.audio()
        self.rekordbox_sync(drive)

    def disconnect(self):
        # Send quit string to server and call listen method
        self.s.send(str.encode("quit"))
        self.listen()

    def terminate_connection(self):
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()
