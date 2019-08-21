import random
WORDS = ("python", "jumble", "easy", "difficult", "answer", "continue", "phone",
        "position", "pose", "game")
print(
"""
        欢迎参加猜单词游戏
    把字母组合成一个正确的单词.
"""
)
iscontinue = "y"
while iscontinue == 'y' or iscontinue == 'Y':
    word = random.choice(WORDS)     # 从列表中挑出一个单词
    correct = word      # 判断玩家是否猜对的变量
    jumble = ""     # 创建乱序后的单词
    while word:     # word非空循环
        position = random.randrange(len(word))   # 根据长度产生随机位置
        jumble += word[position]        # 将position位置字母组合到乱序后单词
        word = word[:position] + word[(position + 1):]      # 通过切片把position位置字母从原单词中删除
    print("乱序后单词：", jumble)
    guess = input("\n请你猜：")
    while guess != correct and guess != "":
        print("对不起，不正确！")
        guess = input("继续猜：")
    if guess == correct:
        print("真棒，你猜对了！")
    iscontinue = input("\n是否继续（Y/N）:")