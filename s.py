import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket Created successfully')

host='127.0.0.1'
port=12000

sock.bind((host,port))

sock.listen(10)
print('Listening....')

while True:
    con,addr=sock.accept()
    data=con.recv(1024)
    print(data.decode())
    
    f=open('s.txt','rb')
    line=f.read(1024)
    
    
    while line:
        con.send(line)
        line=f.read(1024)
        
    print('file succesfully transfered')
    f.close()
    con.close()