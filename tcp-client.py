import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# create socket (SOCK_STREAM = TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # connect to server
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # receive data back
    received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))
