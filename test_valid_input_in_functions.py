


import unittest
import more_functions.validate_input_in_functions as score_ave


class test_score_input_test_score_valid(unittest.TestCase):

        def test_score_input_test_score_valid(self):
           self.assertEqual(('Python', 75), score_ave.score_test_average('Python', '75', 'invalid'))

        def test_score_input_test_score_below_range(self):
            self.assertEqual(('Python', 'invalid'), score_ave.score_test_average('Python', '-75', 'invalid'))


        def test_score_input_test_score_above_range(self):
           self.assertEqual(('Python', 'invalid'), score_ave.score_test_average('Python', '150', 'invalid'))


        def test_test_score_non_numeric(self):
            self.assertEqual(('Python',  'invalid'), score_ave.score_test_average('Python', 'out', 'invalid'))




if __name__ == '__main__':
    unittest.main()