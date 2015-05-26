import time
import threading


class Clock(threading.Thread):
    def __init__(self, aCpu):
        super(Clock, self).__init__()
        self.running = True
        self.cpu = aCpu

    def tick(self):
        self.cpu.tick()

    def run(self):
        while self.running:
            print("ticking and sleeping")
            self.tick()
            time.sleep(1)

    def stoprunning(self):
        self.running = False
