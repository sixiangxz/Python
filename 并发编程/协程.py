import time


# 串行
# def produce():
#     res = []
#     for i in range(10000000):
#         res.append(i)
#
#     return res
#
#
# def consumer():
#     pass

# 并行
def produce():
    g = consumer()
    next(g)
    for i in range(10000000):
        g.send(i)


def consumer():
    while True:
        res = yield


if __name__ == '__main__':

    start = time.time()
    # 串行
    # produce()
    # consumer()
    # print(time.time()-start)

    # 并行
    produce()
    consumer()
    print(time.time() - start)
