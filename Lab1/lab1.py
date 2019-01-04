#   Erich Eden
#   SY301
#   Dr. Mayberry
#   Lab 1


class Adding:
   def __init__(self, num1, num2):
       self.num1 = num1
       self.num2 = num2

   def addEm(self, num3):
       total = self.num1 + self.num2 + num3
       return total

   def __str__(self):
       return "Adding: (" + str(self.num1) + ", " + str(self.num2) + ")"
