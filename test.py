import unittest
from main import remainder

class TestRemainderFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(remainder(10, 3), 1)

    def test_zero_dividend(self):
        self.assertEqual(remainder(0, 5), 0)

    def test_divisor_one(self):
        self.assertEqual(remainder(10, 1), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            remainder(10, 0)


if __name__ == "__main__":
    unittest.main()