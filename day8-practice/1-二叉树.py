# Author Wunchia
# 2025年01月02日11时32分39秒
# wunchia@outlook.com

#定义节点
class Node:
    def __init__(self, item,lchild=None, rchild=None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild

#定义二叉树
class BinaryTree:
    def __init__(self):#初始化 不包括建树
        self.root = None
        self.aid_queue=[]

    #建树 一次传入一个节点
    def level_build_tree(self,node:Node):
        if self.root is None:#根节点为空则放入根节点
            self.root = node
            self.aid_queue.append(node)#放入辅助列表 备用（左右孩子待处理）
        else:#根节点已存在
            # 利用辅助列表处理最后还有空孩子的节点
            if self.aid_queue[0].lchild is None: #左孩子空，挂在其左孩子
                self.aid_queue[0].lchild=node
            else:
                self.aid_queue[0].rchild=node #右孩子空，挂在其右孩子
                self.aid_queue.pop(0) #此时该节点已无空孩子，踢出辅助列表
            self.aid_queue.append(node) #将插入节点放入辅助列表 备用

    def pre_order(self,current_node:Node):
        if current_node:
            print(current_node.item,end=' ')
            self.pre_order(current_node.lchild)
            self.pre_order(current_node.rchild)

    def mid_order(self,current_node:Node):
        if current_node:
            self.mid_order(current_node.lchild)
            print(current_node.item,end=' ')
            self.mid_order(current_node.rchild)

    def post_order(self,current_node:Node):
        if current_node:
            self.post_order(current_node.lchild)
            self.post_order(current_node.rchild)
            print(current_node.item,end=' ')

    def level_order(self):
        help_queue=[]
        help_queue.append(self.root)
        while help_queue:
            current_node = help_queue.pop(0)
            print(current_node.item,end=' ')
            if current_node.lchild:
                help_queue.append(current_node.lchild)
            if current_node.rchild:
                help_queue.append(current_node.rchild)


if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1,11):
        new_node=Node(i)
        tree.level_build_tree(new_node)
    print('\n','*' * 3, '前序', '*' * 3)
    tree.pre_order(tree.root)
    print('\n','*' * 3, '中序', '*' * 3)
    tree.mid_order(tree.root)
    print('\n','*' * 3, '后序', '*' * 3)
    tree.post_order(tree.root)
    print('\n','*' * 3, '层序', '*' * 3)
    tree.level_order()
