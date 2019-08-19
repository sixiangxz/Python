import socket
from multiprocessing import Process


def talk(conn):
    recv = conn.recv(1024).decode('gbk')
    print(recv)
    conn.send(recv.encode('gbk'))


def server(name):
    phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    phone.bind(name)
    phone.listen(5)
    while True:
        conn, addr = phone.accept()
        p = Process(target=talk, args=(conn, ))
        p.start()


if __name__ == '__main__':
    bind = ("127.0.0.1", 8000)
    server(bind)
