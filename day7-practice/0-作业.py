# Author Wunchia
# 2024年12月31日21时10分45秒
# wunchia@outlook.com

# 1.完成包的使用（与上课一致）
#模块导入
from module1 import test as test1
from module2 import test as test2

test1()
test2()

#包导入
import wd_message #需要在__init__中设置权限

wd_message.send.send()
wd_message.receive.receive()

# 2.完成文件的文本模式的读，写（与上课一致）
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

if __name__ == '__main__':
    open_r()
    open_rw()
    open_w()
    open_a()
    use_readline()

# 3.完成目录的listdir，getcwd,chdir的使用（与上课一致）
import os

def use_dir_func():
    file_list=os.listdir('.')
    print(file_list)
    os.mkdir('dir2')
    os.rmdir('dir1')
    print(os.getcwd())
    os.chdir('dir2')
    file=open('file_indir2','w',encoding='utf-8')
    file.close()

def change_dir():
    print(os.getcwd())
    os.chdir('dir2')
    print(os.getcwd())

if __name__ == '__main__':
    use_dir_func()
    change_dir()

# 4.完成python的传参练习（与上课一致）
import sys
def write_hello(file_path):
    file = open(file_path, 'w+', encoding='utf-8')
    file.write('Hello')
    file.close()

if __name__ == '__main__':
    write_hello(sys.argv[1])

# ********
# 5、完成普通文件文件的seek，二进制文件的seek（代码编写与上课一致即可）
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

if __name__ == '__main__':
    use_seek()
    binary_seek()

# 6、完成目录深度优先遍历（代码编写与上课一致即可
def scan_dir(file,depth):
    file_list=os.listdir(file)
    for file in file_list:
        print(f"{'  '*depth}{file}")
        if os.path.isdir(file): #如果是 dir 则递归遍历，不是 dir 则可以返回
            scan_dir((file),depth+1)

if __name__ == '__main__':
    scan_dir('.',0)