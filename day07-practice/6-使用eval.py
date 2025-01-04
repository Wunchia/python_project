# Author Wunchia
# 2025年01月02日01时57分46秒
# wunchia@outlook.com
"""
eval 处理配置文件
"""
def read_conf():
    file=open('file4','r+',encoding='utf-8')
    text_info=file.read()
    print(text_info)
    my_dict=eval(text_info)
    print(type(my_dict))
    print(my_dict)
    file.close()

if __name__ == '__main__':
    read_conf()