#   Erich Eden
#   SY301
#   Dr. Mayberry
#   Enigma project


class Rotor:
    def __init__(self, setting):
        self.rlist = list(setting)
        self.initial = self.rlist[0]
        return

    def encryptLetter(self, letter): #ASCII conversion to find corresponding letter in rlist
        pos = (ord(letter) - 65)
        cipherLetter = self.rlist[pos]
        return cipherLetter

    def decryptLetter(self, letter):
        pos = self.rlist.index(letter) #get the position of the given letter in the rotor
        decrypted = chr(65 + pos) #convert that position to plaintext
        return decrypted

    def click(self):
        #self.rlist needs to rotate
        tmp = self.rlist[0]
        for i in range (25):
            self.rlist[i] = self.rlist[i+1]
        self.rlist[25] = tmp

        if (self.rlist[0] == self.initial):
            return True
        else:
            return False
        return
    def reset(self):
        while (self.rlist[0] != self.initial):
            self.click()
        return

class Enigma:
    def __init__(self, rotor1, rotor2, rotor3): #feed in the settings for each rotor
        self.rotor1 = Rotor(rotor1)
        self.rotor2 = Rotor(rotor2)
        self.rotor3 = Rotor(rotor3)
        return
    def encrypt(self, message):
        self.rotor1.reset() #in case I already used this machine to encode or decode
        self.rotor2.reset()
        self.rotor3.reset()
        plaintext = list(message)
        ciphertext = []
        rotate1 = False
        rotate2 = False
        for i in range(0, len(plaintext)):
            ct = self.rotor1.encryptLetter(plaintext[i])
            ct = self.rotor2.encryptLetter(ct)
            ct = self.rotor3.encryptLetter(ct)
            if (self.rotor3.click() == True):
                if (self.rotor2.click() == True):
                    self.rotor1.click()

            ciphertext.append(ct)
        ciphertext = ''.join(ciphertext)
        #print(ciphertext)
        return ciphertext

        
    def decrypt(self, message):
        self.rotor1.reset() #in case I encoded then decoded in the same program, or want to decrypt multiple messages
        self.rotor2.reset()
        self.rotor3.reset()
        ciphertext = list(message)
        plaintext = []
        rotate1 = False #these are set to false to tell rotors 2 and 1 not to click
        rotate2 = False
        for i in range(0,len(ciphertext)):
            pt = self.rotor3.decryptLetter(ciphertext[i])
            rotate2 = (self.rotor3.click()) #set to true when rotor 3 is back where it started
            pt = self.rotor2.decryptLetter(pt)
            if (rotate2):
                rotate1 = self.rotor2.click() #set to true when rotor 2 is back where it started
            pt = self.rotor1.decryptLetter(pt)
            if (rotate1):
                self.rotor1.click()
            plaintext.append(pt)
        plaintext = ''.join(plaintext)
        #print(plaintext)
        return plaintext
