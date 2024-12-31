# Author Wunchia
# 2024年12月30日10时06分08秒
# wunchia@outlook.com

#内置函数练习
class Cat():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"my name is {self.name.capitalize()}"

    def __del__(self):
        print(f'{self.name} has been deleted')

def test_cat():
    tom = Cat('tom')
    print(tom)
    del tom
    print('程序结束')

#封装练习

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
                solider.attacked(self.gun)
            else:
                print('开火失败，没子弹')

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
    # test_cat()
    solder_main()