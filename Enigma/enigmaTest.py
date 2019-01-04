#from enigma import Rotor
#from enigma import Enigma
#import enigma
from enigma import *
'''
r = Rotor("SHBMFWEIQRODTAVXCPYZUJKGNL")
encrypt = "Q"
print("encrypting: " + encrypt)
cipher = r.encryptLetter(encrypt)
print("encrypted: " + cipher)
print("#####################")
print("decrypting: " + cipher)
decrypted = r.decryptLetter(str(cipher))
print("decrypted: " + str(decrypted))
'''

e = Enigma("SHBMFWEIQRODTAVXCPYZUJKGNL", "GYRFNUCZLQDWMKHSJOEPBVITXA", "MSEWGQHDPRFNXATOIBUJLCZVYK")
#cipher = e.encrypt("ALOVESTRUCKROMEOSANGTHESTREETSASERENADELAYINEVERYBODYLOWWITHALOVESONGTHATHEMADE")

#e.decrypt(cipher)
e.decrypt("OQMTANMGPABQSDAKAUFXXGJBSPHBZXHLXMBNOHTNQZQGDBMIQNZJ")
#e.decrypt("OQMTANMGPABQSDAKAUFXXGJBSPHBZXHLXMBNOHTNQZQGDBMIQNZJ")
