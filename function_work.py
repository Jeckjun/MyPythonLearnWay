# 1、请写一个函数，判定一个三位数字是否为水仙花数
# def is_shuixianhua(num):
#     gewei = num % 10
#     shiwei = num // 10 % 10
#     baiwei = num // 100
#     if gewei ** 3 + shiwei ** 3 +baiwei ** 3 == num:
#         return True
#     else:
#         return False

# for i in range(100, 1000):
#     if is_shuixianhua(i):
#         print("{0:d}是水仙花数".format(i))

# 2、不使用自带函数，写一个函数，用于返回一个数的绝对值
# def absolute(num):
#     if num >= 0:
#         return num
#     else:
#         return -num
#
# print(absolute(-8))

# 3、两数值的谐均值可以这样计算：
#  首先对两数值的倒数取平均值，最后再取倒数。
# 编写一个带有两个小数参数的函数，返回两个参数的谐均值。
# def harmmean(num1, num2):
#     num1_d = 1 / num1
#     num2_d = 1 / num2
#     avg_d = (num1_d + num2_d) / 2
#     return 1 / avg_d
#
# print(harmmean(1.2, 2.3))

# 4、写一个函数，返回输入整数（大于0小于10000）的每位数的数字之和。
# 例如：1234    1+2+3+4 = 10
# def int_sum(num):
#     if num < 10:
#         return num
#     else:
#         return num % 10 + int_sum(num // 10)
#
# print(int_sum(1234))

# 5、写一个函数，用来求三个数中的最大数
# def max_num(num1, num2, num3):
#     if num1 > num2:
#         if num1 > num3:
#             return num1
#         else:
#             return num3
#     else:
#         if num2 > num3:
#             return  num2
#         else:
#             return num3
#
# print(max_num(15, 13, 19))

# 6、输入某年某月某日，写一个函数，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
# 特殊情况，闰年且输入月份大于3时需考虑多加一天。
# def year_count(year, month, day):
#     sum = 0
#     for i in range(1, month):
#         if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
#             sum += 31
#         elif i == 4 or i == 6 or i == 9 or i == 11:
#             sum += 30
#         else:
#             sum += 28
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) and month > 2:
#         sum = sum + 1
#     return sum + day
# print(year_count(2019, 5, 30))

# 扩展：
# 1、编写一个函数，传入一个数，判定是否为质数
# def is_zhishu(num):
#     flog = True
#     for i in range(2, num):
#         if num % i == 0:
#             flog = False
#             break
#     return flog
# if is_zhishu(9):
#     print("是质数")
# else:
#     print("不是质数")

# 2、书写一个简洁版的取钱和存钱的功能
# 1）登录函数，传入用户名和密码进行登录；
# 2）登录成功后，可以反复存钱和取钱，直到用户选择退出
# def login(name, password):
#     if name == "aaa" and password == "123":
#         return True
#     else:
#         return False
#
# def money_control_center():
#     balance = 2000
#     print("账户余额为：{0:2f}".format(balance))
#     while True:
#         print("请选择：1.取钱\t2.存钱\t3.退出")
#         status = int(input("请选择指令："))
#         if status == 1:
#             print("取钱中...")
#             draw_money = int(input("输入金额："))
#             if draw_money % 100 == 0:
#                 balance -= draw_money
#                 print("取钱成功，余额为：{0:2f}".format(balance))
#                 continue
#             else:
#                 print("金额无效，请重输!")
#                 continue
#         elif status == 2:
#             print("存钱中...")
#             save_money = int(input("输入金额："))
#             if draw_money % 100 == 0:
#                 balance += save_money
#                 print("存钱成功，余额为：{0:2f}".format(balance))
#                 continue
#             else:
#                 print("金额无效，请重输!")
#                 continue
#         elif status == 3:
#             print("退出用户成功")
#             break
#         else:
#             print("没有该指令")
#             continue
#
# while True:
#     name = input("请输入用户名：")
#     password = input("请输入密码：")
#     if login(name, password):
#         money_control_center()
#     else:
#         print("用户名或密码不正确!")