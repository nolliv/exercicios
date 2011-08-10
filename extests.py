import unittest
from ex1 import *    
class TestMain(unittest.TestCase):
    #1
    def test_diz_oi(self):
        self.assertEquals("Alo mundo", oi())
    #2
    def test_numero_confere(self):
        self.assertEquals("o numero informado foi 3", informa_numero(3))
    #3
    def test_soma_numeros(self):
        self.assertEquals(5, soma_numeros(2, 3))
    #4 
    def test_tira_media(self):
	self.assertEquals(5, media(5, 5, 5, 5))
    #5
    def test_converte_metros_em_centimetros(self):
	self.assertEquals(500, conversor(5))
    #6
    def test_calcula_area_do_circulo(self):
	self.assertEquals(12.56, circulo(2))
    #7
    def test_retorna_dobro_da_area(self):
		self.assertEquals(8, dobroarea(2))

    #8 pulei			
    #9
    #10
    #11
    #12
    #13
    #14
    #15
    #16
    #17
    #18

if __name__ == '__main__' :
    unittest.main()

