class FileSystem(object):
    def __init__(self, disk):
        self.disk = disk

    def addProgram(self, program):
        if self.disk.has_key(program):
            return None
        else:
            self.disk[program.name] = program.instructions
            return program.name


class FileSystemHasThatProgramError(Exception):
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg
