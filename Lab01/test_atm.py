import unittest
from atm import Cajero

class CajeroTest(unittest.TestCase):
  def setUp(self):
      self.cajero = Cajero()
  
  def test_retiro_saldo_suficiente(self):
      self.assertTrue(self.cajero.validar_retiro(23))

  def test_retiro_saldo_insuficiente(self):
      self.assertFalse(self.cajero.validar_retiro(5001))

  def test_retiro_maximo(self):
      
      self.assertTrue(self.cajero.retiroMaximo(2000))
      self.assertFalse(self.cajero.retiroMaximo(4000))

  def test_deposito_maximo(self):
      
      self.assertTrue(self.cajero.depositoMaximo(5000))
      self.assertFalse(self.cajero.depositoMaximo(15000))

if __name__ == '__main__':
    unittest.main()
