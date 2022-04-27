import unittest
from teste import somas


class TestCalculadora(unittest.TestCase):
    def Test_5_e_5_retorna_10(self):
        self.assertEqual(somas(5, 5), 10)


unittest.main(verbosity=2)
