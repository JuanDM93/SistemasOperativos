from software.Program import *


class PidController(object):
    def __init__(self):
        self.currentPid = 0

    def newPid(self):
        self.currentPid += 1
        return self.currentPid

class Kernel(object):
    def __init__(self, scheduler):
        self.scheduler = scheduler
        self.pidController = PidController()
        self.kernelThread = Program("Kernel", (Instruction(False, "kernelTask")))

    def newProcess(self, program):
        program.pcb.pid = self.pidController.newPid()
        self.scheduler.setState(program)

    def start(self):
        self.newProcess(self.kernelThread)
