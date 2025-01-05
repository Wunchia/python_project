# Author Wunchia
# 2025年01月03日09时45分46秒
# wunchia@outlook.com
import copy

#copy与赋值的区别
def copy_diff():
    #赋值 a和b在同一个地方 改b a也变
    a=[1,2,3]
    b=a
    b[0]=10
    print(f'a={a},地址为{id(a)}')
    print(f'b={b},地址为{id(b)}')
    #copy a和c在不同地方  改c a不变
    c=a.copy()
    c[0]=20
    print(f'a={a},地址为{id(a)}')
    print(f'c={c},地址为{id(c)}')

#如要操作自定义类型，需使用copy库
#浅copy 只拷贝了引用，没有拷贝内容
def use_copy():
    a=[1,2]
    b=[3,4]
    c=[a,b] #中间嵌套了一层c
    print(c)
    d=copy.copy(c)
    d[1]=a #d变 c不变 c和d在不同位置
    a[0]=10  #a变 d也变 c中元素和d中元素在相同位置
    print(c)
    print(d)
    print(id(c),id(d))
    d[1]=b
    print(f'a在c中：{c[0]},{id(c[0])}\n 在d中：{d[0]},{id(d[0])}')
    print(f'b在c中：{c[1]},{id(c[1])}\n 在d中：{d[1]},{id(d[1])}')

#深copy 所有层次的拷贝
def use_deepcopy():
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    print(c)
    d = copy.deepcopy(c)
    a[0]=10 #a变 d不变 c中元素和d中元素在不同位置
    print(c)
    print(d)
    print(f'a在c中：{c[0]},{id(c[0])}\n 在d中：{d[0]},{id(d[0])}')
    print(f'b在c中：{c[1]},{id(c[1])}\n 在d中：{d[1]},{id(d[1])}')

if __name__ == '__main__':
    # copy_diff()
    # use_copy()
    use_deepcopy()