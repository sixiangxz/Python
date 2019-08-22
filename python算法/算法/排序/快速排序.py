#  归位函数
#  目的是把小于tmp的值放在左边,大于tmp的值放在右边
import random
import sys
import time
sys.setrecursionlimit(100000)  # 设置递归最大深度

def partition(li, left, right):
    # 把第一位元素值保存到tmp,然后变成一个空位
    tmp = li[left]
    while left < right:
        # 从右面找比tmp小的数，li[right] >= tmp则right下标往前移,left==right时应该终止循环
        while left < right and li[right] >= tmp:
            right -= 1
        # 循环结束后找到比tmp小的数(或者是因为右边数比tmp都大,此时下标left和right重合),即自己给自己赋值
        li[left] = li[right]
        # 从左面找比tmp大的数，li[left] <= tmp则left下标往后移，,left==right时应该终止循环
        while left < right and li[left] <= tmp:
            left += 1
        # 循环结束后找到比tmp大的数(或者是因为左边数比tmp都小,此时下标left和right重合),即自己给自己赋值
        li[right] = li[left]
        # 最后空位指向left==right,要把值填回来
    li[left] = tmp
    # 返回此时mid下标
    return left


def quick_sort(li, left, right):
    if left < right:#  至少两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)


li = list(range(10000))
random.shuffle(li)
a = time.time()
quick_sort(li, 0, len(li)-1)
print(li)
print(time.time()-a)
