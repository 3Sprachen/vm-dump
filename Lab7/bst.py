#   Erich Eden
#   SY301
#   Dr. Mayberry
#   bst.py

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None

    def insert(self, phrase):
        newNode = Node(phrase)

        if (self.root != None):
            self.__insert(newNode, self.root)
        else:
            self.root = newNode

    def __insert(self, newNode, currentNode):

        if (newNode.data < currentNode.data):
            if (currentNode.left == None):
                currentNode.left = newNode
                return
            else:
                self.__insert(newNode, currentNode.left)
        else:
            if (currentNode.right == None):
                currentNode.right = newNode
                return
            else:
                self.__insert(newNode, currentNode.right)


    def __contains__(self, phrase):
        if (self.__check(phrase, self.root) == True):
            return True
        else:
            return False


    def __check(self, phrase, currentNode):
        if (currentNode == None):
            return False
        if (currentNode.data == phrase):
            return True
        if (phrase > currentNode.data):
            return self.__check(phrase, currentNode.right)
        else:
            return self.__check(phrase, currentNode.left)

###############################################################################
#test code
'''
testTree = TreeSet()
testTree.insert("eat")
testTree.insert("my")
testTree.insert("shorts")
testTree.insert("five")
testTree.insert("ten")
testTree.insert("fifteen")
testTree.insert("sell")
testTree.insert("apple")

if ("eat" in testTree):
    print ("mission success")
else:
    print("back to the drawing board")
if ("my" in testTree):
    print ("mission success")
else:
    print("back to the drawing board")
if ("ten" in testTree):
    print ("mission success")
else:
    print("back to the drawing board")
if ("apple" in testTree):
    print ("mission success")
else:
    print("back to the drawing board")
if ("fifteen" in testTree):
    print ("mission success")
else:
    print("back to the drawing board")
'''
