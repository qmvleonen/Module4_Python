import math
import unittest

class TestSqrt(unittest.TestCase):
    def test_sqrt_25(self):
        num = 25
        self.assertEqual(math.sqrt(num), 5)

    def test_square_7(self):
        num = 7
        self.assertEqual(num * num, 49)

if __name__ == '__main__':
    unittest.main()
