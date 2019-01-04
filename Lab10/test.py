#graphTest
from graph import *
g = Graph('sampleDot.dot')
print(g.isAdjacent("A", "B"))
print(g.isAdjacent("B", "A"))
print(g.isAdjacent("H", "A"))
print(g.isAdjacent("Z", "B"))
print(g.returnAdjacent("A"))
print(g.__str__())
