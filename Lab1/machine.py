#   Erich Eden
#   SY301
#   Dr. Mayberry
#   Lab 1: machine.py


class Process:
    def __init__(self, name, memoryReq):
        self.name = name
        self.memoryReq = memoryReq
    def __str__(self):
        return str(self.name) + ": " + str(self.memoryReq) + "KB "


class Machine:
    def __init__(self, name, totalMem): #process list?
        self.name = name
        self.processList = []
        self.totalMem = totalMem
    def addProcess(self, Process):
        self.processList.append(Process)
    def availableMemory(self):
        usedMem = 0
        i = 0
        while i < len(self.processList):
            usedMem += self.processList[i].memoryReq
            i+=1
        availMem = self.totalMem - usedMem
        return availMem
    def __str__(self):
        displayMessage = self.name + ", " + str(self.totalMem) + "KB"
        procDisplay = 0
        while procDisplay < len(self.processList):
            displayMessage += "\n\t" + self.processList[procDisplay].name + ": " + str(self.processList[procDisplay].memoryReq) + "KB"
            procDisplay += 1
        return displayMessage
