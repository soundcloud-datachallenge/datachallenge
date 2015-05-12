__author__ = 'applicant'
import unittest
from challenge import mapper

class TestMapper(unittest.TestCase):

    def test_map(self):
        function_output = list(mapper.map(['Bob\tSnippy']))
        expected = ['Bob\tSnippy', 'Snippy\tBob']

        self.assertListEqual(function_output, expected, 'Unexpected Map Output')

    def test_friend_permutations(self):
        function_output = list(mapper.friend_permutations(['Kashi', 'Bob', 'Snippy']))
        expected = [('Kashi', 'Bob'),
                    ('Kashi', 'Snippy'),
                    ('Bob', 'Kashi'),
                    ('Bob', 'Snippy'),
                    ('Snippy', 'Kashi'),
                    ('Snippy', 'Bob')]

        self.assertListEqual(function_output, expected, 'Unexpected Permutations')

if __name__ == '__main__':
    unittest.main()