# Author Wunchia
# 2025年01月03日10时56分24秒
# wunchia@outlook.com
import re

#正则表达式
def easy_case():
    result=re.match("test","test.com")
    if result:
        print(result.group())

def single():
    """
    匹配单个字符
    :return:
    """

def multi():
    """
    匹配多个字符
    :return:
    """

def match_mail():
    email_list=['123456@163.comcc','12345@gmail.com','xiaoming@163acom','happyhappyhappy@163.com']
    for email in email_list:
        ret=re.match('\w{4,20}@163\.com$',email) #.需要转义 匹配的字符串中出现了正则的符号均需要转义
        if ret:
            print(f'{email}是正确email地址')
        else:
            print(f'email地址不正确')

#匹配分组
def split_group():
    pass

#re模块的高级用法
def advanced_func():
    pass

if __name__ == '__main__':
    # easy_case()
    match_mail()