#   Erich Eden
#   SY301
#   Dr. Mayberry
#   sorter.py

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


print numList[0], numList[1], numList[2]
