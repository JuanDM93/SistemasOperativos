class Program(object):
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

    def getInstructions(self):
        return self.instructions

    def getName(self):
        return self.name

class Instruction(object):
    def __init__(self, mode, instruction):
        self.mode = mode
        self.instruction = instruction

    def getMode(self):
        return self.mode

    def read(self):
        return self.instruction
