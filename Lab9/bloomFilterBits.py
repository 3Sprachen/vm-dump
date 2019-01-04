#   Erich Eden
#   SY301
#   Dr. Mayberry
#   bloomFilterBits.py



import hashlib

class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.integer = 0

    def add(self, k):
        for i in range(1,3):
            index = self.hashMagic(k, i)
            thirdBit = 1 << index
            self.integer = self.integer | thirdBit

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
        index = number % self.size
        return index

    def __contains__(self, k):
        for i in range(1,3):
            index = self.hashMagic(k, i)
            thirdBit = 1 << index
            if not (self.integer & thirdBit):
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
