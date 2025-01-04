# Author Wunchia
# 2025年01月02日00时11分28秒
# wunchia@outlook.com

import os
def use_rename():
    # os.rename('picture_copy.png','picture_done.png')
    os.remove('picture_done.png')

def use_dir_func():
    file_list=os.listdir('.') #获取当前目录下的文件列表
    print(file_list)
    os.mkdir('dir2') #创建目录
    os.rmdir('dir1') #删除空目录 目录非空会报错
    print(os.getcwd()) #打印当前工作目录的路径
    os.chdir('dir2') #切换工作目录
    file=open('file_indir2','w',encoding='utf-8')
    file.close()

def change_dir():
    print(os.getcwd())
    os.chdir('dir2')
    print(os.getcwd())

def scan_dir(cur_path,depth):
    file_list=os.listdir(cur_path)
    for file in file_list:
        print(f"{'  '*depth*4}{file}")
        new_path=cur_path+'/'+file
        if os.path.isdir(new_path): #如果是 dir 则递归遍历，不是 dir 则可以返回
            scan_dir(new_path,depth+1)

def use_stat(file_path):
    file_info=os.stat(file_path)
    print('size {}\nuid {}\nmode {:x}\nmtime {}'.format(file_info.st_size,file_info.st_uid,file_info.st_mode,file_info.st_mtime))

    # os.stat()函数返回一个os.stat_result对象
    # 这个对象包含了文件的各种属性。可以通过访问这个对象的属性来获取具体的信息。
    #
    # 常用属性
    # st_mode: 文件的权限模式。
    # st_size: 文件的大小（字节）。
    # st_atime: 文件最后一次被访问的时间。
    # st_mtime: 文件最后一次被修改的时间。
    # st_ctime: 文件的元数据（如权限、所有者等）最后一次被修改的时间。

if __name__ == '__main__':
    # use_rename()
    # use_dir_func()
    # change_dir()
    scan_dir('.',0)
    # use_stat('file1')