class Frame(object):
    def __init__(self, program):
        self.id = pcb.getPID()
        self.start = 0
        self.size = len(program.getInstructions())


class MMU(object):
    def __init__(self):
        pass

    def nextInstruction(self):
        pass
