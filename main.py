import Queue

class ReadyQueue(object):

    def __init__(self):
        self.queue = Queue.Queue()

    def insert(self, pid):
        self.queue.put(pid)

    def take(self):
        return self.queue.get()

class Program(object):

    def __init__(self, name):
        self.name = name
        self.instructions = []

class PCB(object):

    def __init__(self):
        self.pid = 0
        self.pc = 0
        self.state = 0
        self.priority = 0

    def getPID(self, pid):
        self.pid = pid

class Kernel(object):

    def __init__(self, scheduler, pidController):
        self.scheduler = scheduler
        self.pidController = pidController

    def newProcess(self, program):
        program.pcb.pid = self.pidController.newPid()
        self.scheduler.setState(program)

class PidController(object):

    def __init__(self):
        self.currentPid = 0

    def newPid(self):
        self.currentPid += 1
        return self.currentPid

class FileSystem(object):

    def __init__(self):
        self.fileSystem = {}

    def addProgram(self, program):
        self.fileSystem[program.name] = program.instructions
        return program.name


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

class Scheduler(object):

    def __init__(self):
        pass

    def setState(self, program):
        program.pcb.state = 1