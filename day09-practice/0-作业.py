# Author Wunchia
# 2025年01月04日16时11分29秒
# wunchia@outlook.com

# 1、练习深copy与浅copy

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

# 2、练习上课匹配单个字符，多个字符，匹配分组的正则表达式案例

import re

#正则表达式
def single():
    r"""
    匹配单个字符
    . 任意字符（除了\n）   []匹配[]中列举的字符
    \d 匹配数字  \D 匹配非数字
    \s 匹配空格  \S 匹配非空格
    \w 匹配单词字符 即 a-z、A-Z、0-9、_、汉字
    \W 匹配非单词字符
    :return:
    """
    ret=re.match("t.o","too")
    print(ret.group())
    ret=re.match("t.o","two")
    print(ret.group())
    ret=re.match('[0-35-68-9]','1234567890')
    if ret:
        print(ret.group())
    ret=re.match(r'土星\d号','土星5号')
    print(ret.group())


def multi():
    """
    匹配多个字符
    * 可有可无  + 一次或无限次
    ？ 一次或0次
    {m}出现m次  {m,n}出现从m到n次
    :return:
    """
    ret=re.match("[A-Z][a-z]+",'Aabcdefghijkl')
    print(ret.group())
    print('-'*50)
    names=['name1','_name','2name','__name__']
    for name in names:
        ret=re.match(r"[a-zA-Z_]\w*",name)
        if ret:
            print(ret.group())
        else:
            print(f'{name} is wrong format')
    print('-' * 50)
    ret=re.match(r"[1-9]?[0-9]",'7')
    print(ret.group())
    ret = re.match(r"[1-9]?\d", '33')
    print(ret.group())
    ret = re.match(r"[1-9]?\d", '09')
    print(ret.group())
    ret=re.match(r"[1-9]{5,7}", '999873*4582425')
    print(ret.group())


# 3、练习上课的search，findall,sub等案例

