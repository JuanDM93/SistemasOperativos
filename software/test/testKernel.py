import unittest

from software.Kernel import Kernel

class KernelTestCase(unittest.TestCase):
    def setUp(self):
        self.kernel = Kernel()


if __name__ == "__main__":
    unittest.main()
