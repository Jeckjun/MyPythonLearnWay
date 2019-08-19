# 随机排序
# import random
# lists = ["张三", "李四", "王二", "麻子", "皮特", "鲍勃", "苏珊", "阿三"]
# newList = []
# for i in range(1, len(lists)+1):
#     name = random.choice(lists)
#     newList.append(name)
#     lists.remove(name)
# print(newList)


# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{0:d}x{1:d}={2:d}".format(j, i, i*j), end="\t")
#     print()

# 使用while
# i = 1
# while i < 10:
#     j = 1
#     while j < i+1:
#         print("{0:d}x{1:d}={2:d}".format(j, i, i * j), end="\t")
#         j += 1
#     i += 1
#     print()

# 反的九九乘法表
# for i in range(1, 10):
#     for j in range(1, 11-i):
#         print("{0:d}x{1:d}={2:d}".format(i, 10-j, i*j), end="\t")
#     print

# 使用while
# i = 1
# while i < 10:
#     j = 1
#     while j < 11-i:
#         print("{0:d}x{1:d}={2:d}".format(i, 10-j, i * j), end="\t")
#         j += 1
#     i += 1
#     print()

# n = 1
# while n <= 9:
#     j = 1
#     content = ""
#     while j <= 10-n:
#         content += ("{0:2d} x{1:2d}={2:2d} |".format(n, 10-j, n * j))
#         j += 1
#     print(content)
#     n += 1

# 或者用-=
# n = 1
# while n <= 9:
#     j = 9
#     content = ""
#     while j >= n:
#         content += ("{0:2d} x{1:2d}={2:2d} |".format(n, j, n * j))
#         j -= 1
#     print(content)
#     n += 1

"""
   1
  2 3
 4 5 6
7 8 9 0
"""
# n = 4
# i = 1
# space_num = n - 1
# while space_num >= 0:
#     string = (" "*space_num)  # 打印前面的空格
#     j = 0
#     while n - space_num > j:    # 循环行数
#         string += str(i % 10) + " "     # 拼接
#         i += 1
#         j += 1
#     print(string)
#     space_num -= 1

# n = 5
# i = 1
# while n >= i:
#     print("*"*n)
#     n -= 1

"""
     *
    **
   ***
  ****
 *****
******
"""
# n = 6
# start_num = 1
# j = 0
# while j < n:
#     space_num = n - start_num
#     print(" "*space_num+"*"*start_num)
#     start_num += 1
#     j += 1

"""
******
 *****
  ****
   ***
    **
     *
"""
# n = 6       # 行数
# start_num = 6       # 开始*的个数
# j = 0
# while j < n:
#     space_num = n - start_num   # 计算每行的空格数
#     print(" "*space_num+"*"*start_num)  # 打印每行的内容
#     start_num -= 1
#     j += 1

# 简化版
# line = 6
# j = 0
# while j < line:        # 循环行数，每行的空格数等于j
#     print(" "*j + "*"*(line-j))     # 行数空格*的规律：j = 空格数，line - j = *数
#     j += 1

"""
   *
  ***
 *****
*******
 *****
  ***
   *
"""
# 必须是基数
# def starArrange(line):
#     if line % 2 == 0:
#         raise Exception('必须是奇数')
#     else:
#         star_num = 1
#         j = 0
#         space_num = line // 2   # 第一排空格的规律
#         while j < line:
#             print(" "*space_num + "*"*star_num)     # 打印结果
#             if j < line // 2:       # 程序运行前半部分
#                 star_num += 2       # 星星数等差2增加
#                 space_num -= 1      # 空格等差1减少
#             else:                   # 程序运行后半部分
#                 star_num -= 2       # 星星等差2减少
#                 space_num += 1      # 星星等差1增加
#             j += 1
# starArrange(4)
# 老师的方法
# n = 7
# if n % 2 == 0:
#     raise Exception('必须是奇数')
# mid = n // 2 + 1    # 找到中间排
# i = 1
# while n > 0:        # 循环n次:1,2,3
#     space_num = abs(mid - i)        # 算出每次循环的空格数:3,2,1
#     base_num = mid - space_num      # 每列中间一半的**数:1,2,3
#     star_num = base_num * 2 - 1     # 计算**数:1,3,5
#     print(" " * space_num + "*" * star_num)     # 打印结果
#     i += 1
#     n -= 1

# 绝对值函数
# print(abs(-8))
"""
   *
  * *
 *   *
*     *
 *   *
  * *
   *
"""
# n = 7
# if n % 2 == 0:
#     raise Exception('必须是奇数')
# mid = n // 2 + 1    # 找到中间排
# i = 1
# while n > 0:        # 循环n次:1,2,3
#     space_num = abs(mid - i)        # 算出每次循环的空格数:3,2,1
#     base_num = mid - space_num      # 每列中间一半的**数:1,2,3
#     star_num = base_num * 2 - 1     # 计算**数:1,3,5
#     if base_num == 1:
#         print(" " * space_num + "A" * star_num)  # 打印首尾
#     else:
#         print(" " * space_num + "A" + " " * (star_num-2)+"A")     # 打印有空格部分
#     i += 1
#     n -= 1

# 字母金字塔
def pyramid(char: str) -> None:
    row = ord(char) - ord('A') + 1
    for i in range(row):
        # whitespace
        space = ord(char) - ord('A') - i
        for s in range(space):
            print(' ', end='')
        # part one
        for c in range(i+1):
            print(chr(c+65), end='')
        # part two
        reverse = i+65
        while reverse > 65:
            reverse -= 1
            print(chr(reverse), end='')
        # newline
        print()
def numCount(num):
    alphabet = [chr(i) for i in range(65, 65 + num)]
    for char in alphabet:
        pyramid(char)
numCount(26)
