
# print(1<<2)
# print(2<<2)
# print(3<<2)
# print(4<<4)
# print(8>>2)
# print(64>>4)
'''
1 0 1 0
1 0 1 1
--------
1 0 1 1
'''
# print(10 | 11)
'''
1 0 1 0
1 0 1 1
--------
0 0 0 1
'''
# print(10 ^ 11)
"""
1 0 1 0
1 0 1 1
--------
1 0 1 0
"""
# print(10 & 11)

# if选择结构
# is_not = True
# price = float(input('goods price：'))
# if is_not == True:        # 在内部完成想要的结果
#     print("member打8折：{0:0.2f}".format(price*0.8))
# if is_not == False:
#     print('nonmember不打折：{0:0.2f}'.format(price))
# else:
#     print('nonmember不打折：{0:0.2f}'.format(price))
# if is_not:      # 在内部只改变需要变量的值
#     price = price * 0.8
# print('price：{0:0.2f}'.format(price))

# 练习
# price = float(input('花费金额：'))
# if price > 400:
#     price = price * 0.85
#     print("折后金额：{0:0.2f}".format(price))
# elif 0 <= price <= 400:
#     price = price * 0.95
#     print("折后金额：{0:0.2f}".format(price))
# else:
#     print("输入金额非法")

# 课堂练习
# while True:
#     score = int(input("输入分数："))
#     if score < 0 or score >100:
#         break
#     elif score >= 90:
#         print("A")
#     elif 80 <= score <=89:
#         print("B")
#     elif 70 <= score <= 79:
#         print("C")
#     elif 60 <= score <=69:
#         print("D")
#     else:
#         print("F")

# other method
# flog = True
# while flog:
#     score = int(input("输入分数："))
#     if score < 0 or score >100:
#         flog = False
#     elif score >= 90:
#         print("A")
#     elif 80 <= score <=89:
#         print("B")
#     elif 70 <= score <= 79:
#         print("C")
#     elif 60 <= score <=69:
#         print("D")
#     else:
#         print("F")

# practice
# count = 0
# sumGrade = 0
# while count < 5:
#     grade = int(input("请输入第{0:d}课成绩：".format(count+1)))
#     if grade < 0 or grade > 100:
#         print("成绩输入无效，请重新输入")
#         continue
#     sumGrade += grade
#     count += 1
# print("总成绩为：{0:d}\n平均成绩为：{1:0.2f}".format(sumGrade,sumGrade / count))

# 或者

# if price < 0:
#     print("输入金额非法")
# else:
#     if price > 400:
#         price = price * 0.85
#     else:
#         price = price * 0.95
#     print("折后金额：{0:0.2f}".format(price))


# while循环
# i = 0
# sum1 = 0
# while i < 10:
#     sum1 += i
#     i += 1
# print(sum1)

# for循环
# sum2 = 0
# for i in range(1,10,2):
#     sum2 += i
#     print(i)
# print(sum2)
