# Author Wunchia
# 2024年12月30日21时34分47秒
# wunchia@outlook.com

#单例模式
class MusicPlayer:
    instance=None
    def __new__(cls, *args, **kwargs):
        if cls.instance==None:
            cls.instance=super().__new__(cls) #第一次创建实例 用父类object的new创造一个instance
        return cls.instance #非第一次创建实例 复用之前的instance

    def __init__(self,name):
        self.name=name

if __name__ == '__main__':
    a=MusicPlayer('A')
    b=MusicPlayer('B')
    print(id(a),id(b))
    print(a.name,b.name)