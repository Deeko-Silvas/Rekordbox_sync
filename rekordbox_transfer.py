import socket

local_name = socket.gethostname()
print(local_name)
#name = socket.gethostbyaddr("192.168.0.4")

#print(name)

def connect(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((hostname, port))
    sock.close()
    return result == 0

for i in range(0,20):
    res = connect("192.168.0."+str(i), 135)
    if res:
        address = "192.168.0." + str(i)
        print("Device found at: " + address + ":"+str(135))
        #print(socket.gethostbyaddr(address))
        print("name " + socket.gethostbyaddr(address)[0])

my_socket = socket( socket.AF_INET, socket.SOCK_DGRAM )




