import socket
import html

HOST = '192.168.68.61'                 # Symbolic name meaning all available in$
PORT = 8083              # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(HOST)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connected by', addr
data = html.HTML
print('bip')
print(data)
while 1:
  conn.sendall(data.encode('utf-8'))
conn.close()
