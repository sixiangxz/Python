# from multiprocessing import Process, Pipe
#
# def f(conn):
#      conn.send([42, None, 'hello from child'])
#      conn.send([43,None,'hello from child2'])
#      print("child recv:",conn.recv())
#      conn.close()
#
# if __name__ == '__main__':
#      parent_conn, child_conn = Pipe() #生成管道实例，取出两端
#      p = Process(target=f, args=(child_conn,))
#      p.start()
#      print('1', parent_conn.recv())# prints "[42, None, 'hello']"
#      print('2', parent_conn.recv())
#      parent_conn.send("hello send by parent")
#      p.join()
#
#
from multiprocessing import Process
from threading import Thread
import time
n = [1,2,3]
def consumer(n):
    time.sleep(0.5)
    n.append("a")
    print(n)


if __name__ == '__main__':

    p1 = Process(target=consumer, args=(n,))
    p1.start()
    p1.join()
    print("主")
    print(n)