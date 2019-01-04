#   Erich Eden
#   SY301
#   Dr. Mayberry
#   bloomFilter.py

import hashlib

class BloomFilter:
    def __init__(self, size):

        self.arr = [False] * size

    def add(self, k):
        for i in range(1,3):
            index = self.hashMagic(k, i)
            self.arr[index] = True

    def hashMagic(self, k, hashmode):
        if hashmode == 1:
            hashObject = hashlib.md5()
        if hashmode == 2:
            hashObject = hashlib.sha256()
        if hashmode == 3:
            hashObject = hashlib.sha512()
        byteString = k.encode()
        hashObject.update(byteString)
        hexOut = hashObject.hexdigest()
        number = int(hexOut, 16)
        index = number % len(self.arr)
        return index

    def __contains__(self, k):
        for i in range(1,3):
            index = self.hashMagic(k, i)
            if (self.arr[index] == False):
                return False
        return True

BF = BloomFilter(1234567)
BF.add("Rock")
BF.add("Your")
BF.add("Socks")
BF.add("Off")

if "Rock" in BF:
    print("True")
else:
    print("False")
if "Your" in BF:
    print("True")
else:
    print("False")
if "Off" in BF:
    print("True")
else:
    print("False")
if "Doors" in BF:
    print("True")
else:
    print("False")
