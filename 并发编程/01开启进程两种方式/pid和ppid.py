from multiprocessing import Process
import time
import os


def test():
    print("子进程id——>：%s 父进程id——>：%s" % (os.getpid(), os.getppid()))
    time.sleep(2)
    print("子进程id——>：%s 父进程id——>：%s" % (os.getpid(), os.getppid()))


if __name__ == '__main__':

    p1 = Process(target=test,)
    # p1只是给操作做系统发一个start信号,具体什么时候执行由操作系统决定
    p1.start()
    print("主—>：%s 父—>：%s" % (p1.pid,  os.getppid()))