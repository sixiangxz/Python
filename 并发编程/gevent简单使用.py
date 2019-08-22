import gevent
from gevent import monkey; monkey.patch_all()# 要在第一行
import time

def eat(name):
    print("%s eat 1" % name)
    # gevent.sleep(1)
    time.sleep(1)
    print("%s eat 2" % name)


def play(name):
    print("%s play 1" % name)
    # gevent.sleep(1)
    time.sleep(1)
    print("%s play 2" % name)


g1 = gevent.spawn(eat, "jack")
g2 = gevent.spawn(play, "jack")


# 异步执行方式,发完信号次线程就该结束,需要用join等待,否则还没执行就已经结束
# g1.join()
# g2.join()
gevent.joinall([g1, g2])
