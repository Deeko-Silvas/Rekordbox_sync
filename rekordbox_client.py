import socket
import os
from transfer import Transfer
from Qt_popups import Popups


class Client:
    def __init__(self):
        self.host = ""
        self.port = 9999
        self.data = None
        self.s = None
        self.current_connection = None
        self.audio_folder = ""
        self.app = None

    def connect(self):
        # Create socket
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

            # If reply from server is quit then shutdown, close socket and exit infinite loop
            if self.data == "!confirm_quit":
                self.terminate_connection()
                break

            elif len(self.data) > 0:
                print(self.data)
                # data_list = self.data.split("\n")
                # print(data_list)
        return

    def listen_list(self, files):
        """ listens for a list of files from server until !finished message received.
        passes the list to file.server_files_list to compare against client files before sending missing
        files to server"""
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
        for track in files.client_difference:
            # find last instanc of \ in track to split track and root
            i = track.rfind("\\")
            root = track[:i]
            if "HArd Drive" not in root:
                track = track[i+1:]
                files.send_root(self.s, root)
                files.prepare_to_send_file(self.s, root, track)
        message_box = Popups("Finished", "Finished sending Audio files")
        message_box.message_box()

    def send(self):
        self.s.send(str.encode("Send Data"))

    def audio(self):
        print("audio")
        if len(self.audio_folder) != 0:
            files = Transfer(self.audio_folder)
            self.s.send(str.encode("!list_server_audio_files"))
            self.listen_list(files)
        else:
            message_box = Popups("Error", "Please select audio folder")
            message_box.message_box()

    def rekordbox_sync(self, drive):
        username = os.getlogin()
        files = Transfer(f"{drive[:3]}Users\\{username}\\AppData\\Roaming\\Pioneer\\rekordbox\\")
        # rb_files = ["automixPlaylist6.xml"]
        rb_files = ["master.db", "master.backup.db", "networkAnalyze6.db", "masterPlaylists6.xml",
                    "automixPlaylist6.xml"]

        for rb_file in rb_files:
            files.prepare_to_send_file(self.s, files.path, rb_file)

        for root, d, file in os.walk(f"{files.path}share\\PIONEER"):
            if files.send_root(self.s, root):
                for f in file:
                    files.prepare_to_send_file(self.s, root, f)

        message_box = Popups("Finished", "Finished sending database, artwork and waveform files")
        message_box.message_box()

    def all(self, drive):
        """run audio and rekordbox sync functions when sync all button clicked"""
        self.audio()
        self.rekordbox_sync(drive)

    def disconnect(self):
        """Send quit string to server and call listen method"""
        self.s.send(str.encode("!quit"))
        self.listen()

    def terminate_connection(self):
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()
