import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.bind(('127.0.0.1', 8000),)

phone.listen(5)

conn, addr = phone.accept()
print("server开始工作...")
conn.send("服务器...".encode('utf-8'))

server_sev = conn.recv(1024)
print(server_sev.decode())
conn.close()
conn.close()
