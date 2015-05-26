import time
import unittest

from mockito import *

from hardware.Clock import Clock


class ClockTestCase(unittest.TestCase):
    def setUp(self):
        self.cpu = mock()
        self.clock = Clock(self.cpu)

    def test_GivenAClock_WhenStart_ShouldSendCpuTick(self):
        self.clock.start()
        time.sleep(0.1)
        verify(self.cpu).tick()

    def test_GivenAClock_WhenStart_ShouldVerifyFiveTicksInFiveSeconds(self):
        self.clock.start()
        time.sleep(5)
        verify(self.cpu, times=5).tick()

    def test_GivenAClock_WhenStart_ShouldNoSendTwoTicksInOneSecond(self):
        self.clock.start()
        time.sleep(0.1)
        verify(self.cpu).tick()
        time.sleep(0.5)
        verifyNoMoreInteractions(self.cpu)

    def tearDown(self):
        self.clock.stoprunning()


if __name__ == "__main__":
    unittest.main()
