import unittest

from software.Program import *

class ProgramTestCase(unittest.TestCase):

    def setUp(self):
        self.instruction1 = Instruction(True, "start")
        self.instruction2 = Instruction(False, "io")
        self.instruction3 = Instruction(True, "run")
        self.instruction4 = Instruction(True, "end")
        self.instros = (self.instruction1, self.instruction2, self.instruction3, self.instruction4)
        self.program = Program("pacman", self.instros)

    def test_GivenANewProgramWithAnInstructionSet_GetTheNextInstructionFromModeTrue(self):
        self.count = 0
        for x in self.program.getInstructions():
            if x.getMode() is True:
                print x.read()
                self.count += 1
        assert self.count == 3

if __name__ == "__main__":
    unittest.main()
