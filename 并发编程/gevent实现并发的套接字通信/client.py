import socket
from threading import Thread, current_thread


def client():
    client = socket.socket()
    client.connect(('127.0.0.1', 8090), )

    while True:
        client.send(("%s hello " % current_thread().getName()).encode('utf-8'))
        data = client.recv(1024)
        print(data.decode('utf-8'))
    client.close()


if __name__ == '__main__':
    for i in range(15):
        t = Thread(target=client)
        t.start()