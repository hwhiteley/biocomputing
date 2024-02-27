import unittest
from practical8 import f_measure

class TestFMeasureFunction(unittest.TestCase):

    def test_f_measure_positive_num(self):
        self.assertEqual(f_measure(10,10,10), 0.5)

    def test_f_measure_negative_tp(self):
        with self.assertRaises(ValueError):
            f_measure(-10, 10, 10)

    def test_f_measure_zero(self):
        with self.assertRaises(ValueError):
            f_measure(0, 0, 0)

if __name__ == '__main__':
    unittest.main()

