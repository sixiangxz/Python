from multiprocessing import Process
import time


# 方式一
# def test(name):
#     print("%s正在运行..." % name)
#     time.sleep(2)
#     print("%s结束运行..." % name)
#
#
# if __name__ == '__main__':
#
#     p1 = Process(target=test, args=('p',),)
#     # p1只是给操作做系统发一个start信号,具体什么时候执行由操作系统决定
#     p1.start()
#
#     print("主")


# 方式二
class MyProcess(Process):

    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    # 必须写run()方法，指定要执行的代码
    def run(self):
        print("%sis running ..." % self.name)
        time.sleep(1)
        print("%sis ending ..." % self.name)


if __name__ == '__main__':

    p1 = MyProcess("p")
    # p1只是给操作做系统发一个start信号,具体什么时候执行由操作系统决定
    p1.start()

    print("主")