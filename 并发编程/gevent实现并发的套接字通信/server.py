from gevent import monkey, spawn;monkey.patch_all()
import socket


# 单线程实现并发
def communicate(conn):

    while True:
        try:
            data = conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()


def server(ip, port):
    server = socket.socket()
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        spawn(communicate, conn)

    server.close()


if __name__ == '__main__':
    g = spawn(server, '127.0.0.1', 8090)
    g.join()
