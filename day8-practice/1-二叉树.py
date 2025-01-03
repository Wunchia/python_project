# Author Wunchia
# 2025年01月02日11时32分39秒
# wunchia@outlook.com

class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root
