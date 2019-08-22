import socket

client = socket.socket()
client.connect(('127.0.0.1', 8050))

while True:
    data = input(">>>:").strip()
    if not data:continue
    client.send(data.encode('utf-8'))
    recv = client.recv(1024)
    print(recv.decode('utf-8'))

client.close()