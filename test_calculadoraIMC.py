# 1) Importar a classe
# "Calculadora"
from calculadoraIMC import CalculadoraIMC

# 2) Importar o pacote de
# testes unitários chamado "unittest"
import unittest

# 3) Criando a classe de
# testes unitários
class TestCalculadoraIMC(unittest.TestCase):
    
    # 4) Criando o objeto
    # que herdará a classe
    # "Calculadora"
    
    # OBS: é necessário usar
    # o método chamado "setUp()"
    def setUp(self):
        self.calc = CalculadoraIMC()
        
    def test_resultado(self):
        #Testando o resultado de magreza
        self.assertEqual(self.calcIMC.resultado(60, 1.90), 'magreza')
        
    
        
# Executar a classe de
# testes unitários
if __name__ == '__main__':
    unittest.main()
