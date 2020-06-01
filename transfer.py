import os
from datetime import datetime


class Transfer:
    def __init__(self, path):
        self.path = path
        self.audio_folder = ""
        self.files_list = []
        self.client_files_list = []
        self.server_files_list = []
        self.client_difference = []

    def list_audio_files(self, location, split, finish):
        """create a list of audio files on server and client machine"""
        for root, d, files, in os.walk(self.path):
            if len(files) > 0:
                for file in files:
                    self.files_list.append(f"{root}\\{file}{split}")
            if location == "client":
                self.client_files_list = self.files_list
            else:
                self.files_list.append(finish)
                return self.files_list

    def list_server_files(self):
        """list files that are on client but not server"""
        self.client_difference = set(self.client_files_list) - set(self.server_files_list)
        self.client_difference = list(self.client_difference)

    def send_root(self, s, root):
        """send all folder names to server and return true if folder contents need to be sent"""
        s.sendall(str.encode("!sending_root"))
        data = s.recv(1024)
        data = data.decode("utf-8")
        if data == "!ready":
            details = self.file_details(root)
            details = str.encode(details, encoding="utf-8")
            s.sendall(details)
            while True:
                data = s.recv(1024)
                if data.decode("utf-8") == "!send":
                    return True
                return False

    def prepare_to_send_file(self, s, root, filename):
        """ open file to be sent and send message to server to be ready to accept file
        wait for confirmation that the server is ready"""
        file = open(f"{root}\\{filename}", "rb")
        sending = str.encode("!sending_file", encoding="utf-8")
        s.sendall(sending)
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

    def file_details(self, root, filename=""):
        """return a string containing root, filename, size and modified time and date separated by a +"""
        size = str(os.path.getsize(f"{root}{filename}"))
        mod_time = datetime.fromtimestamp(os.path.getmtime(f"{root}{filename}")).strftime('%Y, %m, %d, %H, %M, %S')
        return f"{root} + {filename} + {size} + {mod_time}"

    def send_file(self, s, file):
        """ when confirmation of size is received back send read file and send until all of file has been sent,
        then close the file"""
        print("sending file")
        file_data = file.read(1024)
        while file_data:
            s.sendall(file_data)
            file_data = file.read(1024)
        file.close()
        while True:
            data = s.recv(1024)
            if data.decode("utf-8") == "!complete":
                break


class ServerTransfer:
    def __init__(self, path):
        self.path = path
        self.files_list = []

    def list_files(self):
        for root, dirs, files in os.walk(self.path):
            if len(files) > 0:
                for file in files:
                    self.files_list.append(f"{root}\\{file}!new_track")
        self.files_list.append("!finished")
        return self.files_list
