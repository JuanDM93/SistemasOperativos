import unittest

from hardware.Memory import Memory
from software.Program import *

class MemoryTestCase(unittest.TestCase):
    def setUp(self):
        self.memory = Memory(8)
        self.instruction = Instruction(0, "Add")

    def test_GivenAnEmptyMemory_WhenGetAnInstruction_ShouldReturnNull(self):
        assert None == self.memory.get(0x0a)

    def test_GivenAMemory_WhenPutAnInstruction_ShouldReturnThatInstruction(self):
        self.memory.set(0x0, self.instruction)
        assert self.instruction == self.memory.get(0x0)

if __name__ == "__main__":
    unittest.main()
