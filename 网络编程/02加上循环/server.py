import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.bind(('127.0.0.1', 8000),)

phone.listen(5)
conn, addr = phone.accept()
print("server开始工作...")
while True:

    conn.send("服务器已经成功连接".encode('utf-8'))

    server_sev = conn.recv(1024)
    print(server_sev.decode('utf-8'))

conn.close()
conn.close()
