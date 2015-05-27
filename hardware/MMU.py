class Frame(object):
    def __init__(self, program):
        self.id = program.pcb.getPID()
        self.start = 0
        self.size = len(program.getInstructions())


class MMU(object):
    def __init__(self, memory):
        self.memory = memory

    def nextInstruction(self):
        pass
