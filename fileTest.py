# io流
import io
# 读取文件内容
# 方法一
# fileobj = open("C:\\Users\\Administrator\\Desktop\\git.txt")
# fileContent = fileobj.read()  # read(n)可以带参数，表示一次读取n个字符读取文件
# fileobj.close()
# print(fileContent)

# 方法二
# file1 = open("C:\\Users\\Administrator\\Desktop\\git.txt")
# fileContent = ""
# while True:
#     line = file1.readline()   # 一次读取一行字符
#     if line == "":
#         break
#     fileContent += line
# file1.close()
# print(fileContent)

# 方法三
# file2 = open("C:\\Users\\Administrator\\Desktop\\git.txt")
# fileContent = file2.readlines()     # 读取文件返回列表,也可以设置参数，表示一次读取字符数
# file2.close()
# print(fileContent)
# for line in fileContent:
#     print(line)

# 写入数据到文件
# 方法一
# writeFile = open("C:\\Users\\Administrator\\Desktop\\mytxt.txt",'w')    # 打开已存在，会覆盖内容
# writeFile.write("这是第一行\n这是第二行")
# writeFile.close()
# writeFile = open("C:\\Users\\Administrator\\Desktop\\mytxt.txt",'a')    # 追加模式
# writeFile.write("\n这是第三行")
# writeFile.close()

# 方法二
writeFile1 = open("C:\\Users\\Administrator\\Desktop\\mytxt.txt",'w')   # 把列表字符写入文件
list1 = ['你好', '世界', '你好啊', '人类']
writeFile1.writelines(list1)
writeFile1.close()