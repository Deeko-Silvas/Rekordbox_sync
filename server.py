import socket
import sys
import subprocess
import os
from transfer import ServerTransfer
from datetime import datetime

host = ""
port = 9999
s = None

def create_socket():
    try:
        global s
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

def bind_socket():
    try:
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\nRetrying...")

def socket_accept():
    conn, address = s.accept()
    print("Connection has  been established! | IP " + address[0] + " | Port " + str(address[1]))
    confirm_connection(conn)
    receive_commands(conn)
    conn.close()

def confirm_connection(conn):
    host = socket.gethostname()
    conn.send(str.encode(f"Connection established! | Name {host} | IP {socket.gethostbyname(host)}", encoding="utf-8"))

def receive_commands(conn):
    while True:
        data = conn.recv(1024)
        data = data.decode("utf-8")
        if data == "quit":
            conn.send(str.encode("quit", encoding="utf-8"))
            main()
            break
        if data == "!list_server_audio_files":
            files = ServerTransfer("D:/Music/Unmixed Tunes")
            file_list = files.list_files()
            for file in file_list:
                conn.send(str.encode(file, encoding="utf-8 "))
        if data == "!sending_file":
            conn.send(str.encode("!ready", encoding="utf-8"))
            receive_file(conn)
            # break
        if data == "!sending_root":
            conn.send(str.encode("!ready", encoding="utf-8"))
            create_folders(conn)

def create_folders(conn):
    details = conn.recv(2048)
    details = details.decode("utf-8")
    details_list = details.split(" + ")
    if not os.path.isdir(details_list[0]):
        print("new")
        os.mkdir(details_list[0])
    else:
        if check_date(details_list):
            conn.send(str.encode("!skip", encoding="utf-8"))
            return
    conn.sendall(str.encode("!send", encoding="utf-8"))

def check_date(details):
    file = f"{details[0]}{details[1]}"
    date_server = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y, %m, %d, %H, %M, %S')
    if date_server >= details[3]:
        return True
    return False


def receive_file(conn):
    size_file = conn.recv(2048)
    size_file = size_file.decode("utf-8")
    total = 0
    size_file = size_file.split(" + ")
    if int(size_file[2]) > 0:
        file = f"{size_file[0]}\\{size_file[1]}"
        if os.path.isfile(file) and size_file[1] != "master.db":
            date_server = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y, %m, %d, %H, %M, %S')
            if date_server > size_file[3]:
                conn.sendall(str.encode("!file_exists", encoding="utf-8"))
                return
        conn.sendall(str.encode("!size_confirmed", encoding="utf-8"))
        f = open(file, "wb")
        while True:
            data = conn.recv(1024)
            f.write(data)
            total += len(data)
            if total == int(size_file[2]):
                break
        f.close()
        conn.sendall(str.encode("!complete", encoding="utf-8"))

def command_prompt(conn, data):
    cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    output_byte = cmd.stdout.read() + cmd.stderr.read()
    output_str = str(output_byte, "utf-8")
    current_dir = os.getcwd() + ">"
    conn.sendall(str.encode(output_str + current_dir))

def send_commands(conn):
    conn.sendall(str.encode(f"Connection has been established to {socket.gethostname()}"))
    data = conn.recv(1024)

    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        command = str.encode(cmd)
        if len(command) > 0:
            conn.sendall(command)
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()