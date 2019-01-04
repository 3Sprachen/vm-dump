#   Erich Eden
#   SY301
#   Dr. Mayberry
#   maps.py

import bisect

class KVPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    ####overload the operators####
    def __lt__(self, other):
        if self.key < other.key:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.key > other.key:
            return True
        else:
            return False
    def __le__(self, other):
        if self.key <= other.key:
            return True
        else:
            return False
    def __ge__(self, other):
        if self.key >= other.key:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.key == other.key:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.key != other.key:
            return True
        else:
            return False



class SortedArrayMap:
    def __init__(self):
        self.aMap = []

    def __setitem__(self, key, value):
        #create a kv pair and insert it into the map. aMap[k]=v
        kvpair = KVPair(key, value)
        bisect.insort_right(self.aMap, kvpair)

    def __getitem__(self, key):
        #return the value associated with a key. v=aMap[k]
        return self.search(self.aMap, 0, len(self.aMap), key)
        
    def __contains__(self, key):
        if (self.search(self.aMap, 0, len(self.aMap), key)):
            return True
        else:
            return False

    def search(self, array, low, high, key):
        if (low > high):
            return None
        mid = (low+high)//2
        if (array[mid].key == key):
            return array[mid].value
        if (array[mid].key > key):
            return self.search(array, 0, (mid - 1), key)
        return self.search(array, mid+1, high, key)
