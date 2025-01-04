# Author Wunchia
# 2024年12月30日21时34分37秒
# wunchia@outlook.com

#多态练习

class Dog:
    def __init__(self, name):
        self.name = name
    def game(self):
        print('happy game')

class Xtq(Dog):
    def game(self):
        print('game in sky')

class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self,dog):
        print(f'{self.name} game with {dog.name}')
        dog.game()

if __name__ == '__main__':
    wangchai=Dog('wangchai')
    xtq=Xtq('xtq')
    a=Person('a')
    a.game_with_dog(xtq)
    a.game_with_dog(wangchai)