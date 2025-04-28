import unittest
import numpy as np
import pandas as pd
from montecarlo.die import Die
from montecarlo.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        faces = np.array(['A', 'B', 'C'])
        die1 = Die(faces)
        die2 = Die(faces)
        self.game = Game([die1, die2])

    def test_play_shape(self):
        self.game.play(10)
        result = self.game.show()
        self.assertEqual(result.shape, (10, 2))

    def test_show_wide_format(self):
        self.game.play(5)
        result = self.game.show('wide')
        self.assertIsInstance(result, pd.DataFrame)

    def test_show_narrow_format(self):
        self.game.play(5)
        result = self.game.show('narrow')
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result.index.nlevels, 2)

    def test_show_invalid_format(self):
        self.game.play(5)
        with self.assertRaises(ValueError):
            self.game.show('medium')