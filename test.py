import unittest

from main import PidController
from main import ReadyQueue
from main import FileSystem

from main import Program

class PidControllerTestCase(unittest.TestCase):

    def setUp(self):
        self.pidController = PidController()

    def testNewPid(self):
        assert 1 == self.pidController.newPid()

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

class FileSystemTestCase(unittest.TestCase):

    def setUp(self):
        self.program1 = Program("Program1")
        self.program2 = Program("Program2")
        self.program3 = Program("Program3")
        self.fileSystem = FileSystem()

    def test_GivenAFileSystem_WhenAddAProgram_ShouldBeReturnedByName(self):
        pass

if __name__ == "__main__":
    unittest.main()
