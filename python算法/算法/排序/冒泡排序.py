# 冒泡排序O(n*n)
def bubble_sort(lis):

    for i in range(len(lis)-1):
        is_sort = False  # 优化算法，可能不用循环n-1次就已有序
        for j in range(len(lis)-i-1):
            if lis[j] > lis[j+1]:
                is_sort = True
                lis[j], lis[j+1] = lis[j+1], lis[j]
        if not is_sort:
            return
        print(i, lis)


a = [1, 4, 5, 3, 7, 9, 6, 2, 8]
print('..........', a)
bubble_sort(a)

