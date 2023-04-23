import socket
# HOST = 'MHTX-COMP1400'
HOST = '127.0.0.1'
PORT = 65432
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'urieddddd')
data = s.recv(1024)
s.close()
print(f'Recieved: {data}')
