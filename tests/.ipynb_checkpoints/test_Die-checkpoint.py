import unittest
import numpy as np
from montecarlo.die import Die

class TestDie(unittest.TestCase):

    def setUp(self):
        self.faces = np.array(['A', 'B', 'C'])
        self.die = Die(self.faces)

    def test_initial_weights(self):
        result = self.die.show()
        expected_weights = [1.0, 1.0, 1.0]
        self.assertListEqual(result['weight'].tolist(), expected_weights)

    def test_change_weight(self):
        self.die.change_weight('A', 2.5)
        result = self.die.show()
        self.assertEqual(result.loc['A', 'weight'], 2.5)

    def test_roll_return_type(self):
        rolls = self.die.roll(5)
        self.assertIsInstance(rolls, list)
        self.assertEqual(len(rolls), 5)

    def test_invalid_face_change_weight(self):
        with self.assertRaises(IndexError):
            self.die.change_weight('Z', 2.0)

    def test_invalid_weight_type(self):
        with self.assertRaises(TypeError):
            self.die.change_weight('A', "heavy")