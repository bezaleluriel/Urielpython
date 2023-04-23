# import the socket module
import socket

# set the host and port values
HOST = '127.0.0.1'
PORT = 65432

# create a TCP socket object
# AF_INET is a constant defined in the socket module that represents the address (or address family) format that the socket can use.
# SOCK_STREAM is a constant defined in the socket module that represents the type of socket that is being created.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the host and port
s.bind((HOST, PORT))

# listen for incoming connections (MAX 5 connections)
s.listen(5)

# keep listening for incoming connections
while True:
    # block until a client connects
    conn, addr = s.accept()

    # print a message indicating the client address
    print(f'Connected by {addr}')

    # receive data from the client
    data = conn.recv(1024)

    print(data)
    # send the received data back to the client
    conn.sendall(data)

    # close the connection with the client
    conn.close()
