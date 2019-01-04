#   Erich Eden
#   SY301
#   Dr. Mayberry
#   Enigma Bombe
import sys
from enigma import *
class Bombe:
	def __init__(self, message):
		#this needs to be modified to take message as an argument
		self.message = message
		sys.setrecursionlimit(52800)

	def solve(self, message, setting1, setting2, setting3):

		return self.__solve(message, setting1, setting2, setting3, 0)

	def __solve(self, message, setting1, setting2, setting3, iteration):
		e = Enigma(setting1, setting2, setting3)
		plaintext = e.decrypt(message)
		#if ("MACHINE" and "SURPRISE" in plaintext):
		if ("ONE" in plaintext): #and MINE
			print(plaintext)
			return plaintext
		else:
			iteration += 1
			setting1 = list(setting1)
			tmp = setting1[0]
			for i in range (25):
				setting1[i] = setting1[i+1]
			setting1[25] = tmp
			setting1 = ''.join(setting1)
			if (iteration + 1  % 26 == 0):
				setting2 = list(setting2)
				tmp = setting2[0]
				for i in range (25):
					setting2[i] = setting2[i+1]
				setting2[25] = tmp
				setting2 = ''.join(setting2)

			if (iteration + 1 % 676 == 0):
				setting3 = list(setting3)
				tmp = setting3[0]
				for i in range (25):
					setting3[i] = setting3[i+1]
				setting3[25] = tmp
				setting3 = ''.join(setting3)
			if (iteration == 17577):
				print("You messed up, bud.")
				return False
			self.__solve(message, setting1, setting2, setting3, iteration)

#message = sys.argv[1]
#message = "OQMTANMGPABQSDAKAUFXXGJBSPHBZXHLXMBNOHTNQZQGDBMIQNZJ"
message = "PZYGMGKHIZLLYVPMIDETWKXQCLRUNAHHCFAJSUVDZUODBTTXQDQZYMVNQXOKCNPQVLRKESAHBOEWZUKTWBQCWYEXJZTTUUHTMTERAQBDYFORQWLJCHYDRCQAZOKLBRSXHIICTUVPWAICHCSWXEDWOMPAORENVFNKDGSWXXEDSEQKTPVDHVCWHOMQPXNUBGULWWHANHETUJYITZVJYOERHVMYTRZCMALJASOGHHMGJXMWFLKFQBWPKMNOEVYWUWBVXXGHFYFRYKOQYZRGMDYUVQMLQFPFYTZWUKHAZTXYNNMEHARLWOATYKOYEJMLCOHWYPC"
b = Bombe(message)
b.solve(message, "GYRFNUCZLQDWMKHSJOEPBVITXA", "MSEWGQHDPRFNXATOIBUJLCZVYK", "SHBMFWEIQRODTAVXCPYZUJKGNL")
#b.solve(message, "SHBMFWEIQRODTAVXCPYZUJKGNL", "GYRFNUCZLQDWMKHSJOEPBVITXA", "MSEWGQHDPRFNXATOIBUJLCZVYK") #B
