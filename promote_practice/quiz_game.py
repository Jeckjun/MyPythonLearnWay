# 智力问答游戏
import sqlite3
# 连接数据库，文件是question.db，没有则创建
conn = sqlite3.connect("C:\\Users\\Administrator\\Desktop\\question.db")
# 创建游标
cursor = conn.cursor()
