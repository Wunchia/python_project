# Author Wunchia
# 2024年12月30日13时06分57秒
# wunchia@outlook.com


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