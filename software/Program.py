class Program(object):
    def __init__(self, name):
        self.name = name
        self.instructions = []


class Instruction(object):
    def __init__(self, mode, instruction):
        self.mode = mode
        self.instruction = instruction

    def getMode(self):
        return self.mode

    def read(self):
        return self.instruction
