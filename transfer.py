import os
import socket
from datetime import datetime


class Transfer:
    def __init__(self, path):
        self.path = path
        self.audio_folder = ""
        self.files_list = []
        self.client_files_list = []
        self.server_files_list = []

    def list_audio_files(self, location, split, finish):
        for root, dir, files, in os.walk(self.path):
            if len(files) > 0:
                for file in files:
                    self.files_list.append(f"{root}\\{file}{split}")
            if location == "client":
                self.client_files_list = self.files_list
            else:
                self.files_list.append(finish)
                return self.files_list

    def list_server_files(self):
        print(self.client_files_list)
        client_difference = set(self.client_files_list) - set(self.server_files_list)
        client_difference = list(client_difference)
        for diff in client_difference:
            #print(diff)
            if "HArd Drive" not in diff:
                print(diff)

    """
    def list_rb_track_info(self, s):
        for root, dir, files in os.walk(f"{self.path}\\share\\PIONEER"):
            self.send_root(s, root)
            for file in files:
                self.prepare_to_send_file(s, root, file)
        print("finished sending")
    """

    def send_root(self, s, root):
        s.sendall(str.encode("!sending_root"))
        data = s.recv(1024)
        data = data.decode("utf-8")
        if data == "!ready":
            root = str.encode(root, encoding="utf-8")
            s.sendall(root)

    def prepare_to_send_file(self, s, root, filename):
        """ open file to be sent and send message to server to be ready to accept file
        wait for confirmation that the server is ready"""
        file = open(f"{root}\\{filename}", "rb")
        l = str.encode("!sending_file", encoding="utf-8")
        s.sendall(l)
        while True:
            data = s.recv(1024)
            if data.decode("utf-8") == "!ready":
                break
        self.confirm_file_name_size(s, root, file, filename)

    def confirm_file_name_size(self, s, root, file, filename):
        """ get size of file to be sent, confirm this to the server and wait for confirmation back"""
        size = str(os.path.getsize(f"{root}\\{filename}"))
        mod_time = os.path.getmtime(f"{root}\\{filename}")
        mod_time = datetime.fromtimestamp(mod_time).strftime('%Y, %m, %d, %H, %M, %S')
        name_size = f"{root} + {filename} + {size} + {mod_time}"
        s.send(str.encode(name_size, "utf-8"))
        while True:
            data = s.recv(1024)
            data = data.decode("utf-8")
            if data == "!size_confirmed":
                break
            elif data == "!file_exists":
                return
        self.send_file(s, file)

    def send_file(self, s, file):
        """ when confirmation of size is received back send read file and send until all of file has been sent,
        then close the file"""
        l = file.read(1024)
        while l:
            s.sendall(l)
            l = file.read(1024)
        file.close()
        while True:
            data = s.recv(1024)
            if data.decode("utf-8") == "!complete":
                break



    def compare_audio_files(self, client, server):
        pass