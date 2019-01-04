from linkedlist import *



print("\nLL TEST should read 2 2 4 7 8 9 13 (then bw) False True numTimes: 2\n")
myLL = LinkedList()

myLL.add2Front(9)
myLL.add2Front(7)
myLL.add2Front(4)
myLL.add2Front(3)
myLL.add2Front(2)
myLL.add2Front(2)
myLL.addBefore(9, 8)
myLL.addBefore(12, 13)
myLL.remove(2)
myLL.printInOrder()
myLL.printInReverseOrder()
myLL.isIn(5)
myLL.isIn(7)
myLL.isInTimes(2)
myLL.get(4)
