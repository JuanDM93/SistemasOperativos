import unittest

from software.Program import *


class ProgramTestCase(unittest.TestCase):
    def setUp(self):
        self.program = Program()
        self.instruction = Instruction()


if __name__ == "__main__":
    unittest.main()
