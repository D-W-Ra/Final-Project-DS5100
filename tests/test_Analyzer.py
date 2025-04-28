import unittest
import numpy as np
from montecarlo.die import Die
from montecarlo.game import Game
from montecarlo.analyzer import Analyzer
import pandas as pd

class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        faces = np.array(['H', 'T'])
        die1 = Die(faces)
        die2 = Die(faces)
        self.game = Game([die1, die2])
        self.game.play(10)
        self.analyzer = Analyzer(self.game)

    def test_jackpot_output(self):
        jackpots = self.analyzer.jackpot()
        self.assertIsInstance(jackpots, int)

    def test_face_counts_per_roll_output(self):
        face_counts = self.analyzer.face_counts_per_roll()
        self.assertIsInstance(face_counts, pd.DataFrame)
        self.assertEqual(face_counts.shape[0], 10)

    def test_combo_output(self):
        combo = self.analyzer.combo()
        self.assertIsInstance(combo, pd.DataFrame)

    def test_permutation_output(self):
        perm = self.analyzer.permutation()
        self.assertIsInstance(perm, pd.DataFrame)

    def test_invalid_analyzer_input(self):
        with self.assertRaises(ValueError):
            Analyzer("not_a_game")