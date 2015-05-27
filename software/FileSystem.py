class FileSystem(object):

    def __init__(self):
        self.fileSystem = {}

    def addProgram(self, program):
        if self.fileSystem.has_key(program):
            return None
        else:
            self.fileSystem[program.name] = program.instructions
            return program.name


class FileSystemHasThatProgramError(Exception):
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg
