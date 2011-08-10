import unittest
from ex1 import *    
class TestMain(unittest.TestCase):
    #def test_coisas(self):
    def test_diz_oi(self):
        self.assertEquals("Alo mundo", oi())

    def test_numero_confere(self):
        self.assertEquals("o numero informado foi 3", informa_numero(3))


if __name__ == '__main__' :
    unittest.main()

