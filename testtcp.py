import time
import socket
import threading

def tcplink(sock,addr):
    while True:
        data = sock.recv(1024)
        if data =='exit' or not data:
            break
    print(data)
    sock.close()

def tcpinit():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('192.168.199.154',9999))
    sock.listen(5)
    return sock

if __name__=="__main__":
    sock = tcpinit()
    while True:
        socket_handle,addr=sock.accept()
        t=threading.Thread(target=tcplink,args=(socket_handle,addr))
        t.start()