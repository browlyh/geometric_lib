import unittest

# Importing the functions to be tested from square.py
from square import area, perimeter

class TestSquareFunctions(unittest.TestCase):

    def test_area(self):
        # Test cases for the area function
        self.assertEqual(area(0), 0)      # Area of a square with side 0 should be 0
        self.assertEqual(area(1), 1)      # Area of a square with side 1 should be 1
        self.assertEqual(area(2), 4)      # Area of a square with side 2 should be 4
        self.assertEqual(area(5), 25)     # Area of a square with side 5 should be 25
        self.assertEqual(area(10), 100)   # Area of a square with side 10 should be 100

    def test_perimeter(self):
        # Test cases for the perimeter function
        self.assertEqual(perimeter(0), 0)      # Perimeter of a square with side 0 should be 0
        self.assertEqual(perimeter(1), 4)      # Perimeter of a square with side 1 should be 4
        self.assertEqual(perimeter(2), 8)      # Perimeter of a square with side 2 should be 8
        self.assertEqual(perimeter(5), 20)     # Perimeter of a square with side 5 should be 20
        self.assertEqual(perimeter(10), 40)    # Perimeter of a square with side 10 should be 40

if __name__ == '__main__':
    unittest.main()