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
        while (node.parent and (node.priority > node.parent.priority)): #should continue swapping up if need be
            #some rotation magic
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

        if node.parent == None: #node is now the root
            return

        #2 rotation methods depending on if the node is left or right
        #if (node.data < parent.data): #node is to the left of parent
        if (node == node.parent.left): #node is to the left of parent

            grandparent = node.parent.parent #it's okaty if this is None
            node.parent.left = node.right
            node.right = node.parent
            node.parent = grandparent
            if grandparent:
                if (grandparent.data < node.data):
                    grandparent.right = node
                else:
                    grandparent.left = node



        else: #node is to the right of parent
            grandparent = node.parent.parent #it's okaty if this is None
            node.parent.right = node.left
            node.left = node.parent
            node.parent = grandparent
            if grandparent:
                if (grandparent.data < node.data):
                    grandparent.right = node
                else:
                    grandparent.left = node


        self.check(node)



    def __contains__(self, k):
        if (self.__isin(k, self.root) == True):
            return True
        else:
            return False


    def __isin(self, k, currentNode):
        if (currentNode == None): #reached the end of a branch, end of search
            return False
        if (currentNode.data == k):
            return True
        if (k > currentNode.data):
            return self.__isin(k, currentNode.right)
        else:
            return self.__isin(k, currentNode.left)

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
            return self.__height(node.right)+1
        if (node.right == None):
            return self.__height(node.left)+1
        else:
            return max(self.__height(node.left), self.__height(node.right)) + 1
