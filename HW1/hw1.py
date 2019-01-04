#   Erich Eden
#   SY301
#   Dr. Mayberry
#   HW1: hw1.py


def sortFunc():
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    c = int(input("Enter third integer: "))

    numList = [a, b, c]

    while numList[0] > numList[1]:
        tmp = numList[0]
        numList[0] = numList[1]
        numList[1] = tmp
    while numList[0] > numList[2]:
        tmp = numList[0]
        numList[0] = numList[2]
        numList[2] = tmp
    while numList[1] > numList[2]:
        tmp = numList[1]
        numList[1] = numList[2]
        numList[2] = tmp

    return numList;
def everyOther(itemList):
    x = 0
    y = 0
    newList = []
    while x < len(itemList):
        if x % 2 == 0:
            newList.append(itemList[x])
            y += 1

        x += 1
    
    return newList;

#########Test bits
#sortFunc()

#letterList = ['a', 'b', 'c', 'd', 'e']
#everyOther(letterList)
