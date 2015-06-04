#!/usr/bin/python

import unittest
from ReflexivePosition import ReflexivePosition
from ReflexivePosition import InfiniteString

class ReflexivePositionTest(unittest.TestCase):

    def test_reflexive_position(self):

        reflPosn = ReflexivePosition()

        self.assertEqual(reflPosn.f(0), 0, 'testing out of bound condition')
        self.assertEqual(reflPosn.f(-5), 0, 'testing out of bound condition')

        self.assertEqual(reflPosn.f(1), 1, 'answer given in problem statement')
        self.assertEqual(reflPosn.f(5), 81, 'answer given in problem statement')
        self.assertEqual(reflPosn.f(12), 271, 'answer given in problem statement')
        self.assertEqual(reflPosn.f(7780), 111111365, 'answer given in problem statement')

    def test_infinite_string(self):

        infiniteString = InfiniteString(howManyToAdd=-5)
        self.assertEqual(infiniteString.toString(), '', 'testing out of bound condition')

        infiniteString = InfiniteString(howManyToAdd=0)
        self.assertEqual(infiniteString.toString(), '', 'testing the howManyToAdd of 0')

        infiniteString = InfiniteString()
        self.assertEqual(infiniteString.toString(), '12345678910', 'testing default condition')

        infiniteString = InfiniteString(howManyToAdd=5)
        self.assertEqual(infiniteString.toString(), '12345', 'testing the changing of default howManyToAdd')

        # THE FOLLOWING SECTION IS SEQUENTIAL, DO NOT REMOVE OR ADD TO IT UNLESS YOU UNDERSTAND THIS

        infiniteString = InfiniteString(howManyToAdd=5)
        infiniteString.addMoreDigits()
        self.assertEqual(infiniteString.toString(), '12345678910', 'testing the adding of more digits')

        infiniteString.keepLast(4)
        self.assertEqual(infiniteString.toString(), '8910', 'testing the keepRight (shift Left)')

        infiniteString.keepLast(6)
        self.assertEqual(infiniteString.toString(), '8910', 'testing the keepRight (shift Left) where you are keeping more than you have')

        infiniteString.keepLast(1)
        self.assertEqual(infiniteString.toString(), '0', 'testing the keepRight (shift Left) where you are keep 1')

        infiniteString.keepLast(0)
        self.assertEqual(infiniteString.toString(), '', 'testing the keepRight (shift Left) where you are keep nothing')

        infiniteString.addMoreDigits()
        self.assertEqual(infiniteString.toString(), '1112131415', 'testing additional addMoreDigits from last number of 10')

        infiniteString.keepLast(-10)
        self.assertEqual(infiniteString.toString(), '', 'testing the keepRight with a negative input which should leave nothing')
        
        infiniteString.addMoreDigits()
        infiniteString.addMoreDigits()
        infiniteString.addMoreDigits()
        self.assertEqual(infiniteString.toString(), '161718192021222324252627282930', 'testing additional addMoreDigits from last number of 15')

        infiniteString.keepLast(30)
        self.assertEqual(infiniteString.toString(), '161718192021222324252627282930', 'testing the keepRight with keeping everything (edge condition)')

        # THE ABOVE SECTION IS SEQUENTIAL, DO NOT REMOVE OR ADD TO IT UNLESS YOU UNDERSTAND THIS

if __name__ == '__main__':
    unittest.main()
