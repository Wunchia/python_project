# Author Wunchia
# 2025年01月01日10时38分02秒
# wunchia@outlook.com

import os  #使用 seek 需要

def open_r():
    file=open('file1',mode='r',encoding='utf-8')
    text=file.read()
    print(text)
    #file.write('world') #报错 以只读方式打开 不可写
    file.close()

def open_rw():
    file=open('file2.txt',mode='r+',encoding='utf-8')
    file.write('world')
    text = file.read()
    print(text)
    file.close()

def open_w():
    file=open('file3',mode='w',encoding='utf-8')
    file.write('hello world')
    file.close()

def open_a(): #每次写的时候追加到文件末尾
    file=open('file3',mode='a',encoding='utf-8')
    file.write('Yes')
    file.close()

def use_readline():
    file=open('file1',mode='r',encoding='utf-8')
    while True:
        text=file.readline()
        if not text:
            break
        print(text,end=" ")
    file.close()

def use_seek():
    """
    移动光标 操作对象为汉字时需要为3的倍数 因为utf-8一个汉字占三字节，seek不能将其切开
    :return:
    """
    file=open('file3',mode='r+',encoding='utf-8')
    file.seek(3,os.SEEK_SET) #SEEK_SET 相对开始位置偏移3
    file.seek(0,os.SEEK_CUR) #SEEK_CUR 当前位置 只能填0 否则报错 鸡肋
    file.seek(0,os.SEEK_END) #SEEK_END 结束位置 只能填0 否则报错 鸡肋
    text = file.read(2)
    print(text)
    file.close()

def binary_seek():
    """
    操作二进制文件时 cur和 end 可不为0
    :return:
    """
    file=open('file3',mode='rb+')
    file.seek(5,os.SEEK_CUR)
    file.seek(-2,os.SEEK_CUR)
    b=file.read()
    print(b)
    file.close()

def copy():
    file01=open('picture_test.png',mode='rb+')
    file02=open('picture_copy.png',mode='wb+')
    file02.write(file01.read())
    file01.close()
    file02.close()

if __name__ == '__main__':
    open_r()
    open_rw()
    open_w()
    open_a()
    use_readline()
    use_seek()
    binary_seek()
    copy()