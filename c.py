import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket Created')

host='127.0.0.1'
port=12000

sock.connect((host,port))
print('Connection Established')

sock.send('A message from client'.encode())

f=open('c.txt','wb')
line=sock.recv(1024)

while line:
    f.write(line)
    line=sock.recv(1024)
    
print('successfully received')
f.close()
sock.close()
print('Connection Closed')