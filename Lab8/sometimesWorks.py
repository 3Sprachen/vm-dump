#   Erich Eden
#   SY301
#   Dr. Mayberry
#   treap.py
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.priority = random.random()

class TreapSet:
    def __init__(self):
        self.root = None
        self.length = 0
    def add(self, k):
        node = Node(k)
        if (self.root == None):
            self.root = node
            self.length = 1
            return
        else:
            self.__insert(node, self.root) #put it in the tree like normal
            self.check(node) #find out if a given node should be rotated
            self.length += 1

    def check(self, node):
        while (node.priority > node.parent.priority): #should continue swapping up if need be
            #some rotation magic
            if not node.parent:
                break
            self.rotate(node)


    def __insert(self, node, currentNode):
        if (node.data < currentNode.data):
            if (currentNode.left == None):
                currentNode.left = node
                node.parent = currentNode
                return
            else:
                self.__insert(node, currentNode.left)
        else:
            if (currentNode.right == None):
                currentNode.right = node
                node.parent = currentNode
                return
            else:
                self.__insert(node, currentNode.right)

    def rotate(self, node):
        parent = node.parent
        if parent == None: #node is now the root
            return
        else:
            if parent.parent:
                grandparent = parent.parent
            else:
                grandparent = None

        if (node.data < parent.data): #node is to the left of parent

            parent.right = None
            parent.left = node.left
            node.right = parent
            if grandparent:
                grandparent.left = node
                node.parent = grandparent


            self.check(node)


        else: #node is to the right of parent
            parent.left = None
            parent.right = node.right #likely None, but could be another branch
            node.left = parent
            if grandparent:
                grandparent.right = node
                node.parent = grandparent
            self.check(node)

            #parent.right = node.left

    def __contains__(self, k):
        if (self.__check(k, self.root) == True):
            return True
        else:
            return False


    def __check(self, k, currentNode):
        if (currentNode == None):
            return False
        if (currentNode.data == k):
            return True
        if (k > currentNode.data):
            return self.__check(k, currentNode.right)
        else:
            return self.__check(k, currentNode.left)

    def __len__(self):
        return self.length

    def height(self):
        return self.__height(self.root)
    def __height(self, node):
        if not node:
            return 0
        #we know we are done with a given chain when left and right are both none
        if (node.left == None and node.right == None):
            return 1
        if (node.left == None):
            rHeight = self.__height(node.right)+1
        if (node.right == None):
            lHeight = self.__height(node.left)+1
        if (lHeight > rHeight):
            return lHeight + 1
        else:
            return rHeight + 1
