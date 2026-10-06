import unittest
from project import calculations

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = calculations(5, '+', 5)
        self.assertEqual(result, 10)

    def test_subtraction(self):
        result = calculations(5, '-', 3)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = calculations(4, '*', 20)
        self.assertEqual(result, 80)

    def test_division(self):
        result = calculations(15, '/', 3)
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        result = calculations(1, '/', 0)
        self.assertEqual(result, "Cannot divide by zero!")

if __name__ == '__main__':
    unittest.main()