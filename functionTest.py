
# 函数
# n = 7
# def test():
#     global n    # 引用全局变量
#     if n % 2 == 0:
#         raise Exception('必须是奇数')
#     mid = n // 2 + 1  # 找到中间排
#     i = 1
#     while n > 0:  # 循环n次:1,2,3
#         space_num = abs(mid - i)  # 算出每次循环的空格数:3,2,1
#         base_num = mid - space_num  # 每列中间一半的**数:1,2,3
#         star_num = base_num * 2 - 1  # 计算**数:1,3,5
#         if base_num == 1:
#             print(" " * space_num + "*" * star_num)  # 打印首尾
#         else:
#             print(" " * space_num + "*" + " " * (star_num - 2) + "*")  # 打印有空格部分
#         i += 1
#         n -= 1

# 带参数
# def test(n):
#     if n % 2 == 0:
#         raise Exception('必须是奇数')
#     mid = n // 2 + 1  # 找到中间排
#     i = 1
#     while n > 0:  # 循环n次:1,2,3
#         space_num = abs(mid - i)  # 算出每次循环的空格数:3,2,1
#         base_num = mid - space_num  # 每列中间一半的**数:1,2,3
#         star_num = base_num * 2 - 1  # 计算**数:1,3,5
#         if base_num == 1:
#             print(" " * space_num + "*" * star_num)  # 打印首尾
#         else:
#             print(" " * space_num + "*" + " " * (star_num - 2) + "*")  # 打印有空格部分
#         i += 1
#         n -= 1
# test(7)

# 带返回值
# def discount(amount):
#     amount = amount * 0.8
#     return amount
# print(discount(100))

# 递归
# def test0(n):
#     if n > 16:
#         return n
#     return test0(2 * n)
# print(test0(2))

# 打印1+2+...+100的和
# 递归求和
# def plus(n):
#     if n == 1:
#         return n
#     else:
#         return n + plus(n - 1)
# print(plus(100))

# 递归阶乘
# def jiecheng(n):
# #     if n == 1:
# #         return n
# #     else:
# #         return n * jiecheng(n - 1)
# # print(jiecheng(5))

# 斐波那契数 1 1 2 3 5 8 13 21 34 55 89
# n = 6 --> 8
# n = 7 --> 13
# def fbo(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fbo(n-1) + fbo(n-2)
# print(fbo(11))

# 汉诺塔算法
def hannota(n, x, y, z):    # n是盘子数,x,y,z为形参作为柱子
    if n == 1:  # 递归出口
        print("从", x, '放到', z)
        return              # 返回None
    else:
        hannota(n-1, x, z, y)  # 把x上的n-1个盘子借助z，移动到y上
        hannota(1, x, y, z)    # 把x上最下面的盘子移动到z上
        hannota(n-1, y, x, z)  # 最后把y上的n-1个盘子借助x移动到，z上，大功告成
hannota(9, '盘子X', '盘子Y', '盘子Z')   # 传递实参进去


