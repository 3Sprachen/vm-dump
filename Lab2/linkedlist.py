#   Erich Eden
#   SY301
#   Dr. Mayberry
#   Lab 2


class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printAll(self):
        print ("list contains: \n")
        current = self.head
        if (current == None): #list is empty. Checked this bc otherwise my print tail would crash on an empty list
            print("   ")
        while (current.nextNode != None):
            print (current.data)
            current = current.nextNode
        print(current.data) #while loop exited before printing tail

    def add2Front(self, data):
        if (self.head == None): #if this is the first thing in the list
            newNode = Node(data)
            self.head = newNode
            self.tail = self.head
        else:
            newNode = Node(data)
            tmp = self.head #store prior head
            self.head = newNode
            newNode.nextNode = tmp #what was the head is now the next node for the new head

    def add2Back(self, data):
        if (self.tail == None): #list is empty
            newNode = Node(data)
            self.tail = newNode
            self.head = self.tail
        else:
            newNode = Node(data)
            self.tail.nextNode = newNode
            self.tail = newNode

    def isIn(self, data):
        current = self.head
        test = Node(data)

        while (current.nextNode != None):
            if (current.data == test.data):
                return True
            current = current.nextNode
        return False
    def addinOrder(self, data):

        current = self.head
        previous = self.head
        newNode = Node(data)
        if (newNode.data < current.data): #if new node should be first in LinkedList
            add2front(data)
            return
        if (newNode.data > self.tail.data):
            add2back(data)
            return
        while (current.data < newNode.data):
            previous = current
            current = current.nextNode
        newNode.nextNode = current
        previous.nextNode = newNode

        return
