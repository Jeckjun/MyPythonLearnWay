# 计时装饰器
import time
def dec(func):      # 时间装饰器
    def decl(*args, **kwargs):    # *args表示多个参数拆分，**kwargs多个key,value的参数拆分,类似dict字典
        print('--------%s 算法-------------' % (func.__name__))
        start = time.perf_counter()
        a = func(*args, **kwargs)
        print('本次算法 长度为 %6d || 消耗的时间为 %s' % (len(l), (time.perf_counter() - start)))
        print('******************')
        return a
    return decl
@dec
def bubble_sort(l):
    #下标的维护
    for i in range(len(l)):
        j = 0
        while j < (len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
            j += 1
    return l

def selection_sort(l):
    for i in range(len(l)):
        tmp = i #目前最小的下标
        for k in range(i,len(l)):
            if l[k] < l[tmp]:
                tmp = k
        l[i],l[tmp] = l[tmp],l[i]
#
def insert_sort(l):
    for i in range(len(l)):
        #tmp = l[i] #准备交换的值 目前还不知道和哪个下标交换
        # for j in list(range(i))[::-1]:
        #     print(j)
        j = i - 1
        tmp = l[i]
        while j >= 0:
            if tmp < l[j]:
                l[j+1] = l[j]
            else:
                break
            j -= 1
        l[j+1] = tmp
    return l
#     0 1       0 1
# [8,7,6,5,4,3,2,1]  --> [3,4]  -- [1,2] -- [1,2,3,4]
def merge_sort(l):
    if len(l) < 2:
        return l
    else:
        mid = len(l) // 2
        left = merge_sort(l[:mid])
        right = merge_sort(l[mid:])
        tmp = list()
        i = 0
        j = 0
        while (i < len(left)) or (j < len(right)):
            if (i < len(left)) and (j < len(right)):
                if left[i] < right[j]:
                    tmp.append(left[i])
                    i += 1
                else:
                    tmp.append(right[j])
                    j += 1
            elif i >= len(left):
                tmp.append(right[j])
                j += 1
            else:
                tmp.append(left[i])
                i += 1
        return tmp

import random
import time
# def cast(fun):
#     print('--------%s 算法-------------' % (fun.__name__))
#     for i in range(2,5):
#         l = []
#         for j in range(10**i):
#             l.append(random.randint(0,100000))
#         start = time.perf_counter()
#         fun(l[:])
#         print('本次算法 长度为 %6d || 消耗的时间为 %s' % (len(l),(time.perf_counter()-start)))
#         print('******************')
#
# l = [merge_sort,insert_sort,selection_sort,bubble_sort]
#
# def test(l):
#     for f in l:
#         cast(f)
#
# test(l)

l = [2,85,25,12]
x = bubble_sort(l)
print(x)