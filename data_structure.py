# python数据结构--list--一维列表
list1 = ['阿三', '狗', 2, [2, 3]]
print("---更新前---")
for item in list1:
    print(item)
print(len(list1), len(list1[3]))    # len()计算长度
print(list1[-1])        # 取list的最后一个元素
print(list1[len(list1)-1])      # 取list的最后一个元素
print(list1[0])     # 通过下标索引访问
print("取列表中的列表："+str(list1[3][0]))
list1.append('55')  # 在末尾添加元素
list1.remove("狗")   # 移除指定元素
list1.pop(2)        # 通过索引移除指定位置元素
del list1[1]        # 删除指定位置元素
list1[0] = '阿四'     # 更改元素
print("---更新后---")
for item in list1:
    print(item)

# list--多维列表--二维数组，元素是一维数组
list2 = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [6, 7, 8, 9, 10]]
print(list2[0][0])

# list--三维数组，元素是二维数组
list3 = [[[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]], [[6, 7, 8, 9, 10], [10, 9, 8, 7, 6]]]
print(list3[1][1][0])
