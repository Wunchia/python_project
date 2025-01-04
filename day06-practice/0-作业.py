# Author Wunchia
# 2024年12月30日18时59分40秒
# wunchia@outlook.com

# 1、练习封装案例（和上课保持一致即可）
class  Gun():
    def __init__(self, module):
        self.module = module
        self.Max =50
        self.fire=10
        self.buttle_count=0

    def add_buttle(self,num):
        for i in range(num):
            if i <= self.Max:
                self.buttle_count+=1
        else:
            print(f"{self.module}已装满")

    def __str__(self):
        return self.module

class Solider:
    def __init__(self,name,gun:Gun=None):
        self.name = name
        self.havegun=False
        self.blood=100

    def speak(self):
        if self.havegun:
            print(f"my name is {self.name},my gun is {self.gun.__str__()}")
        else:
            print(f"my name is {self.name}")

    def pick_gun(self,gun:Gun):
        self.gun=gun
        self.havegun=True

    def pick_buttle(self, buttle):
        self.gun.buttle_count = buttle

    def fire(self,solider):
        if self.havegun:
            if self.gun.buttle_count > 0:
                print(f'{self.name}开火成功')
                solider.attacked(self.gun)
            else:
                print(f'{self.name}开火失败，没子弹')

    def attacked(self,gun:Gun):
        self.blood-=gun.fire
        print(f"{self.name} blood is {self.blood}")

def solder_main():
    gun01=Gun('AK47')
    gun02=Gun('M16')
    solder01=Solider('A')
    solder02=Solider('B')
    solder01.speak()
    solder01.pick_gun(gun01)
    solder02.pick_gun(gun02)
    solder01.speak()
    solder02.pick_buttle(60)
    solder02.gun.add_buttle(60)
    solder02.speak()
    solder02.fire(solder01)
    solder01.fire(solder02)

if __name__ == '__main__':
    solder_main()


# 2、练习私有属性和私有方法（和上课保持一致即可）
class Agent():
    def __init__(self, name,code):
        self.name = name
        self.__code = code
    def __getcode(self):
        print(f"I'm {self.name},code is {self.__code}")
    def coworker(self):
        self.__getcode()

if __name__ == '__main__':
    agent = Agent('A',114514)
    agent.coworker()


# 3、练习单继承，多重继承案例（和上课保持一致即可）
#单继承
class Animal:
    def __init__(self, name,color):
        self.name = name
        self.color = color

    def eat(self):
        print(f"{self.name} eats")

    def run(self):
        print(f"{self.name} runs")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")

class Xtq(Dog):
    def run(self):
        print(f"{self.name} runs in the sky")

def test_main01():
    dahuang=Dog("dahuang",'yellow')
    xtq=Xtq("xtq",'black')
    print(f"大黄的颜色是{dahuang.color}")
    print(f"哮天犬的颜色是{xtq.color}")
    dahuang.run()
    xtq.run()

#多重继承
class Parent:
    def __init__(self,name,*args):
        self.name = name
        super().__init__(*args)
class A(Parent):
    def __init__(self,age,*args):
        self.age = age
        super().__init__(*args)
    def test(self):
        print('test_A')
class B(Parent):
    def __init__(self,height,*args):
        self.height = height
        super().__init__(*args)

    def test(self):
        print('test_B')

class C(A,B):
    def __init__(self,score,*args):
        self.score = score
        super().__init__(*args)

def test_main02():
    c=C(125.5,19,170,'xiaoming')
    c.test()
    print(C.__mro__)
    print(c.name)
    print(c.age)
    print(c.score)
    print(c.height)

if __name__ == '__main__':
    test_main01()
    test_main02()


# 4、实现单例模式（和上课保持一致即可）
class MusicPlayer:
    instance=None
    def __new__(cls, *args, **kwargs):
        if cls.instance==None:
            cls.instance=super().__new__(cls)
        return cls.instance

    def __init__(self,name):
        self.name=name

if __name__ == '__main__':
    a=MusicPlayer('A')
    b=MusicPlayer('B')
    print(id(a),id(b))
    print(a.name,b.name)


# 5、通过try进行异常捕捉，确保输入的内容一定是一个整型数，然后判断该整型数是否是对称数，12321就是对称数，123321也是对称数
def issymmetric(num):
    str_num = str(num)
    if str_num == str_num[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    while True:
        try:
            num=int(input('请输入一个整数'))
            if issymmetric(num):
                print('True')
            else:
                print('False')
            break
        except:
            print('输入必须为整数')
