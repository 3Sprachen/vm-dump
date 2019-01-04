class Node:
  def __init__(self, data):
    self.data = data
    self.nextNode = None

class LinkedList:
  def __init__(self):
      self.head = None
      self.tail = None

  pass

  def add2Front(self, data):
    if (self.head == None): #if this is the first thing in the list
        newNode = Node(data)
        self.head = newNode
        self.tail = self.head
    else:
        newNode = Node(data)
        tmp = self.head #store prior head
        self.head = newNode
        newNode.nextNode = tmp
  pass

  def printInOrder(self):
      #node = self.head
      self.__printInOrder(self.head) #(self, node)
      return
  def __printInOrder(self, node):
      if (node.nextNode == None):

          print(str(node.data))
          return
      else:
          print(str(node.data))
          nextNode = node.nextNode
          self.__printInOrder(nextNode)

  def printInReverseOrder(self):
    self.__printInReverseOrder(self.head)
    return
  def __printInReverseOrder(self, node):
      if (node.nextNode == None):
          print(str(node.data))
          return
      else:
          nextNode = node.nextNode
          self.__printInReverseOrder(nextNode)
          print(str(node.data))

  def isIn(self, element):
      node = self.head
      result = self.__isIn(element, node)
      return result

    #'''Returns True or False, saying if element appears in the list.'''
  pass

  def __isIn(self, element, node):

    if (node.data == element):
        print("True")
        return True

    if (node == self.tail):
        print("False")
        return False

    nextNode = node.nextNode
    self.__isIn(element, nextNode)

  def isInTimes(self, element):
    #Returns an integer, which is the number of times element appears in the list
    node = self.head

    numTimes = self.__isInTimes(element, node, 0)
    print("numTimes: " + str(numTimes))
    return numTimes

  def __isInTimes(self, element, node, numTimes):

    if (node.data == element):
          numTimes += 1
    if (node == self.tail):
        return numTimes
    else:
          nextNode = node.nextNode
          return self.__isInTimes(element, nextNode, numTimes)

  def get(self, i):
    #Returns the data at index i (counting from 0).  You may assume i is a
    #valid index
    node = self.head
    count = 0
    return self.__get(i, node, count)



  def __get(self, i, node, count):
      if (i > count):
          nextNode = node.nextNode
          count += 1
          self.__get(i, nextNode, count)
      else:
          dat = node.data
          print("value is: " + str(dat))
          return dat

  def addBefore(self, findElement, addElement):
    #Adds addElement to the list, so that it appears right before the first
    #appearance of findElement in the list.  If findElement is not in the list,
    #addElement should be added to the end of the list.
    self.__addBefore(findElement, addElement, self.head)
    return
  def __addBefore(self, findElement, addElement, node):

      if (addElement == self.head.data):
          add2Front(addElement)
      if (node == self.tail): #add to the end
         newNode = Node(addElement)
         self.tail.nextNode = newNode
         self.tail = newNode
         return
      if (node.nextNode.data == findElement):
          newNode = Node(addElement)
          newNode.nextNode = node.nextNode
          node.nextNode = newNode
          return
      else:
          node = node.nextNode
          self.__addBefore(findElement, addElement, node)

  def remove(self, i):
      return self.__remove(i, 0, self.head, None)
    #Alters the linked list such that the i-th element is removed.  You may assume i is a valid index.
  def __remove(self, i, count, node, prevNode):
      if (i == 0):
          self.head = node.nextNode #remove head at index 0
          return
      if (count == i):
          prevNode.nextNode = node.nextNode
          return
      else:
          count += 1
          prevNode = node
          node = node.nextNode
          self.__remove(i, count, node, prevNode)
