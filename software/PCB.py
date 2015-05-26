class PCB(object):
    def __init__(self):
        self.pid = 0
        self.pc = 0
        self.state = 0
        self.priority = 0

    def getPID(self, pid):
        self.pid = pid


class PidController(object):
    def __init__(self):
        self.currentPid = 0

    def newPid(self):
        self.currentPid += 1
        return self.currentPid
