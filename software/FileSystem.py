class FileSystem(object):
    def __init__(self):
        self.fileSystem = {}

    def addProgram(self, program):
        self.fileSystem[program.name] = program.instructions
        return program.name
