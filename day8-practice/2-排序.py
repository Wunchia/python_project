# Author Wunchia
# 2025年01月02日14时16分38秒
# wunchia@outlook.com

import random
import time
import sys
class Sort:
    def __init__(self,n):
        self.len=n
        self.arr=[0]*n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i]=random.randint(0,99)
        print(self.arr)


if __name__ == '__main__':
