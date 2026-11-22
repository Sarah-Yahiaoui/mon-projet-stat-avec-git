import unittest
import numpy as np
from main import (
    calcul_moyenne,
    calcul_variance,
    calcul_ecart_type,
    calcul_mediane,
    calcul_somme,

)

class TestStatistiques(unittest.TestCase):
    def setUp(self):
        self.notes = [10, 20, 30]

    def test_moyenne(self):
        self.assertEqual(
            calcul_moyenne(self.notes), 20
        )

    def test_variance(self):
        self.assertAlmostEqual(
            calcul_variance(self.notes), 200/3
        )

    def test_ecart_type(self):
        self.assertAlmostEqual(
            calcul_ecart_type(self.notes), np.sqrt(200/3)
        )

    def test_mediane(self):
        self.assertEqual(
            calcul_mediane(self.notes), 20
        )

    def test_somme(self):
        self.assertEqual(
            calcul_somme(self.notes), 60
        )


if __name__ == "__main__":
    unittest.main()