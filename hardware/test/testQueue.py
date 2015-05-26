import unittest

from hardware.Queue import *
from software.PCB import *


class ReadyQueueTestCase(unittest.TestCase):
    def setUp(self):
        self.readyQueue = ReadyQueue()
        self.pidController = PidController()

    def test_GivenAnEmptyReadyQueue_WhenPutAPidAndGetIt_ItShouldReturnThatPid(self):
        self.pid = self.pidController.newPid()
        self.readyQueue.insert(self.pid)
        assert self.pid == self.readyQueue.take()

    def test_GivenAnEmptyReadyQueue_WhenPutMultiplePidsAndGetIt_ItShouldReturnTheFirstPid(self):
        self.pid = self.pidController.newPid()
        self.readyQueue.insert(self.pid)
        self.readyQueue.insert(self.pidController.newPid())
        self.readyQueue.insert(self.pidController.newPid())
        self.readyQueue.insert(self.pidController.newPid())
        self.readyQueue.insert(self.pidController.newPid())
        assert self.pid == self.readyQueue.take()
        assert self.readyQueue.take() != self.readyQueue.take()


if __name__ == "__main__":
    unittest.main()
