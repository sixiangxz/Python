from multiprocessing import Process, Queue
from threading import Thread
import time


def producer(q):
    for i in range(10):
        res = "包子%s" % i
        time.sleep(0.3)
        print("生产者生产了%s" % res)
        q.put(res)


def consumer(q):
    while True:
        res = q.get()
        time.sleep(0.5)
        print("生产者吃了%s" % res)


if __name__ == '__main__':

    # 容器
    q = Queue()
    # 生产者们
    p1 = Thread(target=producer, args=(q,))
    # 进程不能共享变量
    # p1 = Process(target=producer, args=(q,))

    # 消费者们
    # c1 = Process(target=consumer, args=(q, ))
    c1 = Thread(target=consumer, args=(q, ))

    p1.start()
    c1.start()

    print("主")

