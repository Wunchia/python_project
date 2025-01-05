# Author Wunchia
# 2025年01月03日10时56分24秒
# wunchia@outlook.com
import re

#正则表达式
def easy_case():
    # result = re.match ( 正则表达式 ，要匹配的字符串 ）
    result=re.match("test","test.com")
    if result:
        print(result.group())

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

def sta_end():
    """
    匹配开头结尾
    ^ 匹配字符串开头
    $ 匹配字符串结尾
    :return:
    """
    email_list=['123456@163.comcc','12345@gmail.com','xiaoming@163acom','happyhappyhappy@163.com']
    for email in email_list:
        ret=re.match(r'\w{4,20}@163\.com$',email) #.需要转义 匹配的字符串中出现了正则的符号均需要转义
        if ret:
            print(f'{email}是正确email地址')
        else:
            print(f'{email}地址不正确')
    print('-' * 50)
    ret = re.match(r"[1-9]?\d$", '09')
    if ret:
        print(ret.group())
    else:
        print('不是0-99')

def split_group():
    """
    | 匹配左右任意一个表达式
    (ab)将括号中字符作为一个分组
    \num 引用分组num匹配到的字符串
    (?P<name>) 分组起别名
    (?P=name) 引用别名为name分组匹配到的字符串
    :return:
    """
    ret=re.match(r"[1-9]?[0-9]|100",'9')
    print(ret.group())
    print('-' * 50)
    ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@qq.com")
    print(ret.group())
    ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@126.com")
    print(ret.group())
    print('-' * 50)
    ret = re.match(r"([^-]+)-(\d+)", "010-12345678")# 代表没有遇到小横杠 - 就一直进行匹配，一直匹配下去
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))
    print('-'*50)
    labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com</h2></html>"]
    for label in labels:
        ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", label)
        if ret:
            print("%s 是符合要求的标签" % ret.group())
        else:
            print("%s 不符合要求" % label)


#re模块的高级用法
def add(x):
    result = x.group()
    return str(int(result) + 100)

def advanced_func():
    ret = re.search(r"\d+", "阅读次数为 9999,点赞888")
    print(ret.group())
    print('-' * 50)
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
    print(ret)
    print('-' * 50)
    ret = re.sub(r"\d+", '998', "python = 997")
    print(ret)
    ret = re.sub(r"\d+", lambda x: str(int(x.group()) + 100), "python = 997")
    print(ret)
    ret = re.sub(r"\d+", add, "python = 997")
    print(ret)
    print('-' * 50)
    # sub只替换前两个
    text = "apple apple apple apple"
    pattern = r"apple"
    replacement = "orange"

    new_text = re.sub(pattern, replacement, text, count=3)
    print(new_text)

if __name__ == '__main__':
    # easy_case()
    # single()
    # multi()
    # sta_end()
    # split_group()
    advanced_func()