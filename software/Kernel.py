class Kernel(object):
    def __init__(self, scheduler, pidController):
        self.scheduler = scheduler
        self.pidController = pidController

    def newProcess(self, program):
        program.pcb.pid = self.pidController.newPid()
        self.scheduler.setState(program)
