"""Module to simulate roll for six-faced size."""
import random

class Shuffle(object):
    """Class to define a dice, incorrectly named Shuffle"""
    def roll_dice(self):
        return random.randint(1,6)
