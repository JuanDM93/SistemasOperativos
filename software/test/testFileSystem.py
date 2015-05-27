import unittest

from software.FileSystem import *
from software.Program import *


class FileSystemTestCase(unittest.TestCase):
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
        self.string = self.fileSystem.addProgram(self.program1)
        assert self.string is None

    def test_GivenAFileSystem_WhenAddAProgram_ShouldBeReturnedByName(self):
        assert self.name == self.fileSystem.addProgram(self.program1)

    def test_GivenAFileSystem_WhenDeleteAnExistingProgram_ShouldReturnTrue(self):
        self.fileSystem.addProgram(self.program1)
        assert self.fileSystem.remProgram(self.name)

    def test_GivenAFileSystem_WhenDeleteANOTExistingProgram_ShouldReturnFalse(self):
        assert False == self.fileSystem.remProgram(self.name)


if __name__ == "__main__":
    unittest.main()
