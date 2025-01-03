# Author Wunchia
# 2025年01月02日00时11分28秒
# wunchia@outlook.com

import os
def use_rename():
    # os.rename('picture_copy.png','picture_done.png')
    os.remove('picture_done.png')

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


if __name__ == '__main__':
    # use_rename()
    # use_dir_func()
    # change_dir()
    scan_dir('.',0)
    # use_stat('file1')