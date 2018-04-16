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
        ensure(self.tur.tape).is_a(list).of(str)
        ensure(self.tur.state_table).is_a(dict).of(tuple).to(tuple)
        # see Turing machine executing 5 iterations (there is no halt state)
        print('\n'.join(self.tur.simulate(self.tur.state_table, 5)))

    def test_last_state_5_iterations(self):
        ensure(self.tur.simulate(self.tur.state_table, 5)[-1]).equals("  s2: XBBB\n       ^")

    def test_last_state_4_iterations(self):
        ensure(self.tur.simulate(self.tur.state_table, 4)[-1]).equals("  s1: BBBB\n      ^")

    def test_last_state_3_iterations(self):   
        ensure(self.tur.simulate(self.tur.state_table, 3)[-1]).equals("  s4: BBBB\n       ^")

    def test_last_state_2_iterations(self):
        ensure(self.tur.simulate(self.tur.state_table, 2)[-1]).equals("  s3: XBBB\n      ^")
    
    def test_last_state_1_iteration(self):
        ensure(self.tur.simulate(self.tur.state_table, 1)[-1]).equals("  s2: XBBB\n       ^")

    def test_output(self):
        ensure(self.tur.simulate(self.tur.state_table, 3)).is_a(list).of(str)
        self.setUp()
        ensure(self.tur.simulate(self.tur.state_table, 1)[0]).equals('  s1: BBBB\n      ^')
        self.setUp()
        ensure(self.tur.simulate(self.tur.state_table, 2)[0]).equals('  s1: BBBB\n      ^')
        self.setUp()
        ensure(self.tur.simulate(self.tur.state_table, 3)[0]).equals('  s1: BBBB\n      ^')
        self.setUp()
        ensure(self.tur.simulate(self.tur.state_table, 4)[0]).equals('  s1: BBBB\n      ^')
        self.setUp()
        ensure(self.tur.simulate(self.tur.state_table, 2)[1]).equals('  s2: XBBB\n       ^')
        self.setUp()
        ensure(self.tur.simulate(self.tur.state_table, 3)[2]).equals('  s3: XBBB\n      ^')
        self.setUp()
        ensure(self.tur.simulate(self.tur.state_table, 4)[3]).equals('  s4: BBBB\n       ^')

    def tearDown(self):
        del self.tur


if __name__ == '__main__':
    unittest.main()