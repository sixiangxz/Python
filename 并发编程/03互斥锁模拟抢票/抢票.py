# from multiprocessing import Process, Lock
from threading import Thread, Lock
import time
import json

def search(name):

    time.sleep(1)
    dic = json.load(open('db.txt', 'r', encoding='utf-8'))
    print("%s 查到余票数为:%s" % (name, dic['count']))


def buy2(name):

    time.sleep(1)
    dic = json.load(open('db.txt', 'r', encoding='utf-8'))
    print(name, dic["count"])
    if dic["count"] > 0:
        dic["count"] -= 1
        time.sleep(2)
        json.dump(dic, open('db.txt', 'w', encoding='utf-8'))
        print("%s 购票成功" % name)

def task(name, lock):

    search(name)

    lock.acquire()
    buy2(name)
    lock.release()


if __name__ == '__main__':
    mutex = Lock()
    for i in range(5):
        p = Thread(target=task, args=("路人%s" % i, mutex))
        p.start()

