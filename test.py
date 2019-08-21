def bubble_sort(l):
    #下标的维护
    flog = False
    for i in range(len(l)):
        j = 0
        while j < (len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                flog = True
            j += 1
        if not flog:
            break
def selection_sort(l):
    for i in range(len(l)):
        tmp = i #目前最小的下标
        for k in range(i,len(l)):
            if l[k] < l[tmp]:
                tmp = k
        l[i],l[tmp] = l[tmp],l[i]

def insert_sort(l):
    for i in range(len(l)):
        #tmp = l[i] #准备交换的值 目前还不知道和哪个下标交换
        # for j in list(range(i))[::-1]:
        #     print(j)
        j = i - 1
        tmp = l[i]
        while j >= 0:
            if tmp < l[j]:
                l[j+1],l[j] = l[j],l[j+1]
            else:
                break
            j -= 1
        #print('-----')


        # print('------')
import random
l = list()
for i in range(1000):
    l.append(random.randint(0, 100))

import time
start = time.perf_counter()
selection_sort(l)
print((time.perf_counter()-start)*10**5)

start = time.perf_counter()
bubble_sort(l)
print((time.perf_counter()-start)*10**5)

start = time.perf_counter()
insert_sort(l)
print((time.perf_counter()-start)*10**5)


# n^2 算法复杂度分析  O(n^2)