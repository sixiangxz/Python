# 表示n个盘子从a经过b移到c上
def hanoi(n, a, b, c):
    # 没有盘子将不移动
    if n > 0:
        # 表示n-1个盘子从a经过c移到b上
        hanoi(n-1, a, c, b)
        # 将第n个盘子由a移到c上
        print('%s moving %s' % (a, c))
        # 表示n-1个盘子从b经过a移到c上
        hanoi(n-1, b, a, c)


hanoi(3, 'A', 'B', 'C')
