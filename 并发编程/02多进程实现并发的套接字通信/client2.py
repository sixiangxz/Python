import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(("127.0.0.1", 8000))

while True:

    send_to = input("发送>>>:")
    if not send_to:continue
    phone.send(send_to.encode('gbk'))

    recv = phone.recv(1024).decode('gbk')
    print(recv)