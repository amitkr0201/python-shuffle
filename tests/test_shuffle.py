import unittest
from shuffle.shuffle import Shuffle

class TddInPythonExample(unittest.TestCase):

    def test_range_should_be_between_one_and_six(self):
        shuffler = Shuffle()
        expectedResult = shuffler.run()
        assert expectedResult > 0 and expectedResult <=6