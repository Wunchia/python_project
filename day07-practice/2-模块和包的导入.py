# Author Wunchia
# 2024年12月31日21时25分22秒
# wunchia@outlook.com

#模块导入
from module1 import test as test1
from module2 import test as test2

test1()
test2()

#包导入
import wd_message #需要在__init__中设置权限

wd_message.send.send()
wd_message.receive.receive()