import socket
server = socket.socket()
server.bind(('127.0.0.1', 8050))
server.listen(5)
print("start......")

while True:

    conn, addr = server.accept()
    print(addr)

    while True:
        # 捕获客户端连接中断
        try:
            data = conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()

server.close()
