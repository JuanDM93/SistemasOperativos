class Memory(object):
    def __init__(self, size):
        self.maxMemory = size
        self.memory = []

    def put(self, i, instruction):
        if i < self.maxMemory:
            self.memory[i] = instruction
        else:
            pass

    def get(self, i):
        return self.memory[i]
