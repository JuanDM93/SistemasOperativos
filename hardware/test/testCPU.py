import unittest

from hardware.Clock import Clock
from hardware.CPU import CPU


class CPUTestCase(unittest.TestCase):
    def setUp(self):
        self.cpu = CPU(self)
        self.clock = Clock(self.cpu)

    def test_GivenACpu_WhenStart_ShouldSendCpuTick(self):
        self.clock.start()


if __name__ == "__main__":
    unittest.main()
