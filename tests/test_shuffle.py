"""Test for shuffle class"""
import unittest
from shuffle.shuffle import Shuffle

class ShuffleInPython(unittest.TestCase):
    """Class to definte shuffle tests"""

    def test_range_should_be_between_one_and_six(self):
        """Test shuffle test"""
        shuffler = Shuffle()
        expected_result = shuffler.roll_dice()
        assert expected_result > 0 and expected_result <=6
