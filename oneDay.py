# -*- coding: utf-8 -*-

print('Art %5d, piece per Unit %8.2f' %(453,59.058))
print(complex(1,2))
while 1:
    print('提示：break为退出指令')
    num = input('输入数字或指令：')
    print(type(num))
    if num=='break':
        break
    else:
        print('转化为十六进制为：%x' % int(num))
print('退出成功')