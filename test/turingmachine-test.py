# -*- coding: utf-8 -*-

"""
    tests for turing machine

"""

import unittest
import sys
sys.path.extend([".", ".."])

from ensure import ensure
from src.turingmachine import TuringMachine

class TuringMachineTestCase(unittest.TestCase):
    
    def setUp(self):
        self.tur = TuringMachine()
       

    def test_init(self):
        print("\n")
        ensure(self.tur).is_a(TuringMachine)
        ensure(self.tur.tape1).is_a_list_of(str)
        # ensure(self.tur.state_table1).is_a_dict_of((chr, chr)).to((chr, chr, chr))

    def tearDown(self):
        del self.tur


if __name__ == '__main__':
    unittest.main()