import socket
import select
server = socket.socket()
server.bind(('127.0.0.1', 8050))
server.listen(5)
# 下面所有的IO操作都为非阻塞,下面操作遇到阻塞会返回BlockingIOError信号
server.setblocking(False)
print("start......")

rlist = [server, ]
wlist = []
# 保存发的数据
wdata = {}
while True:
    # select一次可以询问多个套接字,表示每隔0.5秒询问操作系统数据准备情况
    # rl可以收的套接字，wl可以发的套接字
    rl,wl,xl = select.select(rlist, wlist, [], 0.5)
    print('rl', rl)
    print('wl', wl)

    # sock=server或者sock=conn,一个用于建立连接的套接字，一个用于发送数据的套接字
    for sock in rl:
        if sock == server:
            conn, addr = sock.accept()
            rlist.append(conn)
        else:
            try:
                data = sock.recv(1024)
                if not data:
                    sock.close()
                    rlist.remove(sock)
                    continue
                wlist.append(sock)
                wdata[sock] = data.upper()
            except Exception:
                sock.close()
                rlist.remove(sock)

    for sock in wl:
        data = wdata[sock]
        print(data)
        sock.send(data)
        wlist.remove(sock)
        wdata.pop(sock)

server.close()

