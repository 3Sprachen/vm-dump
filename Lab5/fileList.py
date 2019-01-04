#   Erich Eden
#   SY301
#   Dr. Mayberry
#   Lab 5

import sys

class Node:
  def __init__(self, data):
    self.data = data
    self.nextNode = None

class Stack:
  def __init__(self):
      self.head = None
      self.tail = None

  def push(self, data):
      if (self.tail == None): #list is empty
          newNode = Node(data)
          self.tail = newNode
          self.head = self.tail
      else:
          newNode = Node(data)
          #self.tail.nextNode = newNode
          #self.tail = newNode
          newNode.nextNode = self.head
          self.head = newNode
  def pop(self):
      #return the most recent item and then remove it
      data = self.head.data
      self.head = self.head.nextNode
      return data
  def peek(self):
      if (self.head == None):
          return None
      else:
          return self.head.data

  def printInReverseOrder(self): #straight from lab4
    self.__printInReverseOrder(self.head)
    return
  def __printInReverseOrder(self, node):
      if (node == None):
          return
      else:
          nextNode = node.nextNode
          self.__printInReverseOrder(nextNode)
          print(str(node.data), end = '')
          print("->", end = '')

myStack = Stack()

with open(sys.argv[1]) as log:
    for line in log:
        line = line.split()

        #there are 2 parts to the line: command and then some file / computer / something
        command = line[0]
        if (command != "exit"):
            arg = line[1]

        if (command == "ssh"):
            myStack.push(arg) #myStack is tracking what machine I'm in / how i got there

        if (command == "less"):
            myStack.printInReverseOrder()
            print(arg)
        if (command == "exit"):
            myStack.pop()
