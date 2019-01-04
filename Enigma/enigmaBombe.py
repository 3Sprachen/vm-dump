#   Erich Eden
#   SY301
#   Dr. Mayberry
#   Enigma Bombe
#
#	This bomb can be used to break a message encrypted by my enigma.py project.
#	It assumes knowledge of the rotors used (though not their order or setting relative to each other) and some words the message should contain.


import sys
from enigma import *
class Bombe:
	def __init__(self, message):
		#this needs to be modified to take message as an argument
		self.message = message #sys.argv[1]
		self.setting1 = "GYRFNUCZLQDWMKHSJOEPBVITXA"
		self.setting2 = "MSEWGQHDPRFNXATOIBUJLCZVYK"
		self.setting3 = "SHBMFWEIQRODTAVXCPYZUJKGNL"
		self.configuration = 1
		self.iteration = 0

	def attempt(self):
		e = Enigma(self.setting1, self.setting2, self.setting3)
		plaintext = e.decrypt(self.message)
		return plaintext

	def rotorSwap(self):
		#the letters ABC were aids to figure out what needed swapping from one config to the next

		#ABC when configuration = 1

		#ACB
		if (self.configuration == 1): #change to configuration 2
			tmp = self.setting2
			self.setting2 = self.setting3
			self.setting3 = tmp
		#BCA
		if (self.configuration == 2):#change to configuration 3
			tmp = self.setting1
			self.setting1 = self.setting3
			self.setting3 = tmp
		#BAC
		if (self.configuration == 3): #change to configuration 4
			tmp = self.setting2
			self.setting2 = self.setting3
			self.setting3 = tmp
		#CAB
		if (self.configuration == 4): #change to configuration 5
			tmp = self.setting1
			self.setting1 = self.setting3
			self.setting3 = tmp
		#CBA
		if (self.configuration == 5): #change to configuration 6
			tmp = self.setting2
			self.setting2 = self.setting3
			self.setting3 = tmp

	def rotorShift(self):
		#one rotor goes all the way through while the other two are held constant. Then the next rotor changes by one spot and the process repeats
		self.setting1 = list(self.setting1) #rotor three rotates by one position every time
		tmp = self.setting1[0]
		for i in range (25):
			self.setting1[i] = self.setting1[i+1]
		self.setting1[25] = tmp
		self.setting1 = ''.join(self.setting1)
		if ((self.iteration + 1)  % 26 == 0): #rotor three is all the way around so rotor 2 should rotate by one.
			self.setting2 = list(self.setting2)
			tmp = self.setting2[0]
			for i in range (25):
				self.setting2[i] = self.setting2[i+1]
			self.setting2[25] = tmp
			self.setting2 = ''.join(self.setting2)

		if ((self.iteration + 1) % 676 == 0): #rotor two is all the way around so rotor three should rotate
			self.setting3 = list(self.setting3)
			tmp = self.setting3[0]
			for i in range (25):
				self.setting3[i] = self.setting3[i+1]
			self.setting3[25] = tmp
			self.setting3 = ''.join(self.setting3)

		if ((self.iteration) % 17576 == 0): #26^3 means every rotation combo has been tried so we should swap rotor order
			self.rotorSwap()
			


	def solve(self):
		while 1:
			if (self.iteration > 105456):
				return "All combinations checked."

			plaintext = self.attempt()
			if ("ONE" in plaintext and "MINE" in plaintext): #we found the right message

				return plaintext
			else:
				self.rotorShift()
				self.iteration += 1



b = Bombe(sys.argv[1]) #the message is input as an argument
plaintext = b.solve()
print(plaintext)

#Test conditions used:

#	rotor1 = "GYRFNUCZLQDWMKHSJOEPBVITXA"
#	rotor2 = "MSEWGQHDPRFNXATOIBUJLCZVYK"
#	rotor3 = "SHBMFWEIQRODTAVXCPYZUJKGNL"
#	message = message = PZYGMGKHIZLLYVPMIDETWKXQCLRUNAHHCFAJSUVDZUODBTTXQDQZYMVNQXOKCNPQVLRKESAHBOEWZUKTWBQCWYEXJZTTUUHTMTERAQBDYFORQWLJCHYDRCQAZOKLBRSXHIICTUVPWAICHCSWXEDWOMPAORENVFNKDGSWXXEDSEQKTPVDHVCWHOMQPXNUBGULWWHANHETUJYITZVJYOERHVMYTRZCMALJASOGHHMGJXMWFLKFQBWPKMNOEVYWUWBVXXGHFYFRYKOQYZRGMDYUVQMLQFPFYTZWUKHAZTXYNNMEHARLWOATYKOYEJMLCOHWYPC
