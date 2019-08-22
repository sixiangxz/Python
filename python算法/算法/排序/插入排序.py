def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]  # i表示摸到的牌的下标
        print(tmp)
        j = i - 1  # 手里牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)


li = [5,7,4,6,3,1,2,9,8]
# print(li)
insert_sort(li)
# print(li)