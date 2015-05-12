__author__ = 'applicant'
import unittest
from challenge import reducer

class TestReducer(unittest.TestCase):

    def test_reduce(self):
        function_output = list(reducer.reduce(['Bob\tSnippy', 'Bob\tAmanda', 'Bob\tZach']))
        expected = ['Bob\tAmanda\tSnippy\tZach']

        self.assertListEqual(function_output, expected, 'Unexpected Reduce Output')


if __name__ == '__main__':
    unittest.main()
