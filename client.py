import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


s.connect(('192.168.199.154',9999))
while True:
    data=raw_input("please input data you want to send \n")
    if data!='close':
        s.send(data)
    else:
        break
s.close()
        