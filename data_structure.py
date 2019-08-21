# python数据结构--list--一维列表
list1 = ['阿三', '狗', 2, [2, 3]]
list4 = [1, 3, 4]
print(type(list1))
for item in list1:      # 遍历所有list内容，只能一层，递归见下
    if type(item) == list:  # 判断是否是list
        for i in item:
            print(i)
    else:
        print(item)
print("---更新前---")
for item in list1:      # for循环只能循环有长度的，不能循环int、Boolean、float等基本数据类型
    print(item)
print(len(list1), len(list1[3]))    # len()计算长度
print(list1+list4)      # 两个列表连接
print(str(list1))       # 列表转化为字符串，通过str()、list()、tuple()可以实现字符串、列表、元祖的相互转化
print(list1[1:4])       # 截取索引1->4的元素
print(list1[-1])        # 取list的最后一个元素
print(list1[len(list1)-1])      # 取list的最后一个元素
print(list1[0])     # 通过下标索引访问
print("取列表中的列表："+str(list1[3][0]))
list1.append('55')  # 在末尾添加元素
list1.remove("狗")   # 删除指定元素对象，删除第一个匹配到的元素
list1.pop(2)        # 通过索引移除指定位置元素,不给参数删除最后一个元素
del list1[1]        # 删除指定位置元素
list1[0] = '阿四'     # 更改元素
list1.insert(0, '我来了')  # 在索引位置添加元素
print("---更新后---")
for item in list1:
    print(item)

# 递归列表中的所有list元素
list5 = [1, 2, 3, [4, 5, 6, [7, 8, 9, [10, 11, 12]]]]
def for_list(lists):    # 写完函数一定要记得调用
    for item in lists:
        if type(item) == list:
            for_list(item)
        else:
            print(item)
for_list(list5)     # 函数要调用才能使用

# list--多维列表--二维数组，元素是一维数组
list2 = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [6, 7, 8, 9, 10]]
print(list2[0][0])

# list--三维数组，元素是二维数组
list3 = [[[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]], [[6, 7, 8, 9, 10], [10, 9, 8, 7, 6]]]
print(list3[1][1][0])

# 声明后再添加
l = []
for i in range(10):
    l.append(i)
# for i in 'SML':
#     for j in ['blue', 'red', 'yellow']:
#         l.append((i, j))
# print(l)

# 列表生成式，快速
import random
l1 = [i for i in 'abcdefg']
l2 = [random.randint(0, 10) for i in 'abcdefg']
l3 = [(i, j) for i in 'SML' for j in ['blue', 'red', 'yellow']]
print(l1)
print(l2)
print(l3)

# 切片
print(l[0:5])   # 切片0-5
print(l[:5])    # 切片0-5
print(l[5:])    # 切片5到末尾
print(l[-1])    # 取最后一个元素
print(l[0:8:2])     # 2为step，跳两步，间隔切片
print(l[::-1])  # 倒着切片
print(l[9::-1])    # 倒着切片
print(l[::-2])  # 倒着隔两步切片
print(l[7:2:-1])    # 倒着部分切片

# 排序
l.sort(reverse=True)    # reverse=True降序
l.sort(reverse=False)   # reverse=False升序
print(l)
def takeSecond(elem):   # 获取列表第二个元素
    return elem[1]
num_list = [(1, 2), (2, 4), (4, 8), (8, 10)]
num_list.sort(key=takeSecond, reverse=True)
print(num_list)

# 练习，打印扑克牌
pokes_type = ['梅花', '方板', '红桃', '黑桃']
pokes_num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
pokes = [(j+i) for i in pokes_num for j in pokes_type]
print(pokes)
print(pokes[len(pokes)-4:])

# dict字典
d1 = {'李白': '白', '杜甫': '黑', '王安石': '宰相', '岳飞': '忠义'}
d2 = {'杨过': '雕侠', '郭靖': '大侠'}
print(d1.values())      # 输出值value
print(d1.keys())        # 输出键key
print(d1.items())       # 输出dict内容
d1.clear()
print(d1.get('李白', '没有'))   # 没有输出'没有'
print(d1.items())
print(d1.setdefault('李白', '没有'))    # 没有输出'没有'，并加入到dict
print(d1.items())
d1['李白'] = '风流'     # 更新
print(d1['李白'])
d1.update(d2)       # 批量更新
print(d1)
seq = (1, 2, 3)
d = d1.fromkeys(seq, 0)     # seq对应键，值为0，返回新dict
print(d)
d.popitem()     # 随机删除键值对，一般末尾
print(d)
d.pop(1)        # 删除指定键和值
print(d)
d3 = d1.copy()  # 浅复制
print(d3)

# 用dict优化斐波拉契数递归函数
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        if d.get(n - 1, False):
            f1 = d.get(n - 1)
        else:
            f1 = fib(n - 1)
            d[n - 1] = f1
        if d.get(n - 2, False):
            f2 = d.get(n - 2)
        else:
            f2 = fib(n - 2)
            d[n - 1] = f2
        return f1 + f2

print(fib(700))

# tuple元祖，不可变
t1, t2 = ('你好', '25')       # 拆包
t3 = (25, 35, 'hello', '你好')
t4 = ('一个',)
print(t1)
print(t2)
print(t3)
print(t4)
