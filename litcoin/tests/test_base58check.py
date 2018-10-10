#!/usr/bin/env python3

import unittest
from litcoin.base58check import base58check_encode, base58check_decode


TEST_CASES = [
    {'hex': '', 'base58check': '3QJmnh'},
    {'hex': '00', 'base58check': '1Wh4bh'},
    {'hex': '01', 'base58check': 'BXvDbH'},
    {'hex': '0000', 'base58check': '112edB6q'},
    {'hex': '000100', 'base58check': '1Vyy3ex3'},
    {'hex': '00010001', 'base58check': '13CUzk4iA2'},
    {'hex': 'ff', 'base58check': 'VrZDWwe'},
    {'hex': 'ffff', 'base58check': '3CUsNEUP5'},
    {'hex': '0102030405060708090a0b0c0d0e0f', 'base58check': 'Bhh3pU9gLXZiNDL6PEZxnvuRw'}
]

class TestBase58Check(unittest.TestCase):
    def test_base58check_encode(self):
        for test_case in TEST_CASES:
            actual = base58check_encode(bytes.fromhex(test_case['hex']))
            expected = test_case['base58check']
            assert actual == expected


    def test_base58check_decode(self):
        for test_case in TEST_CASES:
            actual = base58check_decode(test_case['base58check'])
            expected = bytes.fromhex(test_case['hex'])
            assert actual == expected
