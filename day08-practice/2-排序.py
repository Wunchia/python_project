# Author Wunchia
# 2025年01月02日14时16分38秒
# wunchia@outlook.com

import random
import time
import sys

sys.setrecursionlimit(100000) #增加递归深度

class Sort:
    #产生一个随机列表
    def __init__(self,n):
       self.arr=[0]*n #留意python数组初始化方法
       self.len=n
       self.random_data() #在init中调用后面定义的函数
    def random_data(self):
       """
       随机数组 random.randint(0,99)左闭右闭
       :return:
       """
       for i in range(self.len):
           self.arr[i]=random.randint(0,99)

    #快速排序

    #交换法
    def partition01(self,left,right):
        arr=self.arr
        i=k=left
        #通过随机选取枢轴 避免陷入最坏时间复杂度
        random_pos=random.randint(left,right)
        arr[right],arr[random_pos]=arr[random_pos],arr[right]
        # i不断后移 k只有接到一个小于枢轴的元素后才向后走 因此k会停在枢轴位置
        for i in range(left,right):
            if arr[i]<arr[right]: #i所指元素小于枢轴时
                arr[i],arr[k]=arr[k],arr[i] #i所指换到前面k的位置
                k+=1 #k后移
        arr[k],arr[right]=arr[right],arr[k]
        return k

    def quick_sort01(self,left,right):
        if left < right:
            pivot=self.partition01(left,right)
            self.quick_sort01(left,pivot-1)
            self.quick_sort01(pivot+1,right)

    #挖坑法
    def partition02(self,low,high):
        pivot=self.arr[low]
        while low<high:
            while low<high and self.arr[high]>=pivot:
                high-=1
            self.arr[low]=self.arr[high]
            while low<high and self.arr[low]<=pivot:
                low+=1
            self.arr[high]=self.arr[low]
        self.arr[low]=pivot
        return low

    def quick_sort02(self,low,high):
        if low<high:
            pivotpos=self.partition02(low,high)
            self.quick_sort02(low,pivotpos-1)
            self.quick_sort02(pivotpos+1,high)

    #堆排序

    #调整大根堆
    def adjust_max_heap(self,pos,arr_len):
        """
        把子树调整为大根堆 从子树的根开始向下处理
        :param pos: 被调整的元素的位置
        :param arr_len: 当前列表总长度
        :return:
        """
        arr=self.arr
        dad=pos
        while 2*dad+1 < arr_len:
            son = 2 * dad + 1
            if son+1<arr_len and arr[son]<arr[son+1]:
                son+=1
            if arr[son] > arr[dad]:
                arr[dad],arr[son]=arr[son],arr[dad]
                dad=son
            else:
                break

    def heap_sort(self):
        #建大根堆
        for parent in range(self.len//2-1,-1,-1): #从后向前（从下向上）处理
            self.adjust_max_heap(parent, self.len)
        #交换堆顶元素和末尾元素
        arr = self.arr
        arr[0],arr[self.len-1]=arr[self.len-1],arr[0]
        # 此时及之后只有以堆顶元素为根的子树不满足大根堆
        for cur_len in range(self.len-1,1,-1): #每轮处理后 待处理的长度-1
            self.adjust_max_heap(0,cur_len)
            arr[0], arr[cur_len - 1] = arr[cur_len - 1], arr[0]

    #用小根堆排降序
    def adjust_min_heap(self,pos,arr_len):
        arr=self.arr
        dad=pos
        son = 2 * dad + 1
        while son < arr_len:
            if son+1 < arr_len and arr[son]>arr[son+1]:
                son+=1
            if arr[son] < arr[dad]:
                arr[dad],arr[son]=arr[son],arr[dad]
                dad=son
                son = 2 * dad + 1
            else:
                break

    def reverse_heapsort(self):
        arr=self.arr
        for parent in range(self.len//2-1,-1,-1):
            self.adjust_min_heap(parent,self.len)
        arr[0], arr[self.len-1] = arr[self.len-1], arr[0]
        for cur_len in range(self.len-1,1,-1):
            self.adjust_min_heap(0,cur_len)
            arr[0], arr[cur_len - 1] = arr[cur_len - 1], arr[0]

    #计算耗时
    def count_time(self,sort_func,*args,**kwargs):
        start_time=time.time()
        sort_func(*args,**kwargs)
        end_time=time.time()
        return end_time-start_time

if __name__ == '__main__':
    count=100000
    my_sort=Sort(count)
    # print(my_sort.arr)
    # my_sort.quick_sort01(0,my_sort.len-1)
    # my_sort.quick_sort02(0,my_sort.len-1)
    # my_sort.heap_sort()
    # my_sort.reverse_heapsort()
    # print(my_sort.arr)
    print(f'快速排序-交换法 用时：{my_sort.count_time(my_sort.partition01,0,my_sort.len-1)}')
    print(f'快速排序-挖坑法 用时：{my_sort.count_time(my_sort.partition02, 0, my_sort.len-1)}')
    print(f'堆排序-升序 用时：{my_sort.count_time(my_sort.heap_sort)}')
    print(f'堆排序-降序 用时：{my_sort.count_time(my_sort.reverse_heapsort)}')
