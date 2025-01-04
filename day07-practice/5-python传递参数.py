# Author Wunchia
# 2025年01月02日01时45分44秒
# wunchia@outlook.com

import sys
def write_hello(file_path):
    file = open(file_path, 'w+', encoding='utf-8')
    file.write('Hello World')
    file.close()

if __name__ == '__main__':
    write_hello(sys.argv[1])