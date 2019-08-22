# 8-21 list作业

# 1、循环录入5个数字，然后按反序输出（将一个数组中的值按逆序重新存放，
# 例如原来的顺序为：8，6，5，4，1.要求改为：1，4，5，6，8输出；并将数组中的值输出）
# list_num = []
# i = 0
# while i < 5:
#     num = int(input('输入数字：'))
#     list_num.append(num)
#     i += 1
# list_num.sort(reverse=True)
# print(list_num)

# 2、['12','13','33','34']，移除这个数组中包含1的字符串，提示：使用成员运算符in判定是否包含
# current_list = ['12', '13', '33', '34']
# 方法一，while
# i = 0
# while i < len(current_list):
#     if '1' in current_list[i]:
#         current_list.pop(i)
#         i -= 1
#     i += 1
# 方法二，倒序
# for i in range(len(current_list)-1, -1, -1):
#     if '1' in current_list[i]:
#         current_list.pop(i)
# 方法三，拷贝原始list操作
# for i in current_list[:]:
#     if '1' in i:
#         current_list.remove(i)
# print(current_list)

# 3、找出一个数组中，输出数字小于33的元素 如数组：[11,22,33,1,6,4,88,44]
# 和数组 ['11','22','33','1','6','4','88','44']
# list1 = [11, 22, 33, 1, 6, 4, 88, 44]
# list2 = ['11', '22', '33', '1', '6', '4', '88', '44']
# for i in list1:
#     if i < 33:
#         print(i, end='\t')
# print()
# for i in list2:
#     if int(i) < 33:
#         print(i, end='\t')

# 4、找出一个列表中，只出现了一次的数字，并且保持原来的次序，例如[1,2,1,3,2,5]结果为[3,5]
# list3 = [1, 2, 1, 3, 2, 5]
# for i in range(len(list3)):
#     j = i+1
#     while j < len(list3):
#         if list3[i] == list3[j]:
#             list3.pop(i)
#             j -= 1
#             list3.pop(j)
#         j += 1
# print(list3)

# 5、一个列表中，存放多个数字，查找这个列表中的最大值；
# list4 = [5, 45, 450, 500, 35, 65]
# 方法一，先排序，再找
# list4.sort(reverse=True)
# print(list4[0])
# 方法二
# for i in range(len(list4)-1):
#     # for j in range(i+1, len(list4)):
#     if list4[i] > list4[i+1]:
#         list4[i], list4[i+1] = list4[i+1], list4[i]
# print(list4[-1])
# 方法三
# print(max(list4))

# 6、随机产生20个100-200之间的正整数存放到数组中，并求数组中的所有元素最大值、最小值、平均值，
# 然后将各元素的与平均值的差组成一个新列表。
# import random
# random_list = []
# new_list = []
# for i in range(20):
#     random_list.append(random.randint(100, 201))
# print(random_list)
# print(max(random_list))
# print(min(random_list))
# avgList = sum(random_list)/len(random_list)
# print(avgList)
# for j in random_list:
#     new_list.append(j - avgList)
# print(new_list)

# 7、将字符串中的数字去掉，字母转为大写：“0go08o32d”
# str1 = '0go08o32d'
# list5 = []
# for i in list(str1)[:]:
#     if i in '0123456789':
#         list(str1).remove(i)
#     else:
#         list5.append(chr(ord(i)-32))
# print(list5)
# 方法二
# import re
# strObj = re.sub(r'[0-9]+', "", str1)
# newList = []
# for i in strObj:
#     newList.append(chr(ord(i)-32))
# print(newList)

# 8、给定一个字符串，判断字符串中是否还有png，有就删除它
# str2 = 'sjdhpdjnahdgd'
# str2_list = list(str2)
# for i in str2_list[:]:
#     if i in 'png':
#         str2_list.remove(i)
# print(''.join(str2_list))

# 9、aaabbccccdd输出为3a2b4c2d
str9 = 'aaabbccccdd'
# 方法一
# str9_list = list(str9)
# print(str9_list)
# print(str(str9_list.count('a'))+'a'+str(str9_list.count('b'))
#       +'b'+str(str9_list.count('c'))+'c'+str(str9_list.count('d'))+'d')

# 方法三，列表
# a = []
# x = []
# for i in range(0, len(str9)):
#     if i + 1 < len(str9):
#         if str9[i] == str9[i + 1]:
#             x.append(str9[i])  # 把相同的放入x列表
#         else:
#             x.append(str9[i])
#             a.append(x)    # 不同时，把x放入a
#             x = []
#     else:
#         x.append(str9[len(str9) - 1])
#         a.append(x)
# y = []
# for i in a:
#     x = ''
#     for j in i:
#         x += j
#     y.append(x)    # 放入新集合，并转化为int
# for i in y:
#     print(str(len(i))+''.join(set(i)), end='')      # set集合去重

# 方法三，字典
# count = {}
# for i in 'aaabbccccdd':
#     if i not in count:
#         count[i] = 1
#     else:
#         count[i] += 1
# for k, v in count.items():
#     print(str(v)+''+k, end='')

# 10、写一个函数，计算任意一个身份证号对应的出生年月日和性别
# idStr = '513701198011251112'
# def judge_id(idStr):
#     id_list = list(idStr)
#     year = id_list[6:10]
#     month = id_list[10:12]
#     day = id_list[12:14]
#     sex = id_list[14:15]
#     sexStr = ''.join(sex)
#     if sexStr == '1':
#         sexStr = '男'
#     else:
#         sexStr = '女'
#     print("出生日期：{0:s}年{1:s}月{2:s}日\t性别：{3:s}".format("".join(year), "".join(month), "".join(day), sexStr))

# judge_id(idStr)

# 1、编写一个函数，输入n为偶数时，调用函数求1/2 + 1/4 + ... + 1/n
# 当输入n为奇数时，调用函数求1/1 + 1/3 + ... + 1/n
# 思考：如何简化为一个函数完成，通用两个功能
# def common(n):
#     if n % 2 == 0:
#         sum = 0
#         for i in range(2, n+1, 2):
#             sum += 1/i
#         return sum
#     else:
#         sum = 0
#         for i in range(1, n+1, 2):
#             sum += 1 / i
#         return sum
#
# print(common(7))

# 1、杨辉三角实现：
#           1
#          1 1
#        1  2  1
#       1  3  3  1
#     1  4  6  4  1
#    1  5  10 10 5 1
# ........
# def triangle():
#     L = [1]
#     while True:
#         yield L
#         # L = [1] + [L[i]+L[i+1] for i in range(len(L)-1)]+[1]    #len(L)-1为了防止越界
#         # 或者是下面也行
#         L = [1] + [L[i] + L[i - 1] for i in range(1, len(L))] + [1]
#
# n = 0
# result = []  # 初始化一个列表
# t = triangle()  # t是一个generator，即生成器
# for i in t:
#     print(i)
#     result.append(i)
#     n = n + 1
#     if n == 10:  # 只选择打印9行杨辉三角
#         break

# 2、[1 - 1000],有一个数重复了，只扫描一遍，找出重复数
# list_repetition = []
# for i in range(1, 1001):
#     list_repetition.append(i)
# list_repetition[6] = 6
# l1 = []
# for j in list_repetition:
#     if list_repetition.count(j) > 1:
#         l1.append(j)
# print(l1)

# 求整型列表（每个元素都是0-9的整数）中最长连续元素子串所组成的最大的数值。
# 测试数据
# [1,3,3,3,4,4,4,4,4,0,0,0,4,4,4,4]，此例中由5个连续的4为最大连续子串，返回结果为44444.
# [1,3,3,3,4,4,4,4,4,0,0,0,0,0,0,5,5,5,5]，返回44444;
# [1,3,3,3,5,5,5,5,5,4,4,4,4,4,0,0,0,0,0,0,4,4,4,4]，返回55555;
l = [1,3,3,3,5,5,5,5,5,4,4,4,4,4,0,0,0,0,0,0,4,4,4,4]
# d1 = {}   # 转化成字典
# for i in l:
#     if i not in d1:
#         d1[i] = 1
#     else:
#         d1[i] += 1
# print(d1)

# a = []
# x = []
# y = []
# for i in range(0, len(l)):
#     if i + 1 < len(l):
#         if l[i] == l[i + 1]:
#             x.append(l[i])  # 把相同的放入x列表
#         else:
#             x.append(l[i])
#             a.append(x)    # 不同时，把x放入a
#             x = []
#     else:
#         x.append(l[len(l) - 1])
#         a.append(x)
# for i in a:
#     x = ''
#     for j in i:
#         x += str(j)
#     y.append(int(x))    # 放入新集合，并转化为int
# print(max(y))