class CPU(object):

    def __init__(self):
        self.pc
        self.instruction

    def fetch(self):
        self.pc += 1
        self.instruction = self.MMU.nextInstruction()

    def run(self):
        self.pc += 1
        print self.instruction
