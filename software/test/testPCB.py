import unittest

from software.PCB import *

class PidControllerTestCase(unittest.TestCase):

    def setUp(self):
        self.pidController = PidController()

    def test_CreateANewPid(self):
        assert 1 == self.pidController.newPid()

if __name__ == "__main__":
    unittest.main()
