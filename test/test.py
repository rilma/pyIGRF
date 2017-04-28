#!/usr/bin/env python
''' Test 
    $ python -m unittest -v test.py 
'''
from pyigrf.pyigrf import GetIGRF
import unittest

xlat = -11.95
xlon = 283.13
year = 2004.75
alt = 250

bn, be, bd, xl, icode = GetIGRF(xlat, xlon, alt, year)


class TestIGRF(unittest.TestCase):

    ''' class '''

    def test_one_bn(self):

        ''' test '''

        self.assertAlmostEqual(bn, 0.232339769, 7)


    def test_one_be(self):

        ''' test '''

        self.assertAlmostEqual(be, -0.00033941, 7)


    def test_one_bd(self):

        ''' test '''

        self.assertAlmostEqual(bd, 0.00395644, 7)


if __name__ == '__main__':
    unittest.main()
