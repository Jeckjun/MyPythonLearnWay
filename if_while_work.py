# 判定一个输入的整数是否为偶数
# num = int(input("输入偶数："))
# if num % 2 == 0:
#     print("是偶数")
# else:
#     print("不是偶数")
#
# # 验证自己是否成年(18岁及以上属于成年)
# age = int(input("输入年龄："))
# if age >= 18:
#     print("已成年")
# else:
#     print("未成年")

# 闰年问题（输入一个年份，判断是否为闰年）
# 能被4整除 不能被100整除
# 或者能被400整除
# year = int(input("输入年份："))
# if year % 400 == 0:
#     print("是闰年")
# elif year % 4 ==0 and year % 100 != 0:
#     print("是闰年")
# else:
#     print("不是闰年")

# 小明身高1.75，体重80kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25以下：正常
# 25-28以下：过重
# 28-32：肥胖
# 高于32：严重肥胖
# height = float(input("输入身高(单位米)："))
# weight = float(input("输入体重（单位kg）："))
# BMI = weight / height**2
# if BMI < 18.5:
#     print("过轻")
# elif 18.5 <= BMI <= 25:
#     print("正常")
# elif 25 < BMI <= 28:
#     print("过重")
# elif 28 < BMI <= 32:
#     print("肥胖")
# else:
#     print("严重肥胖")

# 购买车票，输入身高，判定1.2m以下输出购买儿童票；其他输出成人票
# height = float(input("输入身高（单位米）："))
# if height <= 1.2:
#     print("购买儿童票")
# else:
#     print("购买成人票")

# 输入温度，查看温度适宜问题（15度以下寒冷，15-29度舒适，30度及以上炎热)
# temperature = float(input("输入温度："))
# if temperature < 15:
#     print("寒冷")
# elif 15 <= temperature <= 29:
#     print("舒适")
# else:
#     print("炎热")

# 今天老板找我到办公室，说要调整薪资，输入老板说的薪资，输出我此刻的心情（条件和心情自由设定）
# salary = int(input("输入工资："))
# if salary < 8000:
#     print("心情不爽")
# elif 8000 <= salary <= 20000:
#     print("有点小激动")
# elif 20000 < salary <= 50000:
#     print("开心极了")
# else:
#     print("走上人生巅峰")

# 输入一个成绩，如果考试成绩大于 90 分，则奖励一个 IPHONE 8S ，如果成绩介于 70 分至 90 分之间，则奖励一个小米，否则罚做 500 个俯卧撑。
# grade = int(input("输入成绩："))
# if grade < 70:
#     print("罚做 500 个俯卧撑")
# elif 70 <= grade <= 90:
#     print("奖励小米9一部")
# else:
#     print("奖励一个IPHONE 8S")

# 在游乐场中，门票全票价位10美元
# 4岁以下免费；
# 4~18岁收费3美元；
# 18岁（含）以上收费10美元。
# 对于65岁（含）以上的老人，可以半价（即5美元）购买门票，输入年龄，查看需要多钱购买门票
# age = int(input("输入年龄："))
# if age >= 65:
#     print("门票5美刀")
# elif 18 <= age < 65:
#     print("门票10美刀")
# elif 4 < age < 18:
#     print("门票3美刀")
# else:
#     print("门票免费")

# 某单位马上要加工资，增加金额取决于工龄和现工资两个因素：
# 对于工龄大于等于20年的，如果现工资高于2000，加200元，否则加180元；
# 对于工龄小于20年的，如果现工资高于1500，加150元，否则加120元。工龄和现工资从键盘输入，编程求出一个员工加工资后的工资。
# workYear = int(input("输入工龄："))
# salary = int(input("输入工资："))
# if workYear >= 20:
#     if salary > 2000:
#         salary += 200
#     else:
#         salary += 180
# else:
#     if salary > 1500:
#         salary += 150
#     else:
#         salary += 120
# print("加薪工资为：{0:d}".format(salary))

# 请写1个ATM程序.定义1个变量,用来存储该ATM机器中剩余的金额.
# 接收用户输入取款金额.由于ATM机器只支持100的票子.
# 如果用户输入的取款金额不是100的倍数的话.则打印 "对不起,本机器无法提供输入的面额"
# 如果用户输入的取款金额大于了ATM的剩余金额.则打印 "对不起,余额不足."
# 如果用户输入的取款金额是100的倍数,并且小于等于ATM的剩余金额就打印."正在出钞,请从出钞口拿钱.ATM机器剩余xx元
# money = 50000
# drawMoney = int(input("输入取钱金额："))
# if drawMoney > money:
#     print("对不起,余额不足")
# elif drawMoney % 100 != 0:
#     print("对不起,本机器无法提供输入的面额")
# else:
#     print("正在出钞,请从出钞口拿钱.ATM机器剩余{0:d}元".format(money - drawMoney))

# 输入一个数，判定该数是否为质数
# num = int(input("输入一个数："))
# flog = True
# for i in range(2,num):
#     if num % i == 0:
#         flog = False
#         break
# if flog:
#     print("是质数")
# else:
#     print("不是质数")

# 封装函数
# def is_sushu(num):
#     flog = True
#     for i in range(2,num):
#         if num % i == 0:
#             flog = False
#             break
#     return flog
# n = 100
# while n > 0:
#     if is_sushu(n):
#         print(n, end=" ")
#     n -= 1

# 或者
# num = int(input("输入一个数："))
# flog = True
# i = 2
# while i < num:
#     if num % i == 0:
#         flog = False
#         break
#     i += 1
# if flog:
#     print("是质数")
# else:
#     print("不是质数")

# 求 100-200以内同时能被7、8整除的数
# i = 100
# while i < 200:
#     if i % 7 == 0 and i % 8 == 0:
#         print(i)
#     i += 1
# 或者
# for i in range(100, 200):
#     if i % 7 == 0 and i % 8 == 0:
#         print(i)
#
# # 求 1-100以内所有含6的数
# for i in range(100):
#     if i % 10 == 6 or i // 10 == 6:
#         print(i)
#     i += 1
# 或者
# i = 0
# while i < 100:
#     if i % 10 == 6 or i // 10 == 6:
#         print(i)
#     i += 1

# 使用while和if，实现求100以内，个位数和十位数相等的两位数
# i = 10
# while i < 100:
#     if i % 10 == i // 10:
#         print(i)
#     i += 1

# 求 0 -1 + 2 - 3 + 4 - 5 + 6 -7.... + 100
# sum = 0
# for i in range(0,101):
#     if i % 2:
#         sum += -i
#     else:
#         sum += i
# print(sum)

# Chuckie Lucky赢了100W美元，
# 他把它存入一个每年盈利8%的账户。
# 在每年的最后一天，Chuckie取出10W美元。
# 编写一个程序，计算需要多少年Chuckie就会清空他的账户。
# year = 1
# money = 100
# while True:
#     money = money * 1.08 - 10
#     if money < 0:
#         break
#     year += 1
#     print(money)
# print(year - 1)

# 输入班级学生语文成绩，求总成绩和平均成绩 。班级人数从键盘输入
# number = int(input("输入班级人数："))
# i = 0
# sum = 0
# while i < number:
#     grade = int(input("输入第{0:d}位同学语文成绩：".format(i+1)))
#     sum += grade
#     i += 1
# print("总成绩：{0:d}\t平均成绩：{1:0.2f}".format(sum,sum / i))

# 循环输入7天温度，求平均温度
# i = 0
# sum = 0
# while i < 7:
#     temp = int(input("输入第{0:d}天温度：".format(i+1)))
#     sum += temp
#     i += 1
# print("平均成绩：{0:0.2f}".format(sum / i))

# 依次输入几个数据，直到0作为输入的结束， 然后求出输入的这些数据的总和及平均值（0不算次数）；
# i = 0
# sum = 0
# while True:
#     num = int(input("输入第{0:d}个数：".format(i+1)))
#     if num == 0:
#         print("总和：{0:d}\t平均成绩：{1:0.2f}".format(sum, sum / i))
#         break
#     sum += num
#     i += 1

# 求1000-5000之间，各位数字之和为5的所有整数，打印输出（例如整数2003的各位数字之和为2+0+0+3，等于5）
# for i in range(999, 5001):
#     if i % 10 + i // 10 % 10 + i // 100 % 10 + i // 1000 == 5:
#         print(i)

# 从键盘输入10个数，求出最大数
# i = 0
# flog = int(input("输入第1个数："))
# while i < 4:
#     num = int(input("输入第{0:d}个数：".format(i+2)))
#     if num > flog:
#         flog = num
#     i += 1
# print("最大数为：{0:d}".format(flog))

# 输入一个五位以内的数，求每位数字之和
# num = int(input("输入一个5位以内的数："))
# sum = num // 10000 + num // 1000 % 10 + num // 100 % 10 + num // 10 % 10 + num % 10
# print(sum)

# 从键盘输入两个正整数，输出这个范围内的所有偶数： 如：输入 3 和9， 输出4 6 8
# min = int(input("输入一个整数："))
# max = int(input("输入比上一个大的整数："))
# for i in range(min, max+1):
#     if i % 2 == 0:
#         print(i)

# 从键盘输入一个正整数x，打印输出从0开始的连续n个偶数，如 x = 5,输出 0 2 4 6 8
# num = int(input("输入一个正整数："))
# j = 0
# for i in range(num):
#     print(j, end=" ")
#     j += 2

# 使用循环完成猜数字游戏，确定一个1-100的随机数（整数），提示用户输入数字进入猜的模式；
# 输入数字后，如果与随机数（整数）相同，提示用户猜成功了；
# 输入数字后，如果与随机数（整数）不相同，提示用户猜大一点或者小一点；
# 记录猜的次数，如果猜的次数小于三次，则赞赏，真聪明
# 如果大于等于3次小于10次，则表示，要加油哦
# 随机数获取：百度  python3 random 关键字，查询资料获得
# import random
# random = random.randint(1, 100)
# count = 0
# while True:
#     num = int(input("猜数字："))
#     if num > random:
#         print("太大了")
#     elif num < random:
#         print("太小了")
#     else:
#         print("恭喜你，猜对了")
#         break
#     count += 1
# print("你一共猜了{0:d}次".format(count+1))
# if count + 1 < 3:
#     print("真聪明")
# elif 3 <= count + 1 < 10:
#     print("要加油哦")
# else:
#     print("你是猪么")

# 打印100-999中不能被7整除又不包含7的数
# for i in  range(100,1000):
#     if i % 7 == 0:
#         continue
#     if i // 100 != 7 and i % 10 != 7 and i // 10 % 10 != 7:
#         print(i)

# while循环作业2019.08.15
# 1、求 100-200以内同时能被2、3、5整除的第一个数
# i = 100
# while i <= 200:
#     if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
#         print(i)
#         break
#     i += 1

# 2、打印200以内能被7整除又不包含7的数
# i = 1
# while i <= 200:
#     if i % 7 == 0:
#         if i % 10 != 7 and i // 100 != 7 and i // 10 % 10 != 7:
#             print(i)
#     i += 1

# 3、9*9乘法表输出
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("{1:d}x{0:d}={2:d}".format(i,j,i*j),end=" ")
#         j += 1
#     i += 1
#     print()

# 4、求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
# count = int(input("输入相加次数："))
# i = 1
# a = 2
# sum = 0
# while i <= count:
#     sum += a**i
#     i += 1
# print(sum)
# 字符串转化数字
# n = int(input("输入相加次数: "))
# total = 0
# a = "2"
# while n > 0:
#     number = a*n
#     total += int(number)
#     n -= 1
# print(total)

# 5、一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在 第10次落地时，共经过多少米？第10次反弹多高？
# height = 100
# count = 1
# sum = 0
# while count <= 10:
#     height = height / 2
#     sum += height
#     count += 1
#     print(height)
# print((sum-height)*2+100, height)

# 打印以下图形
"""
      *********
      *       *
      *       *
      *********
"""
# n = 4
# while n > 0:
#     if n == 1 or n == 4:
#         print("*" * 9)
#     else:
#         print("*" + " " * 7 + "*")
#     n -= 1

# 优化
# w = 12  # 长度
# h = 10  # 高度
# i = h
# while i > 0:
#     if h == i or i == 1:
#         print('*' * w)
#     else:
#         print('*' + " " * (w - 2) + '*')
#     i -= 1
"""
*******
 *****
  ***
   *
  ***
 *****
*******
"""
# line = 7
# if line % 2 == 0:
#     raise Exception('必须是奇数')
# else:
#     star_num = line
#     j = 0
#     space_num = line // 2  # 第一排空格的规律
#     while j < line:
#         print(" " * space_num + "*" * star_num)  # 打印结果
#         if j < line // 2:  # 程序运行前半部分
#             star_num -= 2  # 星星数等差2增加
#             space_num += 1  # 空格等差1减少
#         else:  # 程序运行后半部分
#             star_num += 2  # 星星等差2减少
#             space_num -= 1  # 星星等差1增加
#         j += 1
# 方法二
# n = 9
# i = 1
# mid = n//2 + 1  # 中间
# while n >= i:
#     if i <= mid:
#         space_num = i - 1
#         base_num = mid + 1 - i
#     else:
#         space_num = n - i
#         base_num = i - mid + 1
#     star_num = base_num * 2 - 1
#     print(" "*space_num + '*'*star_num)
#     i += 1
"""
     A
    ABA
   ABCBA
  ABCDCBA
 ABCDEDCBA
ABCDEFEDCBA
"""
# char = 'E'
# for i in range(ord(char)-65+1):
#     # 空格数量
#     space = ord(char) - ord('A') - i
#     for s in range(space):
#         print(' ', end='')
#     # 补前半部分
#     for c in range(i + 1):
#         print(chr(c + 65), end='')
#     # 补后半部分
#     reverse = i + 65
#     while reverse > 65:
#         reverse -= 1
#         print(chr(reverse), end='')
#     print()

# 数字版本
# num = 5
# for i in range(1, num+1):
#     # 空格数量
#     space = num - i
#     for s in range(space):
#         print(' ', end='')
#     # 补前半部分
#     for c in range(1, i + 1):
#         print(c, end='')
#     # 补后半部分
#     reverse = i
#     while reverse > 1:
#         reverse -= 1
#         print(reverse, end='')
#     print()
# 其他版本
# i = 0
# floor = 6
# bias = 64
# while i < floor:
#     space_num = floor - i #空格数量
#     k = 1  #需要循环的次数
#     j = i - 1
#     string = ""
#     while k < 2*i:
#         if k <= i:
#             num = k
#         else:
#             num = j
#             j -= 1
#         k += 1
#         string += chr(num + bias)
#     i += 1
#     print(" "*space_num + string)
# 自己联习
# line = 5
# i = 0
# while i < line:
#     print(" "*(line-i), end=" ")
#     j = 0
#     while j < i+1:
#         print(j+1, end="")
#         j += 1
#     while j > 1:
#         j -= 1
#         print(j, end="")
#     i += 1
#     print()
"""
******
*****
****
***
**
*
"""
# line = 6
# while line > 0:
#     print("*"*line)
#     line -= 1
