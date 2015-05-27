class Disk(object):
    def __init__(self, size):
        self.maxSize = size * 1024
        self.space = {x: None for x in range(0, self.maxSize)}

    def set(self, i, instruction):

        if i < self.maxSize:
            self.space[i] = instruction
        else:
            pass

    def get(self, i):
        return self.space[i]
