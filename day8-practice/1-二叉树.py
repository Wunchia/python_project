# Author Wunchia
# 2025年01月02日11时32分39秒
# wunchia@outlook.com

class Node:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.aid_queue=[]

    def level_build_tree(self,node:Node):
        if self.root is None:
            self.root = node
            self.aid_queue.append(node)
        else:
            self.aid_queue.append(node)

