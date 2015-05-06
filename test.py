import unittest

from main import PidController
from main import ReadyQueue
from main import FileSystem
from main import Program
from main import Memory


class MemoryTest:  # H

    def SetUp(self):
        self.memory = Memory(8)
        self.intruction = "Start"

    def test_GivenAnEmptyMemory_WhenGetAnInstruction_ShouldReturnNull(self):
        assert None == self.memory.get(0x0a)

    def test_GivenAMemory_WhenPutAnInstruction_ShouldReturnThatInstruction(self):
        self.memory.put(0x0, self.intruction)
        assert self.instruction == self.memory.get(0x0)


class PidControllerTestCase(unittest.TestCase):  # S

    def setUp(self):
        self.pidController = PidController()

    def testNewPid(self):
        assert 1 == self.pidController.newPid()


class ReadyQueueTestCase(unittest.TestCase):  # S

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


class FileSystemTestCase(unittest.TestCase):  # S

    def setUp(self):
        self.i1 = "start"
        self.i2 = "run"
        self.i3 = "end"
        self.name = "NombrePrograma"
        self.instructions = [self.i1, self.i2, self.i3]
        self.program1 = Program(self.name, self.instructions)
        self.fileSystem = FileSystem()

    def test_GivenAFileSystemWithAProgram_WhenAddAProgramWithTheSameName_ShouldRaiseAnError(self):
        assert self.name == self.fileSystem.addProgram(self.program1)
        try:
            self.string == self.fileSystem.addProgram(self.program1)
        except FileSystemHasThatProgramError:
            print "El Programa ya esta instalado"
            assert self.string == self.name


    def test_GivenAFileSystem_WhenAddAProgram_ShouldBeReturnedByName(self):
        assert self.name == self.fileSystem.addProgram(self.program1)

    def test_GivenAFileSystem_WhenDeleteAnExistingProgram_ShouldReturnTrue(self):
        self.fileSystem.addProgram(self.program1)
        assert self.fileSystem.remProgram(self.name)

    def test_GivenAFileSystem_WhenDeleteANOTExistingProgram_ShouldReturnFalse(self):
        assert False == self.fileSystem.remProgram(self.name)


if __name__ == "__main__":
    unittest.main()
