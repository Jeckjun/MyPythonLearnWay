import random
# Card Module
class Card():
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']  # 牌面数字列表
    SUITS = ['梅', '方', '红', '黑']   # 牌花色列表
    # 定义构造函数
    def __init__(self, rank, suit, face_up = True):
        self.rank = rank    # 牌面数字
        self.suit = suit    # 花色
        self.is_face_up = face_up   # 是否显示牌正面

    def __str__(self):  # 重写print()方法，打印一张牌的信息
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = 'XX'
        return rep

    def pic_order(self):    # 牌的顺序号
        if self.rank == 'A':
            FaceNum = 1
        elif self.rank == 'J':
            FaceNum = 11
        elif self.rank == 'Q':
            FaceNum = 12
        elif self.rank == 'K':
            FaceNum = 13
        else:
            FaceNum = int(self.rank)
        if self.suit == '梅':
            Suit = 1
        elif self.suit == '方':
            Suit = 2
        elif self.suit == '红':
            Suit = 3
        else:
            Suit = 4
        return (Suit - 1) * 13 + FaceNum

    def filp(self):
        self.is_face_up = not self.is_face_up

# 手牌类
class Hand():
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + '\t'
        else:
            rep = '无牌'
        return  rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

# 牌类
class Poke(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 13):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                else:
                    print('不能继续发牌了，牌已经发完！')

# 程序主程序
if __name__=='__main__':
    print('开始游戏')
    players = [Hand(), Hand(), Hand(), Hand()]
    poke1 = Poke()
    poke1.populate()    # 生成一副牌
    poke1.shuffle()     # 洗牌
    poke1.deal(players, 13)     # 发给玩家每人13张牌
    # 显示4位牌手的牌
    n = 1
    for hand in players:
        print('牌手',n , end = ":")
        print(hand)
        n=n+1
        input('输入回车键继续')