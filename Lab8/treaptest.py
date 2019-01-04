from treap import *

myTreap = TreapSet()

myTreap.add(4)
myTreap.add(5)
myTreap.add(8)
myTreap.add(6)
myTreap.add(4)
myTreap.add(7)
print(4 in myTreap) #True
print(12 in myTreap) #False
print(6 in myTreap) #True
print(7 in myTreap) #True
print(len(myTreap)) #6
print(myTreap.height()) #who knows
