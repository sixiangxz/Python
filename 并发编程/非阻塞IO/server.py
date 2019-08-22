import socket
server = socket.socket()
server.bind(('127.0.0.1', 8050))
server.listen(5)
# 下面所有的IO操作都为非阻塞,下面操作遇到阻塞会返回BlockingIOError信号
server.setblocking(False)
print("start......")


rlist = []
while True:
    try:
        conn, addr = server.accept()
        rlist.append(conn)
        print(rlist)
    except BlockingIOError:
        # 阻塞时干其他事
        del_rlist = []
        for conn in rlist:
            # try没有正常接收消息时需要再次接受
            try:
                data = conn.recv(1024)
                # 此连接没有发送消息时需要移除
                if not data:
                    del_rlist.append(conn)
                    continue
                conn.send(data.upper())
            except BlockingIOError:
                continue
            # 客户端断开连接
            except Exception:
                conn.close()
                del_rlist.append(conn)
        # 从列表中清除断开连接的conn
        for conn in del_rlist:
            rlist.remove(conn)

server.close()
