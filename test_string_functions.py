"""
Robert Walczak
tests the multiply_string function with a known message and known n
"""

import more_functions.string_functions as string_func
import unittest

class nameTest(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(len(string_func.multiply_string('Billy',2)),10)

if __name__=='__main__':
    unittest.main()
