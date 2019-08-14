class Person:
    name = None
    age = None
    __height = None
    __weight = None
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.__height = height
        self.__weight = weight
    @ staticmethod              # 定义静态方法，不需要self
    def eat(name1):
        print(name1+'正在吃饭')
    def work(self,name):        # 定义公有方法，需要self
        print(name+'正在工作')
    def __run(self,name):       # 定义私有方法，需要self
        print(name+'正在跑步')
if(__name__=='__main__'):       # 主函数入口
    p1 = Person('张三',20,170,50)
    p2 = Person('李四',21,180,60)
    print(p1.name)
    print(p2.name)              # 调用公有成员变量
    print(p1._Person__height)
    print(p2._Person__weight)   # 外部调用私有成员变量
    Person.eat(p1.name)         # 静态方法调用
    p1.work(p2.name)            # 调用公有方法
    p2._Person__run(p1.name)    # 外部调用类私有方法
    def talk(content):          # 定义外部方法
        print('我说了:'+content)
    talk('你好，世界')           # 调用函数
