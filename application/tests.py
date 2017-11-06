#!/usr/bin/python

import unittest

from worker import roman_parse


class TestRomanConversion(unittest.TestCase):
    """
        Unit Tests for the solution itself.Expand the values list if needed, 
        run with 'python application/tests.py' from the repo root.
    """

    def setUp(self):
        self.numbers = [(1, 'I'), (3, 'III'), (4, 'IV'), (27, 'XXVII'), (44, 'XLIV'),
                        (93, 'XCIII'), (141, 'CXLI'), (402, 'CDII'), (575, 'DLXXV'),
                        (1024, 'MXXIV'), (3000, 'MMM'), (4000, '~IV'), (4024, '~IVXXIV'),
                        (5000, '~V'), (5024, '~VXXIV'), (6000, '~VI'), (6024, '~VIXXIV'),
                        (7000, '~VII'), (7024, '~VIIXXIV'), (8000, '~VIII'), (8024, '~VIIIXXIV'),
                        (9000, '~IX'), (9024, '~IXXXIV'), (10000, '~X')]

    def test_to_roman(self):
        for num in self.numbers:
            self.assertEqual(num[1], roman_parse(num[0]))

if __name__ == '__main__':
    unittest.main()