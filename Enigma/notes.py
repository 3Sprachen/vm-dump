#   Erich Eden
#   SY301
#   Dr. Mayberry
#   Enigma Bombe

from enigma import *

class Setting:
	def __init__(self, setting):
		self.rlist = list(setting)
        self.initial = self.rlist[0]
        return



def Attempt(message, setting1, setting2, setting3):

	e = Enigma(setting1, setting2, setting3)
	plaintext = e.decrypt(message)
	if ("ONE" and "MINE" in plaintext):
		print(plaintext)
		return True
	else:
		return False

initial1 = list("GYRFNUCZLQDWMKHSJOEPBVITXA")
initial2 = list("MSEWGQHDPRFNXATOIBUJLCZVYK")
initial3 = list("SHBMFWEIQRODTAVXCPYZUJKGNL")
