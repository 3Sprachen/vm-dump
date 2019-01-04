from machine import *

p=Process('aProcess', 1)
p2=Process('aProcess2', 2)
p3=Process('aProcess3', 3)
p4=Process('aProcess4', 4)
print(p)
print(p2)
print(p3)
print(p4)

m=Machine('aMachine', 100)
m2=Machine('aMachine2', 200)
print(m.availableMemory())
print(m2.availableMemory())
m.addProcess(p)
m2.addProcess(p2)
print(m.availableMemory())
print(m2.availableMemory())
m.addProcess(p3)
m2.addProcess(p4)
print(m.availableMemory())
print(m2.availableMemory())
print(m)
print(m2)