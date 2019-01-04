#test for maps.py
from maps import *
pair1 = KVPair(160000, 'Aardvark, Aaron')
pair2 = KVPair(169998, 'Zebra, Zeke')
print(pair1<pair2) #True
print(pair2<pair1) #False
print(pair1==pair2) #False

arrMap=SortedArrayMap()
arrMap[160000] = 'Aardvark, Andrew'
arrMap[201644] = 'Eden, Erich'
arrMap[123456] = 'mom, ur'
arrMap[654321] = 'sorry, im'

#for i in arrMap:
#    print(str(arrMap[i].key) + ", " + str(arrMap[i].value) )

print(arrMap[160000]) #Aardvark, Andrew
print(arrMap[123456]) #mom, ur
print(160000 in arrMap) #True
print(169998 in arrMap) #False
print(123456 in arrMap) #True
