# 1、书写一个程序，用户输入一个数字（圆的半径）要求输出该圆的半径、周长和面积，输出格式如下：
# 	 该圆半径为：xx
# 	 该圆周长为：xx
# 	 该圆面积为：xx
# r = float(input('请输入圆的半径：'))
# print('圆的半径为：{0:0.2f}'.format(r))
# print('圆的周长为：{0:0.2f}'.format(2*3.14*r))
# print('圆的面积为：{0:0.2f}'.format(3.14*r*r))

# print(1 + 10 * 2 / 2 - 5)
# print(3.0 / 5)
# print(3.0 // 5)
# print('a' * 10)
# print(True + 3)
# print(False + 3)
# print('hello' > 'world')
# print('h' > 1)

# a = '''5'''
# python = """5"""
# print(python)

# 4. 定义一个变量。用来存储我卡上有100块钱，到银行存了1000块钱，打印输出现在我卡上多少钱
# myMoney = 100
# print('存入一千元\n卡上余额为：{0:0.2f}'.format(myMoney+1000))

# 5、班费有199块钱，买了30支笔，每支笔2.5元，买了5个杯子，5元一个，打印输出班费还剩多少钱？
# def buyThing(allMoney, penNum, penPrice, cupNum,cupPrice):
#     return allMoney - (penNum * penPrice + cupNum * cupPrice)
# print('剩余金额：{0:0.2f}'.format(buyThing(199,30,2.5,5,5)))

# 6. 使用运算符，求19的个位打印输出；求29的十位数字打印输出；189的每位数字输出；
# def numPrint(num):
#     if num == 19:
#         print('19的个位输出为：{0:d}'.format(num % 10))
#     if num == 29:
#         print('29的十位输出为：{0:d}'.format(num // 10))
#     if num == 189:
#         print('189的个位输出为：{0:d}'.format(num % 10))
#         print('189的十位输出为：{0:d}'.format(num // 10 % 10))
#         print('189的百位输出为：{0:d}'.format(num // 100))
# numPrint(19)
# numPrint(29)
# numPrint(189)

# 7 、已知一个学生两科成绩：语文90；英语66；求该学生总成绩和平均成绩
# def analyzeScore(ch,en):
#     allScore = ch + en
#     avgScore = (ch + en) / 2
#     print('总成绩为：{0:0.1f}\n平均成绩为：{1:0.2f}'.format(allScore,avgScore))
# analyzeScore(90,66)

# 8、已知正方形边长为4，求正方形周长和面积
# def square(len):
#     area = len**2
#     perimeter = len*4
#     print('面积为：{0:0.2f}\n周长为：{1:0.2f}'.format(area, perimeter))
# square(4)

# 9、已知一个圆半径为3.5，声明一个变量名为radius存储该圆半径，要求输出该圆的半径、周长和面积
radius = 3.5
def circle(radius):
    area = 3.14 * radius ** 2
    perimeter = 2 * 3.14 * radius
    print('半径为：{0:0.2f}\n面积为：{1:0.2f}\n周长为：{2:0.2f}'.format(radius,area, perimeter))
circle(radius)