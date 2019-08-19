import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8000),)

client_recv = phone.recv(1024)
print(client_recv.decode())

phone.send("hello".encode())

phone.close()