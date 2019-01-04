from linkedlist import *

node1 = Node(3)
node2 = Node(4)
print(node1.data)
print(node2.data)
node1.data = 5
print (node1.data)
node1.nextNode = node2
print(node1.nextNode.data)

print("\nLL TEST\n")
myLL = LinkedList()
myLL.add2Front(4)
myLL.add2Front(3)
myLL.add2Back(6)
myLL.addinOrder(5)
print(myLL.isIn(5))
print(myLL.isIn(12))
myLL.printAll()
