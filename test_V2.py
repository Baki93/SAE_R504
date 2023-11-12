import unittest
from unittest.mock import patch
from v2 import Personnage

class TestPersonnageMethods(unittest.TestCase):

    def test_attaquer(self):
        personnage = Personnage("Test", 100, 20, 30, 10)
        adversaire = Personnage("Adversaire", 100, 20, 15, 10)

        with patch('builtins.input', return_value='1'):
            personnage.attaquer(adversaire, 1)
            self.assertLess(adversaire.points_de_vie, 100)

    def test_utiliser_sort(self):
        personnage = Personnage("Test", 100, 20, 30, 10)
        adversaire = Personnage("Adversaire", 100, 20, 15, 10)

        with patch('builtins.input', return_value='1'):
            personnage.utiliser_sort(adversaire, 1)
            self.assertGreater(personnage.endurance, 20)

    def test_se_defendre(self):
        personnage = Personnage("Test", 100, 20, 30, 10)
        defense_initiale = personnage.defense
        esquive_initiale = personnage.esquive

        personnage.se_defendre()
        self.assertEqual(personnage.defense, defense_initiale + 5)
        self.assertEqual(personnage.esquive, esquive_initiale + 10)

    def test_ameliorer_caracteristique(self):
        personnage = Personnage("Test", 100, 20, 30, 10)
        points_de_vie_initiaux = personnage.points_de_vie

        with patch('builtins.input', return_value='1'):
            personnage.ameliorer_caracteristique(1)
            self.assertEqual(personnage.points_de_vie, points_de_vie_initiaux + 20)

if __name__ == '__main__':
    unittest.main()
