# Author Wunchia
# 2024年12月30日21时34分23秒
# wunchia@outlook.com

#private
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