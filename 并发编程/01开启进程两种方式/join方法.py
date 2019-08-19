from multiprocessing import Process
import time


def test(name, n):
    print("%s正在运行..." % name)
    time.sleep(n)
    print("%s结束运行..." % name)


if __name__ == '__main__':
    start = time.time()
    p1 = Process(target=test, args=('p1',4),)
    p2 = Process(target=test, args=('p2',3),)
    p4 = Process(target=test, args=('p4',1),)
    p1.start()
    p2.start()
    p4.start()
    p1.join()
    p2.join()
    p4.join()
    print(time.time()-start)
    print("主")
