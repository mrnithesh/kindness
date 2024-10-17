import unittest
from kindness import random_act, gratitude, compliment

class TestKindness(unittest.TestCase):
    def test_random_act(self):
        act = random_act()
        self.assertIsInstance(act, str)
        self.assertTrue(len(act) > 0)

    def test_gratitude(self):
        note = gratitude()
        self.assertIsInstance(note, str)
        self.assertTrue(len(note) > 0)

    def test_compliment(self):
        comp = compliment()
        self.assertIsInstance(comp, str)
        self.assertTrue(len(comp) > 0)

if __name__ == '__main__':
    unittest.main()