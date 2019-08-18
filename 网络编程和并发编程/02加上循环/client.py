import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8000),)
# 收到服务器
client_recv = phone.recv(1024)
print(client_recv.decode())
while True:

    mesg = input("输入发送信息：")
    if not mesg:continue
    phone.send(mesg.encode('utf-8'))

phone.close()