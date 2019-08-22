# 选择排序  O(n*n)
def select_sort(lis):

    for i in range(len(lis)-1):
        # 假如lis_min为list无序区最小数的下标，默认为第一个数
        lis_min = i
        # i之前为有序区，i之后为无序区，通过循环找到无序列表最小值然后获取下标
        for j in range(i, len(lis)):
            if lis[j] < lis[lis_min]:
                lis_min = j
        # 找到比lis_min还小的值，并交换这个值
        if lis_min != i:
            lis[i], lis[lis_min] = lis[lis_min], lis[i]
        print(a)


a = [1, 4, 5, 3, 7, 9, 6, 2, 8]
print('..........', a)
select_sort(a)